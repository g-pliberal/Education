"""Le gabarit du site : la feuille de style, et les fragments qui la portent.

Le style est ici, dans une chaîne, et non dans `moteur/style.css` :
`scripts/construire_site.py` l'extrait au moment de la construction. La raison
est la même que pour les chiffres — un seul endroit. Le fichier CSS est un
produit, pas une source, et le README le dit.

L'apparence est celle du dépôt `retraitecomptenotionelle`, à dessein : les
deux sites sont deux outils du même parti, et doivent se reconnaître comme
tels. Les jetons de couleur, les deux polices, le bandeau collé, l'affiche de
tête, les engagements numérotés, les repères chiffrés — tout cela est repris
tel quel. Ce qui ne servait qu'au simulateur de retraite (graphiques, cascade,
formulaire, barre de partage) ne l'est pas : une feuille de style qui décrit
des composants absents est une feuille qu'on n'ose plus modifier.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass

DEPOT = "https://github.com/g-pliberal/education"
SITE_PARENT = "https://partiliberalfrancais.fr/"

# -- la navigation -----------------------------------------------------------
#
# Neuf pages, sous quatre étiquettes de groupe. Les étiquettes ne s'affichent
# pas : elles sont lues par les synthèses vocales, pour qui une barre de neuf
# liens sans structure est une liste de neuf liens sans structure.

GROUPES_NAVIGATION: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = (
    ("Le site", (("index", "Accueil"),)),
    ("Le constat", (("resultats", "Résultats"),
                    ("depense", "Dépense"),
                    ("gouvernance", "Qui décide"))),
    ("La proposition", (("proposition", "La proposition"),
                        ("comparaisons", "Ailleurs"),
                        ("chiffrage", "Chiffrage"))),
    ("La confiance", (("objections", "Objections"),
                      ("sources", "Sources"))),
)

TITRES: dict[str, str] = {
    "index": "L'école française, et ce qu'elle pourrait être",
    "resultats": "Résultats",
    "depense": "Dépense",
    "gouvernance": "Qui décide",
    "proposition": "La proposition",
    "comparaisons": "Ailleurs en Europe",
    "chiffrage": "Chiffrage",
    "objections": "Objections",
    "sources": "Sources",
}

DESCRIPTIONS: dict[str, str] = {
    "index": "Ce que la politique éducative française fait, ce qu'elle coûte, "
             "ce qu'elle obtient — et l'alternative libérale : le financement "
             "qui suit l'élève, l'autonomie des établissements, l'évaluation "
             "publique des résultats.",
    "resultats": "PISA, TIMSS, PIRLS, Journée défense et citoyenneté : ce que "
                 "les élèves français savent faire, et ce qu'ils ne savent "
                 "plus faire.",
    "depense": "197,1 milliards d'euros, 6,8 % du PIB, et un euro mal réparti "
               "entre l'écolier et l'étudiant : où va l'argent de l'école.",
    "gouvernance": "55 % des décisions prises au niveau central, 10 % des "
                   "chefs d'établissement qui recrutent leur équipe : qui "
                   "décide vraiment dans l'école française.",
    "proposition": "Sept réformes libérales de l'école : le financement suit "
                   "l'élève, l'établissement s'administre, les résultats se "
                   "publient, le métier d'enseignant redevient un métier.",
    "comparaisons": "Pays-Bas, Danemark, Estonie, Suède : ce que la liberté "
                    "scolaire donne quand elle est bien faite, et ce qu'elle "
                    "coûte quand elle est mal faite.",
    "chiffrage": "Ce que coûte le programme libéral pour l'école, poste par "
                 "poste, par rapport à la situation actuelle : formules, "
                 "hypothèses, fourchettes, et qui y gagne ou y perd.",
    "objections": "Les dix objections sérieuses à la liberté scolaire, et ce "
                  "que nous y répondons — y compris quand elles ont raison.",
    "sources": "Tous les chiffres cités sur ce site, avec leur année, leur "
               "source et son adresse.",
}


def echapper(texte: str) -> str:
    """Le texte tel qu'il s'écrit dans du HTML."""
    return html.escape(texte, quote=False)


def lien(page: str) -> str:
    """L'adresse d'une page du site depuis n'importe quelle autre.

    Le site est fait de fichiers posés côte à côte : l'accueil est
    `index.html`, et rien ne dépend du répertoire où il est servi. C'est ce qui
    permet de l'ouvrir depuis un disque, de le servir sous `/education/` sur
    les pages GitHub, ou de le glisser sous n'importe quel chemin du site du
    parti, sans toucher une ligne.
    """
    return f"{page}.html"


def navigation(page_active: str) -> str:
    def liens_du_groupe(pages: tuple[tuple[str, str], ...]) -> str:
        return "".join(
            f'<a href="{lien(page)}"'
            + (' aria-current="page"' if page == page_active else "")
            + f">{echapper(libelle)}</a>"
            for page, libelle in pages
        )

    return "".join(
        f'<span class="groupe"><span class="etiquette">{echapper(etiquette)}</span>'
        f'<span class="liens">{liens_du_groupe(pages)}</span></span>'
        for etiquette, pages in GROUPES_NAVIGATION
    )


def entete(page_active: str) -> str:
    """Bandeau de tête, précédé du lien d'évitement.

    Le lien d'évitement est le premier élément parcouru au clavier : sans lui,
    atteindre le contenu impose de traverser les neuf onglets à chaque page.
    """
    return f"""<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="bandeau"><div class="interieur">
  <p class="nom"><a href="{lien('index')}"><span>Parti libéral français — École</span></a></p>
  <nav aria-label="Navigation principale">{navigation(page_active)}</nav>
</div></header>"""


def affiche(surtitre: str, titre: str, chapeau: str) -> str:
    """Le bloc de tête d'une page : sur-titre, titre massif, chapeau.

    C'est l'unité qui fait de chaque page une affiche. Le titre est mis en
    capitales par le STYLE, jamais dans le texte : une capitale écrite dans le
    texte serait épelée par certaines synthèses vocales, et ne se copierait pas
    proprement.
    """
    return (f'<div class="affiche"><p class="surtitre">{echapper(surtitre)}</p>'
            f'<h1>{titre}</h1><p class="chapeau">{chapeau}</p></div>')


def pied() -> str:
    """Pied de page.

    Il porte ce qu'il faut savoir avant de citer ce site : ce qu'il est, ce
    qu'il n'est pas, et où sont les chiffres. Il ne porte aucune mention
    légale : le site qui l'héberge édite la page, et deux déclarations
    concurrentes valent moins qu'une.
    """
    return f"""<footer>
  <p><strong>Ce site est un document de campagne, pas un rapport officiel.</strong>
  Il n'émane ni du ministère, ni d'une administration. Les constats sont
  sourcés un par un sur la page <a href="{lien('sources')}">Sources</a> ; les
  propositions, elles, sont des choix politiques, et se discutent comme tels.</p>
  <p>Chaque chiffre porte son année et son émetteur — DEPP, OCDE, Cour des
  comptes, Conseil d'analyse économique. Les comparaisons internationales sont
  fragiles par nature : elles rapportent des systèmes qui ne scolarisent ni les
  mêmes élèves, ni au même âge. Nous les citons pour ce qu'elles montrent, et
  la page <a href="{lien('objections')}">Objections</a> dit où elles s'arrêtent.</p>
  <p>Textes et code sur <a href="{DEPOT}">GitHub</a> (code sous licence Apache 2.0,
  textes sous <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>).
  Une erreur, un chiffre périmé, une objection oubliée : ouvrez une
  <a href="{DEPOT}/issues">issue</a>.</p>
  <p class="retour-site">Un document du
  <a href="{SITE_PARENT}" target="_top">Parti libéral français</a>.</p>
</footer>"""


# -- fragments ---------------------------------------------------------------


@dataclass(frozen=True)
class Repere:
    """Un chiffre d'ouverture de page : l'étiquette, la valeur, la précision."""

    etiquette: str
    valeur: str
    precision: str = ""


def reperes(elements: tuple[Repere, ...]) -> str:
    """Les trois ou quatre chiffres qu'on emporte si on ne lit rien d'autre.

    L'étiquette passe au-dessus du nombre : on lit « ce que l'école coûte »
    puis « 197,1 Md€ », dans cet ordre, et non un nombre dont on cherche le
    sens.
    """
    cases = "".join(
        f'<div class="fiche"><span class="etiquette">{echapper(e.etiquette)}</span>'
        f'<span class="valeur">{echapper(e.valeur)}</span>'
        + (f'<span class="precision">{e.precision}</span>' if e.precision else "")
        + "</div>"
        for e in elements
    )
    return f'<div class="fiches reperes">{cases}</div>'


@dataclass(frozen=True)
class Engagement:
    """Un engagement du programme : son chiffre, sa promesse, son détail."""

    chiffre: str
    promesse: str
    detail: str


def engagements(elements: tuple[Engagement, ...], titre: str) -> str:
    """Les engagements, numérotés, deux par rangée.

    C'est le bloc que l'on photographie et que l'on partage. Il n'est pas un
    résumé de la page : il est ce que le programme promet, dit en autant de
    mots qu'il en faut pour être vérifiable.
    """
    cases = "".join(
        f'<div class="engagement"><p class="rang">{i:02d}</p>'
        f'<p class="chiffre">{echapper(e.chiffre)}</p>'
        f'<p class="promesse">{e.promesse}</p>'
        f'<p class="detail">{e.detail}</p></div>'
        for i, e in enumerate(elements, start=1)
    )
    return (f'<section class="engagements" aria-label="{echapper(titre)}">'
            f'<div class="grille">{cases}</div></section>')


def points(elements: tuple[tuple[str, str], ...]) -> str:
    """Quelques idées, une par bloc, de même poids.

    C'est ce qui les distingue d'une liste, où la première l'emporte.
    """
    cases = "".join(
        f'<div class="point"><h3>{echapper(titre)}</h3><p>{corps}</p></div>'
        for titre, corps in elements
    )
    return f'<div class="points">{cases}</div>'


def note(corps: str, genre: str = "") -> str:
    """Un encart : une réserve, un résumé, un point de vigilance."""
    classes = f"note {genre}".strip()
    return f'<div class="{classes}">{corps}</div>'


def encadre(corps: str) -> str:
    """Le bloc cerné d'or : ce qui mérite d'être lu à part."""
    return f'<div class="encadre">{corps}</div>'


def carte(corps: str) -> str:
    return f'<div class="carte">{corps}</div>'


def paire(gauche: str, droite: str) -> str:
    """Deux colonnes de même poids, qui se superposent quand la place manque."""
    return f'<div class="paire"><div>{gauche}</div><div>{droite}</div></div>'


def gestes(elements: tuple[str, ...]) -> str:
    """Une liste numérotée dont le rang se voit : les étapes d'une réforme."""
    lignes = "".join(
        f'<li><span class="rang">{i}</span><span>{corps}</span></li>'
        for i, corps in enumerate(elements, start=1)
    )
    return f'<ol class="gestes">{lignes}</ol>'


def leviers(elements: tuple[str, ...]) -> str:
    """Une liste d'items détachés du texte, sans hiérarchie entre eux."""
    lignes = "".join(f"<li>{corps}</li>" for corps in elements)
    return f'<ul class="leviers">{lignes}</ul>'


def plan(elements: tuple[tuple[str, str], ...]) -> str:
    """Le plan d'une page longue : ce qu'elle contient, en liens d'ancrage."""
    lignes = "".join(
        f'<li><a href="#{ancre}">{echapper(libelle)}</a></li>'
        for ancre, libelle in elements
    )
    return ('<nav class="plan" aria-label="Plan de la page">'
            '<p class="etiquette">Sur cette page</p>'
            f"<ol>{lignes}</ol></nav>")


def section_cle(ancre: str, question: str, reponse: str, source: str = "") -> str:
    """Une question, sa réponse, sa source.

    Encadrée pour se découper : une capture de ce bloc se comprend hors du
    site, et c'est exactement ce qu'on en fait.
    """
    bas = f'<p class="source">{source}</p>' if source else ""
    return (f'<section class="cle" id="{ancre}"><h3>{echapper(question)}</h3>'
            f'<p class="reponse">{reponse}</p>{bas}</section>')


def tableau(legende: str, entetes: tuple[str, ...],
            lignes: tuple[tuple[str, ...], ...],
            classes_colonnes: tuple[str, ...] = ()) -> str:
    """Un tableau qui défile au lieu de faire défiler la page.

    La légende est énoncée par les synthèses vocales avant le contenu, et se
    lit à l'écran comme l'intitulé de la grille. La première colonne est
    l'en-tête de sa ligne : c'est ce qui permet à un lecteur d'écran d'annoncer
    « Danemark, part du privé, 15 à 16 % » plutôt que trois valeurs nues.
    """
    if not classes_colonnes:
        classes_colonnes = ("texte",) + ("nombre",) * (len(entetes) - 1)

    def cellule(balise: str, contenu: str, classe: str, portee: str = "") -> str:
        attributs = f' class="{classe}"' if classe else ""
        attributs += f' scope="{portee}"' if portee else ""
        return f"<{balise}{attributs}>{contenu}</{balise}>"

    tete = "".join(
        cellule("th", echapper(intitule), classes_colonnes[i], "col")
        for i, intitule in enumerate(entetes)
    )
    corps = ""
    for ligne in lignes:
        cellules = cellule("th", ligne[0], classes_colonnes[0], "row")
        cellules += "".join(
            cellule("td", valeur, classes_colonnes[i + 1])
            for i, valeur in enumerate(ligne[1:])
        )
        corps += f"<tr>{cellules}</tr>"
    return (f'<div class="defilant"><table>'
            f"<caption><span>{legende}</span></caption>"
            f"<thead><tr>{tete}</tr></thead><tbody>{corps}</tbody></table></div>")


def sections_depliables(elements: tuple[tuple[str, str], ...]) -> str:
    """Des sections repliées : le détail que peu liront, offert à tous.

    La première est ouverte — une page entièrement repliée ressemble à une page
    vide, et l'on n'ouvre pas ce dont on ne devine pas le contenu.
    """
    blocs = ""
    for i, (titre, corps) in enumerate(elements):
        ouverte = " open" if i == 0 else ""
        blocs += (f'<details class="section"{ouverte}><summary>{echapper(titre)}</summary>'
                  f'<div class="dedans">{corps}</div></details>')
    return blocs


# -- la typographie ----------------------------------------------------------
#
# Le français met une espace insécable devant « ; ! ? », devant « : », à
# l'intérieur des guillemets et entre un nombre et son unité. La poser à la
# main dans deux mille lignes de prose serait la poser presque partout : une
# seule oubliée, et une page s'ouvre sur « 6,8 » suivi, à la ligne, de « % du
# PIB ». Elle est donc posée ici, une fois, sur le HTML fini.
#
# La passe ne touche qu'au TEXTE : tout ce qui se trouve entre `<` et `>` est
# laissé tel quel, sans quoi une adresse « ...?page=2 » recevrait une espace au
# milieu et ne mènerait plus nulle part.

_FINE = "\u202f"   # espace fine insécable : avant ; ! ? et dans les guillemets
_INSEC = "\u00a0"  # espace insécable : avant les deux-points, après un nombre

_AVANT_PONCTUATION = re.compile(r" ([;!?])")
_AVANT_DEUX_POINTS = re.compile(r" (:)(\s|$)")
_APRES_GUILLEMET = re.compile(r"« ")
_AVANT_GUILLEMET = re.compile(r" »")
# Un nombre et ce qui le suit immédiatement : l'unité ne doit jamais tomber à
# la ligne seule. La liste est fermée — « 15 élèves » se lie, « 15 écoles de
# la ville » non, parce qu'une phrase entière ne se lie pas.
_UNITES = ("%", "€", "Md€", "M€", "points", "point", "heures", "élèves",
           "millions", "million", "ans", "an")
_NOMBRE_UNITE = re.compile(
    r"(\d) (" + "|".join(re.escape(u) for u in _UNITES) + r")(?![\w-])")


def typographie(document: str) -> str:
    """Pose les espaces insécables du français, hors des balises."""
    morceaux = re.split(r"(<[^>]*>)", document)
    for i, morceau in enumerate(morceaux):
        if morceau.startswith("<"):
            continue
        morceau = _AVANT_PONCTUATION.sub(_FINE + r"\1", morceau)
        morceau = _AVANT_DEUX_POINTS.sub(_INSEC + r"\1\2", morceau)
        morceau = _APRES_GUILLEMET.sub("«" + _FINE, morceau)
        morceau = _AVANT_GUILLEMET.sub(_FINE + "»", morceau)
        morceau = _NOMBRE_UNITE.sub(r"\1" + _INSEC + r"\2", morceau)
        morceaux[i] = morceau
    return "".join(morceaux)


def page(nom: str, corps: str) -> str:
    """La page entière : en-tête HTML, bandeau, contenu, pied."""
    titre = TITRES[nom]
    titre_complet = (titre if nom == "index"
                     else f"{titre} — École : le programme libéral")
    return typographie(f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- La couleur de la barre du navigateur sur un téléphone : celle de la page,
     pour que la page commence où elle commence. -->
<meta name="theme-color" content="#0b3d3a">
<title>{echapper(titre_complet)}</title>
<meta name="description" content="{echapper(DESCRIPTIONS[nom])}">
<link rel="icon" href="moteur/icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="moteur/icone.svg">
<!-- La feuille est extraite de src/education/gabarit.py par
     scripts/construire_site.py : elle n'existe qu'à un seul endroit. -->
<link rel="stylesheet" href="moteur/style.css">
<meta property="og:title" content="{echapper(titre_complet)}">
<meta property="og:description" content="{echapper(DESCRIPTIONS[nom])}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
</head>
<body>
{entete(nom)}
<main id="contenu">
{corps}
{pied()}
</main>
</body>
</html>
""")


# -- la feuille de style -----------------------------------------------------

STYLE = """/* Extrait de src/education/gabarit.py par scripts/construire_site.py —
   ne pas modifier ici.

   L'apparence est celle du simulateur de retraite du même parti
   (github.com/g-pliberal/retraitecomptenotionelle) : mêmes jetons, mêmes
   polices, même affiche. Deux outils du même parti doivent se reconnaître,
   et un électeur qui passe de l'un à l'autre ne doit pas croire avoir changé
   de site. Les variables de `:root` sont le seul point de contact : un hôte
   qui voudrait ajuster une couleur les redéfinit dans une feuille chargée
   après celle-ci, sans connaître ni un sélecteur, ni un fichier. */

/* Les deux polices, servies par le dépôt et non par un tiers : une requête de
   police chez un hébergeur emporte l'adresse IP du lecteur, et un site qui
   parle de l'école n'a pas à savoir qui le lit. Sous licence OFL, avec les
   deux sous-ensembles dont le français a besoin — `latin` pour l'essentiel,
   `latin-ext` pour les œ, les ÿ et les guillemets qu'il traîne.

   `font-display: swap` : le texte s'affiche tout de suite dans la pile du
   système, et se recompose quand la police arrive. */
@font-face {
  font-family: "Public Sans"; font-style: normal; font-weight: 100 900;
  font-display: swap; src: url(polices/public-sans-latin.woff2) format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA,
    U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}
@font-face {
  font-family: "Public Sans"; font-style: normal; font-weight: 100 900;
  font-display: swap; src: url(polices/public-sans-latin-ext.woff2) format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF,
    U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
    U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
@font-face {
  font-family: "Instrument Serif"; font-style: normal; font-weight: 400;
  font-display: swap; src: url(polices/instrument-serif-latin.woff2) format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA,
    U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193,
    U+2212, U+2215, U+FEFF, U+FFFD;
}
@font-face {
  font-family: "Instrument Serif"; font-style: normal; font-weight: 400;
  font-display: swap; src: url(polices/instrument-serif-latin-ext.woff2) format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF,
    U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
    U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}

:root {
  /* Un seul thème, et c'est voulu : l'affiche EST l'identité. `color-scheme`
     figé sur `dark` donne aussi aux champs et aux barres de défilement du
     navigateur le rendu sombre qui va avec. */
  color-scheme: dark;
  --fond: #0b3d3a;
  --fond-carte: #0f4a46;
  --fond-appui: #0f4a46;
  --fond-defilant: var(--fond);
  /* Le crème porte 12,9:1 sur le fond, et le crème atténué 7,1:1 : au-dessus
     du plancher de 4,5:1 même pour le petit texte. */
  --texte: #f4efe4;
  --texte-doux: #c3d8d4;
  /* Une troisième teinte, pour les légendes et les réserves — 5,4:1, réservée
     aux textes d'au moins 15 px. */
  --texte-tres-doux: #a7c3bf;
  --trait: #2f6360;
  /* Bordure des composants, distincte du filet décoratif : un contour qui dit
     où l'on peut agir doit atteindre 3:1 sur les deux fonds qu'il sépare
     (WCAG 2.1, 1.4.11). Celle-ci est mesurée : 4,12:1 sur le fond, 3,44:1 sur
     la carte. Le filet `--trait` plafonne à 1,76:1 — c'est voulu, il ne porte
     aucune information. */
  --trait-champ: #6fa09c;
  /* L'accent est l'or : 9,4:1 sur le fond, et du vert profond lisible dessus
     sur un bouton plein — le contraste inverse, 9,4:1 lui aussi. */
  --accent: #e9c53d;
  --or: #e9c53d;
  /* Le crème des panneaux qu'on doit lire de près. Une affiche entièrement
     sombre fatigue dès qu'il faut lire vingt lignes de suite ; le crème dit
     « ici, on entre dans le détail ». */
  --creme: #f4efe4;
  --sur-creme: #0b3d3a;
  --sur-creme-doux: #2a4a47;
  --sur-creme-accent: #0b6167;
  --creme-trait: #c9c2b4;
  --bandeau: #0b3d3a;
  --bandeau-texte: #f4efe4;
  /* Les deux systèmes comparés : ce qui existe, et ce qu'on propose. La
     proposition est en or, parce que c'est l'accent de l'affiche et la seule
     couleur que l'œil trouve en premier. C'est fait pour. Elles ne sont
     jamais seules à porter le sens — le mot est toujours écrit à côté. */
  --actuel: #76a2ff;
  --liberal: #e9c53d;
  --alerte: #f0b849;
  --manque: #e8807f;
  --reste: #8ac44a;
  /* La marge latérale, fluide : 18 px sur un téléphone, 40 px au large. Elle
     est ici parce que le bandeau, l'affiche, les repères et les engagements
     s'y alignent, et qu'ils doivent s'aligner au pixel. */
  --marge: clamp(1.125rem, 5vw, 2.5rem);
  /* La largeur de l'affiche. Le texte courant, lui, reste borné par `p` et
     `.chapeau` : une ligne de 80 rem ne se lit pas. */
  --largeur: 80rem;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--fond);
  color: var(--texte);
  font-family: "Public Sans", system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  /* En `rem` et non en pixels : une taille en pixels ignore la préférence de
     taille de police du navigateur, sur laquelle comptent ceux qui l'ont
     agrandie une fois pour toutes. */
  font-size: 1.0625rem;
  line-height: 1.6;
  overflow-x: hidden;
}
main { max-width: var(--largeur); margin: 0 auto; padding: 0 var(--marge); }
/* Lien d'évitement : premier élément parcouru au clavier, invisible tant
   qu'il n'a pas le focus. Il n'est pas caché par `display:none`, qui le
   sortirait de l'ordre de tabulation : il est remonté hors de l'écran. */
.evitement {
  position: absolute; left: 0.5rem; top: -4rem; z-index: 30;
  background: var(--or); color: var(--fond);
  border: 1px solid var(--or); border-radius: 0 0 4px 4px;
  padding: 0.5rem 0.9rem; font-size: 0.92rem; font-weight: 700;
  text-decoration: none; transition: top 0.15s;
}
.evitement:focus { top: 0; }

/* -- le bandeau -------------------------------------------------------------

   Une seule rangée : le nom du site à gauche, les neuf onglets à droite, sur
   le même vert que la page, fermée par un filet. Collé en haut, parce que les
   pages sont longues et qu'on change de page en cours de lecture. */
header.bandeau {
  border-bottom: 1px solid var(--trait);
  background: var(--fond);
  color: var(--bandeau-texte);
  padding: 0; margin-bottom: 0;
  position: sticky; top: 0; z-index: 20;
}
header.bandeau .interieur {
  max-width: var(--largeur); margin: 0 auto; padding: 0 var(--marge);
  display: flex; flex-wrap: wrap; gap: 0 1.5rem;
  align-items: stretch; justify-content: space-between;
}
/* Le nom, en capitales serrées, précédé du carré d'or : la marque de
   l'affiche, douze pixels de côté. Le carré est dessiné par le style et non
   écrit dans le HTML — aucune synthèse vocale n'a à l'annoncer. */
header.bandeau .nom {
  font-size: 0.8125rem; margin: 0; font-weight: 800;
  letter-spacing: 0.14em; text-transform: uppercase; line-height: 1.3;
  display: flex; align-items: center; min-height: 3.5rem; min-width: 0;
}
header.bandeau .nom a {
  color: inherit; text-decoration: none;
  display: inline-flex; align-items: center; gap: 0.75rem;
}
header.bandeau .nom a:hover span { color: var(--or); }
header.bandeau .nom a::before {
  content: ""; flex: none; width: 0.75rem; height: 0.75rem; background: var(--or);
}
nav .groupe { display: contents; }
/* L'étiquette de groupe : lue par les synthèses vocales, invisible à l'œil.
   `clip-path` plutôt que `display:none`, qui la retirerait aussi de l'arbre
   d'accessibilité — c'est-à-dire de la seule oreille qui l'entend. */
nav .etiquette {
  position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0;
  overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0;
}
nav .liens { display: contents; }
header.bandeau nav {
  display: flex; flex-wrap: wrap; align-items: stretch;
  margin-bottom: -1px; min-width: 0;
}
/* Un onglet : toute la hauteur de la barre — 56 px, bien plus que les 44 de
   la cible tactile (WCAG 2.5.8). L'ACTIF NE SE SIGNALE PAS QUE PAR LA
   COULEUR : un soulignement de 2 px ET `aria-current="page"`. Les règles sont
   ancrées sur `header.bandeau`, parce que le plan d'une page longue est un
   `<nav>` lui aussi. */
header.bandeau nav a {
  color: var(--texte-doux); text-decoration: none;
  font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; white-space: nowrap;
  display: inline-flex; align-items: center; min-height: 3.5rem;
  padding: 0 0.55rem;
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s;
}
header.bandeau nav a:hover {
  color: var(--bandeau-texte); border-bottom-color: var(--trait-champ);
}
header.bandeau nav a[aria-current="page"] {
  color: var(--bandeau-texte); border-bottom-color: var(--or);
}
@media (max-width: 60rem) {
  header.bandeau .interieur { padding-bottom: 0.25rem; }
  header.bandeau .nom { flex: 1 1 100%; min-height: 2.75rem; padding-top: 0.25rem; }
  header.bandeau nav { width: 100%; margin-left: -0.55rem; }
  header.bandeau nav a { min-height: 2.75rem; }
}

/* -- les titres -------------------------------------------------------------

   Le premier de chaque page est massif, en capitales, et serré : c'est une
   affiche. La mise en capitales est faite par le STYLE — le texte, lui, reste
   écrit normalement, pour les synthèses vocales et pour le copier-coller. */
h1, h2, h3, h4 {
  font-family: inherit; text-wrap: balance;
}
h1 {
  margin: 0; font-weight: 900; text-transform: uppercase;
  font-size: clamp(2.5rem, 7vw, 6.0625rem); line-height: 0.92;
  letter-spacing: -0.045em;
}
h2 {
  font-size: clamp(1.75rem, 4vw, 2.5rem); line-height: 1;
  margin: 3rem 0 1rem; font-weight: 900;
  letter-spacing: -0.03em; text-transform: uppercase;
}
h3 { font-size: 1.25rem; margin: 2rem 0 0.5rem; font-weight: 700;
     letter-spacing: -0.01em; }
h4 { letter-spacing: -0.01em; margin: 1.5rem 0 0.4rem; }
/* Le titre en serif : celui d'un encadré, d'un bloc qui parle plutôt qu'il
   n'assène. Il coexiste avec les capitales sans les concurrencer, parce qu'il
   ne joue pas dans la même famille. */
.serif {
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif;
  font-weight: 400; text-transform: none; letter-spacing: 0;
  line-height: 1.05;
}
p { margin: 0.7rem 0; max-width: 46rem; }
li { max-width: 44rem; }
a { color: var(--accent); }
a:hover { opacity: 0.85; }
/* Le sur-titre : trois mots en or au-dessus du titre. Il dit où l'on est, ce
   que le titre ne dit plus depuis qu'il est une phrase. */
.surtitre {
  margin: 0 0 1rem; font-size: 0.975rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--or);
  line-height: 1;
}
/* Le chapeau : la phrase sous le titre, en serif. C'est la seule chose que
   lira celui qui ne lit que deux lignes. */
.chapeau {
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif;
  font-size: clamp(1.1875rem, 2vw, 1.625rem); line-height: 1.45;
  color: var(--texte-doux); max-width: 51rem; margin: 1.5rem 0 0;
}
.affiche { padding: 3rem 0 2.5rem; }
.affiche .chapeau { font-size: clamp(1.25rem, 2.4vw, 1.875rem); }
/* Ce qui, dans une phrase, porte le message. En or ET en demi-gras : l'or
   seul disparaît pour une vision basse ou un daltonisme fort, et l'emphase
   avec lui. Deux signaux valent mieux qu'un. */
.cle-texte, strong.cle-texte { color: var(--or); font-weight: 600; }
.discret { color: var(--texte-tres-doux); font-size: 0.9rem; }

/* -- les blocs --------------------------------------------------------------*/
.carte {
  background: var(--fond-carte); border: 1px solid var(--trait);
  border-radius: 4px; padding: 1.25rem 1.4rem; margin: 1.5rem 0;
}
.note {
  border-left: 3px solid var(--or); background: var(--fond-carte);
  padding: 0.85rem 1.1rem; margin: 1.5rem 0; font-size: 0.95rem;
  border-radius: 0 4px 4px 0;
}
.note > :first-child { margin-top: 0; }
.note > :last-child { margin-bottom: 0; }
/* Le point de vigilance : la réserve que la page fait sur elle-même, sortie
   de la prose et marquée comme telle — c'est un gage de sérieux, pas une note
   de bas de page. */
.note.vigilance { border-left-color: var(--alerte); }
.note.resume { font-size: 1rem; }
.note.entree { font-size: 1rem; margin: 1.2rem 0; }
.badge {
  display: inline-block; font-size: 0.68rem; letter-spacing: 0.06em;
  text-transform: uppercase; font-weight: 700; line-height: 1.4;
  padding: 0.05em 0.45em; border-radius: 3px; vertical-align: 0.15em;
  border: 1px solid var(--trait-champ); color: var(--texte-doux);
  white-space: nowrap;
}
.badge.proposition { color: var(--or); border-color: var(--or); }
.badge.actuel { color: var(--actuel); border-color: var(--actuel); }
/* L'encadré d'or : un bloc qui se détache sans changer de fond. */
.encadre {
  border: 2px solid var(--or); padding: clamp(1.25rem, 4vw, 2rem);
  margin: 1.5rem 0;
}
.encadre > :first-child { margin-top: 0; }
.encadre > :last-child { margin-bottom: 0; }
/* Deux colonnes de même poids, qui se mettent l'une sous l'autre quand la
   place manque. */
.paire {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(23.75rem, 100%), 1fr));
  gap: clamp(1.75rem, 4vw, 3rem); margin: 3.5rem 0; align-items: start;
}
.paire > div > :first-child { margin-top: 0; }

/* -- le panneau crème -------------------------------------------------------

   Le seul endroit du site où le texte est sombre sur clair. Il faut donc y
   redéfinir les couleurs de tout ce qui peut s'y trouver — liens, boutons,
   filets —, sans quoi un lien d'or sur du crème tomberait à 1,7:1. */
.creme {
  background: var(--creme); color: var(--sur-creme);
  border-radius: 4px; padding: clamp(1.25rem, 4vw, 2rem);
  margin: 1.5rem 0;
}
.creme h2, .creme h3, .creme .surtitre { color: inherit; }
.creme .surtitre { color: var(--sur-creme-accent); }
.creme a { color: var(--sur-creme-accent); }
.creme .discret { color: var(--sur-creme-doux); }
.creme :focus-visible { outline-color: var(--sur-creme); }
.creme a.bouton { background: var(--sur-creme); color: var(--or);
                  border-color: var(--sur-creme); }
.creme table th, .creme table td { border-bottom-color: var(--creme-trait); }
.creme thead th { color: var(--sur-creme-doux); }
.creme > :first-child { margin-top: 0; }
.creme > :last-child { margin-bottom: 0; }

/* -- les engagements --------------------------------------------------------

   Le bloc que l'on photographie. Le filet de séparation est porté par les
   cartes et non par le fond du conteneur : un fond qui sert de trait laisse un
   rectangle vert vide dès qu'une rangée est incomplète. */
.engagements {
  margin: 4rem 0 0; background: var(--fond-carte);
  border-top: 4px solid var(--or);
}
.engagements .grille {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0; padding: 0.5rem clamp(1.25rem, 4vw, 2rem) 2.25rem;
  overflow: hidden;
}
.engagements .engagement {
  padding: 1.75rem 1.5rem 0 0; display: grid; gap: 1rem; align-content: start;
}
.engagements .engagement:nth-child(even) {
  padding: 1.75rem 1.5rem 0; box-shadow: -1px 0 0 var(--trait);
}
.engagements .rang {
  font-size: 0.9375rem; font-weight: 700; letter-spacing: 0.16em;
  color: var(--texte-doux); line-height: 1; margin: 0;
}
.engagements .chiffre {
  font-size: clamp(2rem, 6vw, 3.25rem); line-height: 0.95;
  font-weight: 900; letter-spacing: -0.05em; color: var(--or); margin: 0;
}
.engagements .promesse {
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif;
  font-size: 1.5625rem; line-height: 1.25; color: var(--texte);
  border-top: 1px solid var(--trait); padding-top: 1rem; margin: 0;
}
.engagements .detail {
  font-size: 1.125rem; line-height: 1.6; color: var(--texte-doux); margin: 0;
}
@media (max-width: 48rem) {
  .engagements .grille { grid-template-columns: 1fr; }
  .engagements .engagement:nth-child(even) { padding: 1.75rem 0 0 0;
                                             box-shadow: none; }
}

/* Les étapes d'une réforme : le rang se voit, parce qu'il y a un ordre. */
ol.gestes {
  margin: 1.5rem 0; padding: 0; list-style: none; display: grid; gap: 0;
  font-size: 1.125rem; line-height: 1.5; color: var(--texte-doux);
  border-top: 1px solid var(--trait);
}
ol.gestes > li {
  display: grid; grid-template-columns: 3rem 1fr; gap: 1.125rem;
  padding: 0.9rem 0; border-bottom: 1px solid var(--trait);
  align-items: baseline; max-width: none;
}
ol.gestes > li > .rang {
  font-size: 2.25rem; line-height: 0.85; font-weight: 900;
  letter-spacing: -0.05em; color: var(--or);
}
ol.gestes > li strong { color: var(--texte); font-weight: 700; }

.leviers { list-style: none; padding: 0; margin: 1rem 0; display: grid;
           gap: 0.75rem; }
.leviers > li { padding: 0.75rem 1rem; background: var(--fond-appui);
                border-left: 3px solid var(--trait); line-height: 1.5;
                max-width: 46rem; }
.leviers > li.oui { border-left-color: var(--reste); }
.leviers > li.non { border-left-color: var(--manque); }

/* -- les repères chiffrés ---------------------------------------------------

   Les trois chiffres d'ouverture d'une page : ce sont eux qu'on emporte si on
   ne lit rien d'autre. L'étiquette passe AU-DESSUS du nombre — on lit « ce que
   l'école coûte » puis « 197,1 Md€ », et non un nombre dont on cherche le
   sens. */
.fiches { display: grid;
          grid-template-columns: repeat(auto-fit, minmax(min(11rem, 100%), 1fr));
          gap: 1rem; }
.fiche .valeur { font-size: 1.25rem; font-variant-numeric: tabular-nums;
                 font-weight: 700; }
.fiche .etiquette { font-size: 0.85rem; color: var(--texte-doux); }
.fiche .precision { font-size: 0.85rem; color: var(--texte-doux); margin-top: 0.3rem; }
.fiches.reperes {
  gap: 0; margin: 2rem 0;
  grid-template-columns: repeat(auto-fit, minmax(min(13.75rem, 100%), 1fr));
  border-top: 1px solid var(--trait); border-bottom: 1px solid var(--trait);
  overflow: hidden;
}
.fiches.reperes .fiche {
  background: none; border: 0; border-radius: 0;
  padding: 1.25rem 1.25rem 1.25rem 0;
  box-shadow: 1px 0 0 var(--trait);
  display: flex; flex-direction: column;
}
.fiches.reperes .fiche .valeur {
  font-size: clamp(1.75rem, 4vw, 2.5rem); line-height: 1.05; font-weight: 900;
  letter-spacing: -0.04em; color: var(--or); order: 2;
}
.fiches.reperes .fiche .etiquette {
  order: 1; font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--texte-doux); margin-bottom: 0.4rem;
}
.fiches.reperes .fiche .precision { order: 3; margin-top: 0.4rem; }

/* Quelques idées, une par bloc, de même poids : c'est ce qui les distingue
   d'une liste, où la première l'emporte. */
.points { display: grid;
          grid-template-columns: repeat(auto-fit, minmax(min(20rem, 100%), 1fr));
          gap: 1.5rem; margin: 2rem 0; }
.points .point { border-top: 3px solid var(--or); padding: 1rem 0 0; }
.points .point > h3 {
  margin: 0 0 0.4rem; font-size: 1.25rem; font-weight: 900;
  letter-spacing: -0.02em; text-transform: uppercase;
}
.points .point > p { margin: 0; font-size: 1rem; color: var(--texte-doux); }

/* Une question, sa réponse, sa source. Encadrée pour se découper : une capture
   de ce bloc se comprend hors du site. */
section.cle {
  background: var(--fond-carte); border: 0; border-top: 3px solid var(--or);
  border-radius: 0; padding: 1.5rem clamp(1.25rem, 3vw, 1.75rem) 1.25rem;
  margin: 2.5rem 0;
}
section.cle > h3 {
  margin: 0; font-size: clamp(1.375rem, 3vw, 1.75rem); font-weight: 900;
  letter-spacing: -0.03em; text-transform: uppercase;
}
section.cle > .reponse {
  font-size: 1.1875rem; line-height: 1.5; max-width: 46rem;
  margin: 0.5rem 0 0.2rem; color: var(--texte-doux);
}
section.cle > .source {
  font-size: 0.875rem; color: var(--texte-tres-doux); margin: 0.2rem 0 0;
}

/* -- le plan d'une page longue ----------------------------------------------*/
.plan {
  background: var(--fond-carte); border-left: 3px solid var(--or);
  padding: 0.85rem 1.1rem; margin: 1.5rem 0; font-size: 0.95rem;
}
.plan .etiquette {
  margin: 0 0 0.35rem; font-size: 0.78rem; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--texte-doux); font-weight: 700;
}
.plan ol {
  margin: 0; padding: 0; list-style: none;
  display: flex; flex-wrap: wrap; gap: 0.25rem 1.1rem;
}
.plan li { max-width: none; }
.plan a {
  color: var(--texte); text-decoration: none;
  font-size: 0.875rem; font-weight: 700; letter-spacing: 0.04em;
  text-transform: uppercase;
  display: inline-flex; align-items: center; min-height: 2.75rem;
  padding: 0 0.7rem;
  border-bottom: 1px solid var(--trait-champ);
}
.plan a:hover { color: var(--or); border-bottom-color: var(--or); }

/* -- les tableaux -----------------------------------------------------------*/
.defilant {
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  /* Conteneur de requête : la légende se dimensionne sur la zone visible, et
     non sur le tableau qui la déborde. */
  container-type: inline-size;
  margin: 1.5rem 0;
  background:
    linear-gradient(to right, var(--fond-defilant) 30%, transparent) left center,
    linear-gradient(to left, var(--fond-defilant) 30%, transparent) right center,
    radial-gradient(farthest-side at 0 50%, rgba(0, 0, 0, 0.4), transparent) left center,
    radial-gradient(farthest-side at 100% 50%, rgba(0, 0, 0, 0.4), transparent) right center;
  background-repeat: no-repeat;
  background-size: 2.5rem 100%, 2.5rem 100%, 0.9rem 100%, 0.9rem 100%;
  background-attachment: local, local, scroll, scroll;
}
table { border-collapse: collapse; width: 100%; font-size: 1rem;
        min-width: 32rem; }
caption {
  caption-side: top; text-align: left; font-size: 0.9rem;
  color: var(--texte-doux); padding: 0 0 0.5rem;
}
caption > span {
  display: block; position: sticky; left: 0; width: 100cqw; box-sizing: border-box;
}
tbody th { font-weight: 700; }
th, td { text-align: right; padding: 0.7rem 0.6rem;
         border-bottom: 1px solid var(--trait); vertical-align: top; }
th:first-child, td:first-child { text-align: left; }
thead th {
  font-size: 0.875rem; color: var(--texte-doux); font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase;
  border-bottom: 2px solid var(--or);
}
tbody tr:last-child :is(th, td) { border-bottom: none; }
td.nombre, th.nombre { font-variant-numeric: tabular-nums; white-space: nowrap; }
/* Une colonne de PHRASES, et non de nombres : elle se lit alignée à gauche,
   comme tout texte, et il lui faut de la place. */
td.texte, th.texte { text-align: left; }
td.long, th.long { text-align: left; min-width: 18rem; white-space: normal; }

/* -- les sections repliées --------------------------------------------------*/
details.section { margin: 0; border-top: 1px solid var(--trait); }
details.section:last-of-type { border-bottom: 1px solid var(--trait); }
details.section > summary {
  color: var(--texte); font-size: 1.0625rem; font-weight: 700;
  padding: 0.85rem 0.2rem; cursor: pointer;
}
details.section > summary:hover { color: var(--or); }
details.section > .dedans { padding: 0 0 1.2rem 1.65rem; }
details.section > .dedans > :first-child { margin-top: 0; }

/* -- les boutons ------------------------------------------------------------

   Or plein, vert profond dessus, capitales, carré. Rien d'arrondi — une
   affiche n'arrondit pas ses angles. */
.actions { display: flex; flex-wrap: wrap; gap: 0.75rem 1.4rem;
           align-items: center; margin: 1.5rem 0 0; }
a.bouton {
  display: inline-flex; align-items: center; min-height: 3rem;
  text-decoration: none;
  color: var(--fond); background: var(--or);
  border: 2px solid var(--or); border-radius: 0;
  padding: 0.85rem 1.5rem; font-size: 1rem; font-weight: 900;
  letter-spacing: 0.02em; text-transform: uppercase;
}
a.bouton:hover { opacity: 0.88; }
a.bouton.second {
  background: transparent; color: var(--texte); border-color: var(--trait-champ);
  font-weight: 700; text-transform: none; letter-spacing: 0;
}
a.bouton.second:hover { border-color: var(--or); opacity: 1; }

/* Le contour de focus : trois pixels d'or, décalés de trois, sur fond sombre ;
   du vert profond dans les panneaux crème, où l'or se perdrait. */
:focus-visible {
  outline: 3px solid var(--or); outline-offset: 3px; border-radius: 0;
}

footer {
  width: calc(100% - 2 * var(--marge)); max-width: calc(var(--largeur) - 2 * var(--marge));
  margin: 4rem auto 0; padding: 1.5rem 0 5rem;
  border-top: 1px solid var(--trait);
  font-size: 0.9rem; color: var(--texte-tres-doux);
}
footer a { color: var(--or); }

/* Mouvement réduit : une animation qui ne s'arrête pas déclenche nausées et
   migraines chez qui y est sensible (WCAG 2.2.2 et 2.3.3). Le système le
   signale ; on l'écoute. */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Impression : qui imprime une page veut les arguments et les chiffres, en
   noir sur blanc — une affiche vert profond pleine page coûterait une
   cartouche pour ne rien dire de plus. Tout est reteinté par les variables :
   c'est le seul endroit où elles servent deux fois. */
@media print {
  :root {
    --fond: #fff; --fond-carte: #fff; --fond-appui: #fff;
    --texte: #000; --texte-doux: #333; --texte-tres-doux: #444;
    --trait: #999; --trait-champ: #666;
    --accent: #000; --or: #000; --creme: #fff; --sur-creme: #000;
    --sur-creme-doux: #333; --sur-creme-accent: #000; --creme-trait: #999;
  }
  header.bandeau nav, .evitement, .plan { display: none; }
  header.bandeau {
    background: #fff; color: #000; border-bottom: 1px solid #000;
    margin-bottom: 1rem; position: static;
  }
  body { background: #fff; color: #000; font-size: 11pt; overflow-x: visible; }
  /* Les capitales massives redeviennent des titres : à 97 px sur du papier, un
     titre mange le tiers de la première page. */
  h1 { font-size: 20pt; }
  h2 { font-size: 15pt; }
  .chapeau, .affiche .chapeau { font-size: 12pt; }
  .defilant { overflow: visible; background: none; }
  .carte, .note, table, section.cle, .encadre, .engagements .engagement {
    break-inside: avoid;
  }
  details.section > .dedans { display: block; }
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 0.85em; }
}
"""

ICONE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img"
     aria-label="École : le programme libéral">
  <!-- Le carré de la charte, et un livre ouvert posé sur la même grille de 24
       au même trait de 2 que l'icône du simulateur de retraite du parti. Un
       fichier, et non un emoji : un emoji n'a ni la même forme ni la même
       taille d'un système à l'autre, et se brouille en petit. -->
  <rect width="32" height="32" rx="7" fill="#0b3d3a"/>
  <g transform="translate(4 4)" fill="none" stroke="#e9c53d" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 6.5C10.5 5 8.5 4.5 6 4.5H3v13h3c2.5 0 4.5 0.5 6 2" />
    <path d="M12 6.5C13.5 5 15.5 4.5 18 4.5h3v13h-3c-2.5 0-4.5 0.5-6 2" />
    <path d="M12 6.5v13" />
  </g>
</svg>
"""
