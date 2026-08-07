#!/usr/bin/env python3
"""Lance toutes les suites de tests des scripts.

    python3 scripts/run_tests.py

Sortie : code 0 si tout passe, 1 sinon. Stdlib uniquement, aucun réseau.
Chaque suite reste lançable seule (`python3 scripts/test_<suite>.py`).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent


def main() -> int:
    suites = sorted(ICI.glob("test_*.py"))
    echecs: list[str] = []

    for suite in suites:
        print(f"\n─── {suite.name} " + "─" * max(0, 60 - len(suite.name)))
        resultat = subprocess.run([sys.executable, str(suite)])
        if resultat.returncode != 0:
            echecs.append(suite.name)

    print("\n" + "═" * 64)
    if echecs:
        print(f"ÉCHEC — {len(echecs)}/{len(suites)} suite(s) en erreur : {', '.join(echecs)}")
        return 1
    print(f"OK — {len(suites)} suite(s), tout passe.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
