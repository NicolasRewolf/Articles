"""Tests stdlib du wrapper DataForSEO.

Deux gestes valent d'être couverts ici, parce qu'ils échouent en silence :

1. **La résolution des credentials.** Trois sources possibles, dont la
   configuration Claude Code. Se tromper d'ordre, c'est utiliser un compte
   inattendu — et facturer le mauvais solde.
2. **La détection d'erreur d'API.** DataForSEO répond **HTTP 200 même quand la
   tâche échoue** : le statut utile est `status_code` (20000 = OK) dans le corps.
   Sans contrôle, un quota épuisé ou une requête refusée ressort en liste vide
   et se confond avec « aucune donnée » — soit un Bloc B faussement vide.

Aucun appel réseau : transport injecté, fonctions pures.

Lancer : python3 scripts/test_dataforseo.py
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from scripts import dataforseo as dfs  # noqa: E402

CREDS = ("compte-test", "mdp-test")


def test_credentials_ordre_des_sources():
    """L'environnement gagne sur `.env`, qui gagne sur la config Claude Code."""
    env = {"DATAFORSEO_USERNAME": "env", "DATAFORSEO_PASSWORD": "x"}
    dotenv = {"DATAFORSEO_USERNAME": "dotenv", "DATAFORSEO_PASSWORD": "x"}
    claude = {"DATAFORSEO_USERNAME": "claude", "DATAFORSEO_PASSWORD": "x"}
    assert dfs.resoudre_credentials([env, dotenv, claude])[0] == "env"
    assert dfs.resoudre_credentials([{}, dotenv, claude])[0] == "dotenv"
    assert dfs.resoudre_credentials([{}, {}, claude])[0] == "claude"
    print("OK credentials — ordre environnement > .env > config Claude Code")


def test_credentials_source_incomplete_ignoree():
    """Une source qui ne porte que la moitié des clés ne doit pas gagner."""
    partielle = {"DATAFORSEO_USERNAME": "moitie"}
    complete = {"DATAFORSEO_USERNAME": "entier", "DATAFORSEO_PASSWORD": "x"}
    assert dfs.resoudre_credentials([partielle, complete])[0] == "entier"
    print("OK credentials — source incomplete ignoree au profit de la suivante")


def test_credentials_alias_login():
    """`DATAFORSEO_LOGIN` est accepté comme alias de `DATAFORSEO_USERNAME`."""
    source = {"DATAFORSEO_LOGIN": "alias", "DATAFORSEO_PASSWORD": "x"}
    assert dfs.resoudre_credentials([source]) == ("alias", "x")
    print("OK credentials — alias DATAFORSEO_LOGIN reconnu")


def test_credentials_absents_message_actionnable():
    """Rien nulle part : l'erreur doit nommer les trois endroits cherchés."""
    try:
        dfs.resoudre_credentials([{}, {}, {}])
    except RuntimeError as e:
        message = str(e)
        assert "DATAFORSEO_USERNAME" in message
        assert ".env" in message
        assert ".claude.json" in message
        print("OK credentials — absence signalee avec les sources cherchees")
        return
    raise AssertionError("une absence de credentials doit lever RuntimeError")


def test_lots_decoupe_et_reste():
    assert dfs.lots([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert dfs.lots([1, 2], 10) == [[1, 2]]
    assert dfs.lots([], 10) == []
    try:
        dfs.lots([1], 0)
    except ValueError:
        print("OK lots — decoupe, reste, liste vide, taille invalide")
        return
    raise AssertionError("une taille de lot nulle doit lever ValueError")


def test_erreur_api_remontee_en_clair():
    """HTTP 200 + status_code d'erreur = RuntimeError, jamais une liste vide."""
    try:
        dfs._resultats({"status_code": 40200, "status_message": "Payment Required"})
    except RuntimeError as e:
        assert "40200" in str(e) and "Payment Required" in str(e)
    else:
        raise AssertionError("un status_code d'erreur doit lever RuntimeError")

    try:
        dfs._resultats({"status_code": 20000, "tasks": [
            {"status_code": 40501, "status_message": "Invalid Field"}]})
    except RuntimeError as e:
        assert "40501" in str(e)
        print("OK erreurs — statut global et statut de tache remontes")
        return
    raise AssertionError("un status_code de tache en erreur doit lever RuntimeError")


def test_resultats_vides_sans_erreur():
    """Une réponse OK mais sans résultat n'est pas une erreur."""
    assert dfs._resultats({"status_code": 20000, "tasks": []}) == []
    assert dfs._resultats({"status_code": 20000,
                           "tasks": [{"status_code": 20000, "result": None}]}) == []
    print("OK resultats — reponse OK sans donnee rend une liste vide")


def test_volumes_batche_et_envoie_le_bon_payload():
    """Deux lots ⇒ deux appels ; chaque payload porte location et langue."""
    envoyes = []

    def transport(url, *, data=None, headers=None, method="GET", timeout=30, label=""):
        envoyes.append(json.loads(data.decode()))
        return {"status_code": 20000,
                "tasks": [{"status_code": 20000, "result": [{"keyword": "k"}]}]}

    items = dfs.volumes(["a", "b", "c"], taille_lot=2,
                        transport=transport, credentials=CREDS)
    assert len(envoyes) == 2
    assert envoyes[0][0]["keywords"] == ["a", "b"]
    assert envoyes[1][0]["keywords"] == ["c"]
    assert envoyes[0][0]["location_code"] == dfs.LOCATION_DEFAUT
    assert envoyes[0][0]["language_code"] == dfs.LANGUE_DEFAUT
    assert len(items) == 2
    print("OK volumes — batching et payload (location, langue) conformes")


def test_extraire_serp_separe_organiques_et_paa():
    """Les blocs SERP sont hétérogènes : on trie, on n'agrège pas à l'aveugle."""
    resultat = {
        "keyword": "cour criminelle departementale",
        "se_results_count": 1234,
        "items": [
            {"type": "organic", "rank_group": 1, "domain": "service-public.fr",
             "title": "La cour criminelle", "url": "https://service-public.fr/x"},
            {"type": "video", "title": "une video"},
            {"type": "people_also_ask", "items": [
                {"title": "Qui juge un viol ?"}, {"title": "Y a-t-il un jury ?"}]},
            {"type": "people_also_ask_element", "title": "Peut-on faire appel ?"},
            {"type": "organic", "rank_group": 2, "domain": "justice.gouv.fr",
             "title": "Justice", "url": "https://justice.gouv.fr/y"},
        ],
    }
    vue = dfs.extraire_serp(resultat)
    assert [o["domaine"] for o in vue["organiques"]] == ["service-public.fr",
                                                         "justice.gouv.fr"]
    assert vue["paa"] == ["Qui juge un viol ?", "Y a-t-il un jury ?",
                          "Peut-on faire appel ?"]
    assert vue["total"] == 1234
    print("OK extraire_serp — organiques et PAA separes, autres blocs ignores")


def test_ligne_volume_supporte_les_valeurs_absentes():
    """Un mot-clé sans données doit s'afficher « n/d », pas planter ni mentir."""
    ligne = dfs.ligne_volume({"keyword": "terme rare", "search_volume": None,
                              "competition": None, "competition_index": None,
                              "cpc": None})
    assert "n/d" in ligne and "terme rare" in ligne
    assert "0" not in ligne.split("·")[0], "un volume inconnu ne doit pas devenir 0"
    pleine = dfs.ligne_volume({"keyword": "cour d'assises", "search_volume": 3600,
                               "competition": "LOW", "competition_index": 2,
                               "cpc": 1.27})
    assert "3 600" in pleine and "LOW" in pleine
    print("OK ligne_volume — valeurs absentes rendues n/d, jamais 0")


if __name__ == "__main__":
    test_credentials_ordre_des_sources()
    test_credentials_source_incomplete_ignoree()
    test_credentials_alias_login()
    test_credentials_absents_message_actionnable()
    test_lots_decoupe_et_reste()
    test_erreur_api_remontee_en_clair()
    test_resultats_vides_sans_erreur()
    test_volumes_batche_et_envoie_le_bon_payload()
    test_extraire_serp_separe_organiques_et_paa()
    test_ligne_volume_supporte_les_valeurs_absentes()
    print("\nTOUS LES TESTS PASSENT")
