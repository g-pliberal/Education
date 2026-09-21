"""Ce que le site doit tenir, et que personne ne vérifiera à la main.

    python3 -m unittest discover -s tests

Ces tests ne jugent pas la prose : ils tiennent les promesses que le dépôt
fait sur sa méthode — un chiffre ne s'écrit qu'une fois, il figure sur la page
« Sources », les liens mènent quelque part, et le HTML publié est bien celui
que le code produit.
"""

from __future__ import annotations

import re
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "src"))

from education import gabarit  # noqa: E402
from education.donnees import CHIFFRES, FAITS  # noqa: E402
from education.pages import PAGES  # noqa: E402

# Les balises qui n'ont pas de fermeture : les compter comme ouvertes ferait
# échouer tout contrôle d'équilibre.
ORPHELINES = {"meta", "link", "br", "hr", "img", "input", "source"}


class _Equilibre(HTMLParser):
    """Vérifie qu'aucune balise ne reste ouverte, ni ne ferme dans le désordre."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pile: list[str] = []
        self.fautes: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag not in ORPHELINES:
            self.pile.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in ORPHELINES:
            return
        if not self.pile:
            self.fautes.append(f"</{tag}> sans ouverture")
        elif self.pile[-1] != tag:
            self.fautes.append(f"</{tag}> alors que <{self.pile[-1]}> est ouvert")
            if tag in self.pile:
                while self.pile and self.pile.pop() != tag:
                    pass
        else:
            self.pile.pop()


def rendues() -> dict[str, str]:
    return {nom: gabarit.page(nom, rendre()) for nom, rendre in PAGES.items()}


class TestPages(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pages = rendues()

    def test_html_equilibre(self) -> None:
        for nom, document in self.pages.items():
            with self.subTest(page=nom):
                analyseur = _Equilibre()
                analyseur.feed(document)
                self.assertEqual(analyseur.fautes, [])
                self.assertEqual(analyseur.pile, [],
                                 f"balises restées ouvertes : {analyseur.pile}")

    def test_un_seul_titre_de_niveau_un(self) -> None:
        """Un `<h1>` par page, et un seul : c'est l'affiche.

        Deux titres de premier niveau sur une page privent les synthèses
        vocales du seul repère qui dit « voici de quoi parle cette page ».
        """
        for nom, document in self.pages.items():
            with self.subTest(page=nom):
                self.assertEqual(document.count("<h1>"), 1)

    def test_entete_complete(self) -> None:
        for nom, document in self.pages.items():
            with self.subTest(page=nom):
                self.assertIn('<html lang="fr">', document)
                self.assertIn('name="description"', document)
                self.assertIn("<title>", document)
                self.assertIn('class="evitement"', document)
                self.assertIn('id="contenu"', document)

    def test_page_courante_signalee(self) -> None:
        """L'onglet actif porte `aria-current`, et pas seulement une couleur."""
        for nom, document in self.pages.items():
            with self.subTest(page=nom):
                self.assertEqual(document.count('aria-current="page"'), 1)

    def test_liens_internes_existent(self) -> None:
        """Aucun lien du site ne mène à une page ou à une ancre absente."""
        noms = set(PAGES)
        for nom, document in self.pages.items():
            ancres = set(re.findall(r'id="([^"]+)"', document))
            for cible in re.findall(r'href="([^"]+)"', document):
                if cible.startswith(("http://", "https://", "mailto:")):
                    continue
                with self.subTest(page=nom, lien=cible):
                    if cible.startswith("#"):
                        self.assertIn(cible[1:], ancres)
                    elif cible.endswith(".html"):
                        self.assertIn(cible[: -len(".html")], noms)
                    else:
                        # Feuille de style, icône : des fichiers du dépôt,
                        # servis à côté des pages.
                        self.assertTrue((RACINE / cible).exists(), cible)

    def test_chaque_page_est_atteignable(self) -> None:
        """Le bandeau mène aux huit pages : aucune n'est orpheline."""
        for nom in PAGES:
            with self.subTest(page=nom):
                self.assertIn(f'href="{nom}.html"', self.pages["index"])


class TestChiffres(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pages = rendues()
        cls.hors_sources = "".join(
            document for nom, document in cls.pages.items() if nom != "sources"
        )

    def test_aucun_chiffre_inutilise(self) -> None:
        """Un chiffre au registre qu'aucune page ne cite est un chiffre mort.

        Il aurait l'air sourcé sur la page « Sources » sans rien étayer nulle
        part : c'est exactement la manière dont un site accumule des chiffres
        qu'il ne sait plus justifier.
        """
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                self.assertIn(gabarit.typographie(chiffre.texte),
                              gabarit.typographie(self.hors_sources))

    def test_page_sources_complete(self) -> None:
        """Chaque chiffre figure sur la page « Sources », avec son émetteur."""
        page = self.pages["sources"]
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                attendu = gabarit.typographie(
                    gabarit.echapper(chiffre.libelle))[:60]
                self.assertIn(attendu, page)
                self.assertIn(
                    gabarit.typographie(gabarit.echapper(chiffre.source)), page)
                self.assertIn(chiffre.annee, page)

    def test_aucun_fait_inutilise(self) -> None:
        """Un fait au registre qu'aucune page ne cite est un fait mort.

        Même raison que pour les chiffres : il aurait l'air sourcé sur la
        page « Sources » sans rien étayer nulle part.
        """
        for cle, f in FAITS.items():
            with self.subTest(fait=cle):
                self.assertIn(
                    gabarit.typographie(gabarit.echapper(f.source)),
                    gabarit.typographie(self.hors_sources))

    def test_page_sources_porte_les_faits(self) -> None:
        """Chaque fait figure sur la page « Sources », daté et attribué."""
        page = self.pages["sources"]
        for cle, f in FAITS.items():
            with self.subTest(fait=cle):
                self.assertIn(
                    gabarit.typographie(gabarit.echapper(f.enonce))[:60], page)
                self.assertIn(
                    gabarit.typographie(gabarit.echapper(f.source)), page)
                self.assertIn(f.annee, page)

    def test_chaque_fait_a_une_source_datee(self) -> None:
        for cle, f in FAITS.items():
            with self.subTest(fait=cle):
                self.assertTrue(f.enonce.strip())
                self.assertTrue(f.source.strip())
                self.assertRegex(f.annee, r"^\d{4}$")
                self.assertTrue(f.url.startswith("https://"))

    def test_chaque_chiffre_a_une_source_datee(self) -> None:
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                self.assertTrue(chiffre.source.strip())
                self.assertRegex(chiffre.annee, r"^\d{4}$")
                self.assertTrue(chiffre.url.startswith("https://"))


class TestTypographie(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pages = rendues()

    def test_unite_liee_au_nombre(self) -> None:
        """« 6,8 % » ne se coupe pas en fin de ligne."""
        for nom, document in self.pages.items():
            texte = re.sub(r"<[^>]*>", "", document)
            with self.subTest(page=nom):
                self.assertNotRegex(texte, r"\d [%€]")

    def test_balises_intactes(self) -> None:
        """La passe typographique ne touche jamais à une adresse.

        Une espace insécable glissée dans un `href` donnerait un lien mort, et
        c'est le genre de faute qu'aucune relecture ne voit.
        """
        for nom, document in self.pages.items():
            with self.subTest(page=nom):
                for balise in re.findall(r"<[^>]*>", document):
                    self.assertNotIn("\u202f", balise)
                    self.assertNotIn("\u00a0", balise)


class TestPublication(unittest.TestCase):

    def test_site_publie_a_jour(self) -> None:
        """Les fichiers du dépôt sont ceux que le code produit.

        Sans ce test, une correction apportée au code et non reconstruite
        laisserait en ligne une page périmée — et personne ne le verrait, le
        HTML publié étant précisément ce qu'on ne relit pas.
        """
        resultat = subprocess.run(
            [sys.executable, "scripts/construire_site.py", "--verifier"],
            cwd=RACINE, capture_output=True, text=True,
        )
        self.assertEqual(resultat.returncode, 0, resultat.stderr)

    def test_ressources_presentes(self) -> None:
        """Tout ce que la feuille de style demande existe dans le dépôt."""
        for police in re.findall(r"url\(([^)]+)\)", gabarit.STYLE):
            with self.subTest(fichier=police):
                self.assertTrue((RACINE / "moteur" / police).exists())
        self.assertTrue((RACINE / "moteur" / "icone.svg").exists())
        self.assertTrue((RACINE / ".nojekyll").exists(),
                        "sans .nojekyll, les pages GitHub ignorent les "
                        "dossiers commençant par un tiret bas")


if __name__ == "__main__":
    unittest.main()
