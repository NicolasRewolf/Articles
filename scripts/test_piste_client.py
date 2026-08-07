"""Tests stdlib du client PISTE — AUCUN appel réseau.

Le transport est le seam : on y branche un espion qui enregistre ce qui part.
C'est le second adapter — sans lui, le seam ne serait qu'hypothétique, et
`judilibre` / `legifrance` resteraient invérifiables autrement qu'en tapant
l'API de production.

Lancer : python3 scripts/test_piste_client.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from scripts import judilibre, legifrance, piste_auth  # noqa: E402
from scripts.piste_auth import PisteClient  # noqa: E402

ENV_SANDBOX = {"PISTE_ENV": "sandbox", "PISTE_CLIENT_ID": "id", "PISTE_CLIENT_SECRET": "secret"}
ENV_PROD = {"PISTE_ENV": "prod", "PISTE_CLIENT_ID": "id", "PISTE_CLIENT_SECRET": "secret"}


class TransportEspion:
    """Adapter de test : enregistre l'appel, rend une réponse fixe."""

    def __init__(self, reponse: dict | None = None) -> None:
        self.appels: list[dict] = []
        self.reponse = reponse if reponse is not None else {"total": 0, "results": []}

    def __call__(self, url, *, data=None, headers=None, method="GET", timeout=30, label="API"):
        self.appels.append({"url": url, "data": data, "headers": headers or {},
                            "method": method, "timeout": timeout, "label": label})
        return self.reponse


def _client(chemin: str, label: str, espion: TransportEspion, env=ENV_SANDBOX) -> PisteClient:
    return PisteClient(chemin, label=label, transport=espion, env=env,
                       jeton="jeton-de-test", cache=False)


def _query(url: str) -> dict[str, list[str]]:
    return urllib.parse.parse_qs(urllib.parse.urlparse(url).query)


def test_judilibre_url_et_params_multivalues():
    espion = TransportEspion()
    judilibre.search("faute inexcusable", size=3, chamber=["civ2", "crim"],
                     client=_client(judilibre.JUDILIBRE_PATH, "Judilibre", espion))

    assert len(espion.appels) == 1, espion.appels
    appel = espion.appels[0]
    assert appel["method"] == "GET", appel["method"]
    assert appel["url"].startswith(
        "https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/search?"), appel["url"]

    q = _query(appel["url"])
    assert q["chamber"] == ["civ2", "crim"], q  # multivalué : la clé est répétée
    assert q["page_size"] == ["3"] and q["query"] == ["faute inexcusable"], q
    assert "order" not in q, "un param None ne doit pas partir"
    assert appel["headers"]["Authorization"] == "Bearer jeton-de-test", appel["headers"]
    assert appel["label"] == "Judilibre"
    print("OK judilibre — URL de service, params multivalues, None omis, Bearer pose")


def test_legifrance_post_json():
    espion = TransportEspion()
    legifrance.search("loi badinter", fond="LODA_DATE",
                      client=_client(legifrance.LEGIFRANCE_PATH, "Légifrance", espion))

    appel = espion.appels[0]
    assert appel["method"] == "POST", appel["method"]
    assert appel["url"] == (
        "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/search"), appel["url"]
    assert appel["headers"]["Content-Type"] == "application/json", appel["headers"]
    corps = json.loads(appel["data"].decode("utf-8"))
    assert corps["fond"] == "LODA_DATE", corps
    assert corps["recherche"]["pageSize"] == 10, corps
    assert appel["label"] == "Légifrance"
    print("OK legifrance — POST JSON, corps conforme, libelle d'erreur porte")


def test_environnement_choisit_la_base():
    espion = TransportEspion()
    judilibre.get_decision("abc", client=_client(judilibre.JUDILIBRE_PATH, "J", espion, ENV_PROD))
    assert espion.appels[0]["url"].startswith(
        "https://api.piste.gouv.fr/cassation/judilibre/v1.0/decision?"), espion.appels[0]["url"]
    print("OK environnement — prod et sandbox visent des bases distinctes")


def test_configuration_lue_une_seule_fois():
    """Avant : api_base() puis get_token() relisaient `.env` à CHAQUE appel."""
    lectures = {"n": 0}
    original = piste_auth._load_env
    piste_auth._load_env = lambda: (lectures.__setitem__("n", lectures["n"] + 1), ENV_SANDBOX)[1]
    try:
        espion = TransportEspion()
        api = PisteClient("/svc", label="X", transport=espion, jeton="j", cache=False)
        for _ in range(5):
            api.get("/ping")
    finally:
        piste_auth._load_env = original

    assert lectures["n"] == 1, f"attendu 1 lecture de configuration, obtenu {lectures['n']}"
    assert len(espion.appels) == 5
    print("OK configuration — 1 lecture pour 5 appels (contre 2 par appel avant)")


def test_oauth_passe_par_le_transport():
    """Sans jeton fourni, l'authentification emprunte le MÊME seam."""
    espion = TransportEspion({"access_token": "jeton-frais", "expires_in": 3600})
    api = PisteClient("/svc", label="X", transport=espion, env=ENV_SANDBOX, cache=False)
    api.get("/ping")

    assert len(espion.appels) == 2, [a["url"] for a in espion.appels]
    oauth, appel = espion.appels
    assert oauth["url"] == "https://sandbox-oauth.piste.gouv.fr/api/oauth/token", oauth["url"]
    assert oauth["method"] == "POST"
    corps = urllib.parse.parse_qs(oauth["data"].decode("utf-8"))
    assert corps["grant_type"] == ["client_credentials"], corps
    assert appel["headers"]["Authorization"] == "Bearer jeton-frais", appel["headers"]
    print("OK oauth — l'authentification passe par le transport, aucun reseau requis")


def test_credentials_manquants_message_actionnable():
    espion = TransportEspion()
    api = PisteClient("/svc", label="X", transport=espion,
                      env={"PISTE_ENV": "sandbox"}, cache=False)
    try:
        api.get("/ping")
    except RuntimeError as e:
        assert "PISTE_CLIENT_ID" in str(e), e
        assert not espion.appels, "aucun appel ne doit partir sans credentials"
        print("OK credentials — echec explicite avant tout appel")
        return
    raise AssertionError("un appel sans credentials aurait du lever")


if __name__ == "__main__":
    test_judilibre_url_et_params_multivalues()
    test_legifrance_post_json()
    test_environnement_choisit_la_base()
    test_configuration_lue_une_seule_fois()
    test_oauth_passe_par_le_transport()
    test_credentials_manquants_message_actionnable()
    print("\nTOUS LES TESTS PASSENT")
