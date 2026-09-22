#!/usr/bin/env python3
"""Écrit le site : les neuf pages, la feuille de style, l'icône.

    python3 scripts/construire_site.py

Les fichiers produits sont versionnés — c'est ce qui permet aux pages GitHub
de servir le site sans rien exécuter, et à quiconque de lire le HTML publié
sans installer Python. Ils ne se modifient donc jamais à la main : le script
les réécrit, et un test vérifie qu'ils sont bien à jour (`--verifier`).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "src"))

from education import gabarit  # noqa: E402
from education.pages import PAGES  # noqa: E402


def fichiers() -> dict[Path, str]:
    """Tout ce que le site publie, et son contenu attendu."""
    produits: dict[Path, str] = {
        RACINE / "moteur" / "style.css": gabarit.STYLE,
        RACINE / "moteur" / "icone.svg": gabarit.ICONE,
    }
    for nom, rendre in PAGES.items():
        produits[RACINE / f"{nom}.html"] = gabarit.page(nom, rendre())
    return produits


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument(
        "--verifier", action="store_true",
        help="ne rien écrire, et sortir en erreur si un fichier publié "
             "diffère de ce que le code produit.")
    options = analyseur.parse_args()

    ecarts: list[Path] = []
    for chemin, contenu in fichiers().items():
        ancien = chemin.read_text(encoding="utf-8") if chemin.exists() else None
        if ancien == contenu:
            continue
        ecarts.append(chemin.relative_to(RACINE))
        if not options.verifier:
            chemin.parent.mkdir(parents=True, exist_ok=True)
            chemin.write_text(contenu, encoding="utf-8")

    if options.verifier:
        if ecarts:
            print("Fichiers publiés périmés — relancer "
                  "`python3 scripts/construire_site.py` :", file=sys.stderr)
            for chemin in ecarts:
                print(f"  {chemin}", file=sys.stderr)
            return 1
        print("Le site publié est à jour.")
        return 0

    if ecarts:
        for chemin in ecarts:
            print(f"écrit  {chemin}")
    else:
        print("Rien à écrire : le site était déjà à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
