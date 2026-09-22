"""Le chiffrage du programme : ce que chaque réforme coûte ou rapporte.

C'est le seul endroit du site qui calcule, et il obéit à trois règles.

1. **Les chiffres constatés ne sont pas recopiés** : ils sont lus au registre
   (`donnees.nombre`), si bien qu'un chiffre corrigé à la source corrige tous
   les calculs qui en dépendent.
2. **Ce qui n'est pas constaté est une hypothèse, et le dit.** Chaque
   hypothèse porte trois valeurs — favorable, centrale, défavorable au solde —
   et la raison de ces valeurs. Aucune n'est cachée dans une formule.
3. **Chaque poste affiche sa formule**, en toutes lettres, à côté de son
   résultat. Un lecteur qui conteste une hypothèse peut refaire le calcul
   avec la sienne.

Le point de comparaison est la situation actuelle, en régime de croisière :
l'année 2035, quand la baisse démographique annoncée par la DEPP sera
acquise. Les montants sont annuels, en euros courants des années de leurs
sources — le chiffrage ne revalorise rien, et le dit sur la page.

Le signe suit le solde des finances publiques : un poste positif est une
dépense de plus, un poste négatif une dépense de moins.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .donnees import nombre, valeur as v

SCENARIOS = ("favorable", "central", "defavorable")

# -- les hypothèses ----------------------------------------------------------


@dataclass(frozen=True)
class Hypothese:
    """Ce que le chiffrage suppose, faute de pouvoir le constater.

    Les trois valeurs sont rangées par leur effet sur le solde, non par leur
    grandeur : « favorable » est la valeur qui rend le programme le moins
    coûteux, quelle qu'elle soit.
    """

    cle: str
    libelle: str
    favorable: float
    central: float
    defavorable: float
    unite: str
    fondement: str

    def valeur(self, scenario: str) -> float:
        return {"favorable": self.favorable, "central": self.central,
                "defavorable": self.defavorable}[scenario]


HYPOTHESES: dict[str, Hypothese] = {h.cle: h for h in (
    Hypothese(
        "part_variable",
        "Part de la dépense de l'État qui suit le nombre d'élèves",
        0.9, 0.8, 0.7, "part",
        "Les salaires suivent les effectifs à mesure des départs en retraite "
        "et des fermetures de classes ; les écoles rurales, les "
        "administrations et une partie des postes, non. Personne ne ferme "
        "une classe de vingt élèves parce qu'elle n'en compte plus que dix-huit."),
    Hypothese(
        "charge_pension",
        "Part des cotisations de pension induites par la revalorisation",
        0.0, 0.5, 1.0, "part",
        "Nulle si la revalorisation passe par des primes, qui ne portent "
        "pas de pension de l'État ; entière si elle passe par la grille "
        "indiciaire. Le programme laisse l'établissement moduler la "
        "rémunération : la vérité sera entre les deux."),
    Hypothese(
        "part_ecart_comble",
        "Part de l'écart de salaire avec la moyenne de l'OCDE que la "
        "revalorisation comble",
        1.0, 1.0, 1.0, "part",
        "Ce n'est pas une hypothèse mais un engagement : ramener l'écart "
        "entre le salaire des enseignants et celui des autres diplômés du "
        "supérieur à la moyenne de l'OCDE. Il figure ici pour qu'on voie ce "
        "qu'il pèse."),
    Hypothese(
        "part_ecart_prive",
        "Part de l'écart de financement public entre privé sous contrat et "
        "public que l'alignement comble",
        1.0, 1.0, 1.0, "part",
        "Engagement du programme : « le même montant public par élève, quel "
        "que soit l'établissement ». Le chiffrage le prend au mot."),
    Hypothese(
        "majoration",
        "Majoration du montant versé pour un élève défavorisé",
        0.4, 0.4, 0.4, "part",
        "Engagement du programme (« + 40 % »)."),
    Hypothese(
        "part_defavorises",
        "Part des élèves ouvrant droit à la majoration sociale",
        0.15, 0.2, 0.25, "part",
        "L'éducation prioritaire scolarise environ un écolier et un "
        "collégien public sur cinq. Le seuil exact dépendra de l'indice "
        "retenu ; un quart des élèves est la borne haute usuelle."),
    Hypothese(
        "adhesion_hors_contrat",
        "Part des élèves du hors contrat dont l'établissement signe le "
        "contrat unique",
        0.3, 0.5, 0.8, "part",
        "Le contrat interdit la sélection et les frais de scolarité ; une "
        "partie du hors contrat existe précisément pour sélectionner ou pour "
        "enseigner autre chose que les programmes, et ne signera pas."),
    Hypothese(
        "ecoles_par_gestionnaire",
        "Écoles publiques par emploi administratif créé",
        8, 5, 3, "écoles",
        "Une école qui gère une dotation et recrute doit avoir un "
        "gestionnaire. Les écoles se regrouperont ; nous comptons un emploi "
        "pour cinq écoles, comme dans un petit collège."),
    Hypothese(
        "cout_agent",
        "Coût annuel d'un emploi administratif, hors pensions",
        45_000, 45_000, 45_000, "€",
        "Ordre de grandeur d'un agent administratif de catégorie B, charges "
        "comprises. Il sert à la fois aux emplois créés et aux emplois "
        "économisés, et ne varie donc pas d'un scénario à l'autre."),
    Hypothese(
        "part_rh_liberee",
        "Part des emplois de gestion des personnels libérés par la fin du "
        "mouvement national",
        0.3, 0.2, 0.1, "part",
        "Le recrutement par l'établissement supprime le mouvement au barème "
        "et la gestion des affectations ; il ne supprime ni la paie, ni les "
        "carrières, ni les concours."),
    Hypothese(
        "cout_evaluation",
        "Coût annuel d'évaluations nationales corrigées hors de "
        "l'établissement, et du calcul de la valeur ajoutée",
        50e6, 100e6, 200e6, "€",
        "Les évaluations exhaustives existent déjà ; il s'y ajoute une "
        "correction externe et une publication. Le budget actuel de toute "
        f"l'évaluation et de l'inspection est de {v('evaluation_controle')}."),
    Hypothese(
        "cout_affectation",
        "Coût annuel de la procédure publique d'affectation",
        10e6, 20e6, 50e6, "€",
        "Une procédure du type Affelnet existe déjà pour l'entrée au lycée ; "
        "il s'agit de l'étendre à l'entrée à l'école et au collège."),
    Hypothese(
        "mobilite",
        "Part des élèves qui changent d'établissement du fait du libre choix",
        0.02, 0.05, 0.1, "part",
        "Là où il y a le choix, la plupart des familles gardent "
        "l'établissement proche ; dans les zones rurales, il n'y a pas de "
        "choix du tout. Un élève sur vingt est une hypothèse moyenne."),
    Hypothese(
        "cout_transport",
        "Surcoût annuel de transport par élève qui change d'établissement",
        200, 400, 800, "€",
        "À la charge des régions et des départements. Le programme ne "
        "promet pas le transport : il faudra pourtant le payer, ou "
        "accepter que le choix reste réservé à ceux qui peuvent conduire "
        "leurs enfants."),
    Hypothese(
        "part_fixe",
        "Part du coût d'un élève qui reste à la charge de l'établissement "
        "qu'il quitte, le temps qu'il s'ajuste",
        0.1, 0.2, 0.3, "part",
        "Les murs, le chauffage, la direction ne partent pas avec l'élève. "
        "C'est l'effet que la Suède a découvert trop tard."),
    Hypothese(
        "cout_systeme",
        "Coût ponctuel du système d'information qui verse la dotation à "
        "l'élève",
        100e6, 200e6, 400e6, "€",
        "Ordre de grandeur des grands systèmes de paie et de gestion de "
        "l'État, dont l'histoire récente enseigne qu'ils coûtent plus que "
        "prévu."),
    Hypothese(
        "cout_formation",
        "Coût ponctuel de formation par établissement à la gestion autonome",
        2_000, 3_000, 5_000, "€",
        "Formation des directeurs et des chefs d'établissement au "
        "recrutement, au budget et à la publication des comptes."),
)}


# -- les quantités de base ---------------------------------------------------
#
# Ce qui se calcule directement à partir du registre, sans hypothèse.


def eleves() -> float:
    """Élèves du premier et du second degré, public et privé sous contrat."""
    return nombre("eleves_premier_degre") + nombre("eleves_second_degre")


def baisse_demographique() -> float:
    """La baisse d'effectifs attendue d'ici 2035, en part des effectifs."""
    return nombre("demographie") / eleves()


def maintien() -> float:
    """Ce qui reste des effectifs en 2035 : un moins la baisse."""
    return 1 - baisse_demographique()


def part_pensions() -> float:
    """La part des cotisations de pension dans les dépenses de personnel."""
    pensions = nombre("pensions_mission")
    return pensions / (pensions + nombre("t2_mission_hors_pensions"))


def eleves_prive() -> tuple[float, float]:
    """Élèves du privé sous contrat, premier et second degré."""
    return (nombre("eleves_premier_degre") * nombre("prive_premier_degre"),
            nombre("eleves_second_degre") * nombre("prive_second_degre"))


def hausse_salaire(ecart: str, ecart_ocde: str) -> float:
    """La hausse qui ramène un écart de salaire à la moyenne de l'OCDE.

    Un enseignant payé 26 % de moins qu'un autre diplômé gagne 0,74 de son
    salaire ; pour n'en gagner que 17 % de moins, soit 0,83, il lui faut
    0,83 / 0,74 − 1, soit 12,2 % de plus.
    """
    return (1 - nombre(ecart_ocde)) / (1 - nombre(ecart)) - 1


def financement_public_aligne() -> float:
    """Ce que coûterait chaque élève au niveau de financement du public."""
    return (nombre("eleves_premier_degre") * nombre("public_eleve_1d")
            + nombre("eleves_second_degre") * nombre("public_eleve_2d"))


# -- les postes --------------------------------------------------------------

Lecteur = Callable[[str], float]


@dataclass(frozen=True)
class Poste:
    """Une ligne du chiffrage : ce qui change, et ce que cela coûte.

    `calcul` reçoit un lecteur d'hypothèses (`h("mobilite")`) et rend un
    montant annuel en euros, avec le signe du solde public. `nature` range le
    poste : `charge` et `ressource` en régime de croisière, `transition` pour
    ce qui ne se paie que pendant la mise en place.
    """

    cle: str
    reforme: str
    intitule: str
    nature: str
    actuel: str
    programme: str
    formule: str
    calcul: Callable[[Lecteur], float]
    # Année par année, la part du montant de croisière effectivement due.
    montee: Callable[[int], float]


def _rampe(debut: int, fin: int) -> Callable[[int], float]:
    """Une montée en charge linéaire, de zéro avant `debut` à un en `fin`."""
    def part(annee: int) -> float:
        if annee < debut:
            return 0.0
        if annee >= fin:
            return 1.0
        return (annee - debut + 1) / (fin - debut + 1)
    return part


def _fenetre(debut: int, fin: int) -> Callable[[int], float]:
    """Un coût dû chaque année de `debut` à `fin`, et plus ensuite."""
    return lambda annee: 1.0 if debut <= annee <= fin else 0.0


def _revalorisation(h: Lecteur) -> float:
    hausse_1d = hausse_salaire("salaire_ecart_elementaire",
                               "salaire_ecart_elementaire_ocde")
    hausse_2d = hausse_salaire("salaire_ecart_college",
                               "salaire_ecart_college_ocde")
    prive_1d, prive_2d = eleves_prive()
    hausse_prive = (prive_1d * hausse_1d + prive_2d * hausse_2d) / (
        prive_1d + prive_2d)
    masse = (nombre("t2_p140") * hausse_1d + nombre("t2_p141") * hausse_2d
             + nombre("t2_p139") * hausse_prive)
    hors_pensions = masse * (1 - part_pensions())
    avec_pensions = hors_pensions + masse * part_pensions() * h("charge_pension")
    # En 2035, la masse salariale aura suivi la baisse des effectifs pour sa
    # part variable : c'est ce qui libère le dividende démographique, et
    # c'est sur cette masse réduite que porte la hausse.
    reste = 1 - baisse_demographique() * h("part_variable")
    return avec_pensions * reste * h("part_ecart_comble")


def _alignement_prive(h: Lecteur) -> float:
    prive_1d, prive_2d = eleves_prive()
    ecart = (prive_1d * (nombre("public_eleve_1d") - nombre("prive_eleve_1d"))
             + prive_2d * (nombre("public_eleve_2d")
                           - nombre("prive_eleve_2d")))
    return ecart * maintien() * h("part_ecart_prive")


def _ponderation(h: Lecteur) -> float:
    majoration = (financement_public_aligne() * maintien() * h("majoration")
                  * h("part_defavorises"))
    existant = (nombre("ep_cout") + nombre("ep_collectivites")) * maintien()
    return majoration - existant


def _hors_contrat(h: Lecteur) -> float:
    cout = (nombre("hors_contrat_1d") * nombre("public_eleve_1d")
            + nombre("hors_contrat_2d") * nombre("public_eleve_2d"))
    return cout * maintien() * h("adhesion_hors_contrat")


def _gestion_ecoles(h: Lecteur) -> float:
    return (nombre("ecoles_publiques") / h("ecoles_par_gestionnaire")
            * h("cout_agent"))


def _mouvement(h: Lecteur) -> float:
    return -nombre("p214_rh") * h("part_rh_liberee") * h("cout_agent")


def _transport(h: Lecteur) -> float:
    return eleves() * maintien() * h("mobilite") * h("cout_transport")


def _dividende(h: Lecteur) -> float:
    return -(nombre("budget_mission") * baisse_demographique()
             * h("part_variable"))


def _couts_echoues(h: Lecteur) -> float:
    cout_moyen = financement_public_aligne() / eleves()
    return eleves() * h("mobilite") * cout_moyen * h("part_fixe")


def _installation(h: Lecteur) -> float:
    etablissements = nombre("ecoles_publiques") + nombre("eple_publics")
    # Réparti sur les deux années où il est dû.
    return (h("cout_systeme") + etablissements * h("cout_formation")) / 2


def _pourcent(x: float) -> str:
    return "+" + f"{x * 100:.1f}".replace(".", ",") + " %"


_HAUSSE_1D = _pourcent(hausse_salaire("salaire_ecart_elementaire",
                                      "salaire_ecart_elementaire_ocde"))
_HAUSSE_2D = _pourcent(hausse_salaire("salaire_ecart_college",
                                      "salaire_ecart_college_ocde"))
_BAISSE = (f"{v('demographie').split(' ')[0]} {v('demographie').split(' ')[1]}"
           " sur " + f"{eleves() / 1e6:.2f}".replace(".", ",") + " millions")


# Le calendrier de la page « La proposition », rentrée 2027 comprise :
# année 1 = 2028 (transparence), année 2 = 2029 (autonomie), année 3 = 2030
# (affectation), année 4 = 2031 (contrat unique et pondération). La
# revalorisation et le dividende démographique courent en continu.
PREMIERE_ANNEE = 2028
CROISIERE = 2035

POSTES: tuple[Poste, ...] = (
    Poste("revalorisation", "6", "Revalorisation des enseignants",
          "charge",
          f"Un professeur des écoles gagne {v('salaire_ecart_elementaire')} "
          "de moins qu'un autre diplômé du supérieur ; la moyenne de l'OCDE "
          f"est de {v('salaire_ecart_elementaire_ocde')}.",
          "L'écart est ramené à la moyenne de l'OCDE, au collège comme à "
          "l'école, dans le public comme dans le privé sous contrat.",
          "Hausse de salaire qui ramène l'écart à la moyenne de l'OCDE ("
          + _HAUSSE_1D + " à l'école, " + _HAUSSE_2D + " au collège et au "
          "lycée) × dépenses de "
          "personnel des programmes 140, 141 et 139, hors pensions, plus la "
          "part retenue des cotisations de pension × part de la masse "
          "salariale maintenue en 2035.",
          _revalorisation, _rampe(PREMIERE_ANNEE, CROISIERE)),
    Poste("alignement_prive", "1", "Même financement public pour l'élève du "
          "privé sous contrat",
          "charge",
          f"Un élève du privé sous contrat reçoit {v('prive_eleve_1d')} "
          f"d'argent public à l'école contre {v('public_eleve_1d')} dans le "
          f"public, {v('prive_eleve_2d')} au collège et au lycée contre "
          f"{v('public_eleve_2d')} ; sa famille paie des frais de "
          "scolarité.",
          "Le même montant public par élève ; les frais de scolarité "
          "disparaissent.",
          "Écart de dépense publique par élève entre public et privé, au "
          "premier et au second degré × élèves du privé sous contrat × part "
          "des effectifs maintenue en 2035.",
          _alignement_prive, _rampe(2031, 2034)),
    Poste("ponderation", "2", "Majoration de 40 % pour l'élève défavorisé",
          "charge",
          "L'éducation prioritaire concentre des moyens sur des zones, "
          "surtout en réduisant la taille des classes.",
          "Chaque élève défavorisé, où qu'il soit scolarisé, apporte 40 % "
          "de plus ; l'éducation prioritaire actuelle est absorbée dans la "
          "majoration.",
          "40 % × part des élèves défavorisés × financement public de tous "
          "les élèves au niveau du public, moins ce que l'éducation "
          "prioritaire coûte déjà à l'État et aux collectivités — le tout "
          "aux effectifs de 2035.",
          _ponderation, _rampe(2031, 2034)),
    Poste("hors_contrat", "4", "Financement des écoles hors contrat qui "
          "signent le contrat unique",
          "charge",
          "Les élèves du hors contrat ne reçoivent aucun financement public ; "
          "leurs familles paient tout.",
          "Les établissements qui acceptent le contrat unique sont financés "
          "comme les autres.",
          "Élèves du hors contrat × dépense publique par élève du public × "
          "part des établissements qui signent × effectifs maintenus en "
          "2035.",
          _hors_contrat, _rampe(2031, 2034)),
    Poste("gestion_ecoles", "3", "Gestionnaires pour les écoles devenues "
          "autonomes",
          "charge",
          "Une école n'a ni budget propre, ni personnalité juridique, ni "
          "personne pour gérer une dotation.",
          "Les écoles se regroupent et reçoivent un gestionnaire pour gérer "
          "leur dotation et leurs recrutements.",
          "Écoles publiques ÷ écoles par emploi créé × coût d'un emploi "
          "administratif.",
          _gestion_ecoles, _rampe(2029, 2031)),
    Poste("evaluation", "5", "Évaluations corrigées hors de l'établissement "
          "et publiées en valeur ajoutée",
          "charge",
          "Des évaluations nationales existent, mais ne sont ni corrigées "
          "hors de l'établissement ni publiées école par école.",
          "Correction externe, calcul de la valeur ajoutée, publication.",
          "Hypothèse directe de coût annuel.",
          lambda h: h("cout_evaluation"), _rampe(PREMIERE_ANNEE,
                                                 PREMIERE_ANNEE)),
    Poste("affectation", "5", "Procédure publique d'affectation",
          "charge",
          "La carte scolaire affecte l'élève selon son adresse ; la "
          "dérogation est opaque.",
          "Les familles classent leurs vœux ; un algorithme public attribue "
          "les places.",
          "Hypothèse directe de coût annuel.",
          lambda h: h("cout_affectation"), _rampe(2030, 2030)),
    Poste("transport", "5", "Transport des élèves qui choisissent un "
          "établissement éloigné",
          "charge",
          "Le transport scolaire dessert l'établissement du secteur.",
          "Une partie des élèves choisit plus loin ; les régions et les "
          "départements paient le trajet.",
          "Élèves en 2035 × part qui change d'établissement × surcoût de "
          "transport par élève.",
          _transport, _rampe(2030, 2033)),
    Poste("mouvement", "3", "Fin du mouvement national au barème",
          "ressource",
          f"{v('p214_rh')} gèrent les personnels, dont le mouvement et les "
          "affectations au barème.",
          "L'établissement recrute ; une partie de ces emplois n'a plus "
          "d'objet.",
          "Emplois de gestion des personnels × part libérée × coût d'un "
          "emploi administratif.",
          _mouvement, _rampe(2030, 2033)),
    Poste("dividende", "6", "Dividende démographique",
          "ressource",
          "À dépense par élève constante, la baisse des effectifs réduit "
          "d'elle-même la dépense de l'État.",
          "La dépense ainsi libérée n'est pas rendue au budget : elle finance "
          "le programme.",
          "Crédits de la mission « Enseignement scolaire » hors pensions × "
          "baisse des effectifs d'ici 2035 (" + _BAISSE + ") × part de la "
          "dépense qui suit les effectifs.",
          _dividende, _rampe(2026, CROISIERE)),
    Poste("couts_echoues", "1", "Coûts fixes laissés par les élèves qui "
          "partent",
          "transition",
          "Sans objet : l'élève reste dans son secteur.",
          "L'établissement quitté garde un temps ses murs et son équipe, le "
          "temps de s'ajuster.",
          "Élèves × part qui change d'établissement × coût public moyen d'un "
          "élève × part de ce coût qui ne part pas avec lui. Dû chaque "
          "année de 2031 à 2034.",
          _couts_echoues, _fenetre(2031, 2034)),
    Poste("installation", "3", "Système d'information et formation des "
          "directions",
          "transition",
          "Sans objet.",
          "Un système qui verse la dotation à l'élève ; une formation à la "
          "gestion pour chaque direction d'école et d'établissement.",
          "Coût du système + établissements × coût de formation, réparti "
          "sur 2028 et 2029.",
          _installation, _fenetre(2028, 2029)),
)


# -- les résultats -----------------------------------------------------------


class _Lecteur:
    """Lit les hypothèses d'un scénario, et note celles qu'on a lues.

    La note sert au test qui refuse une hypothèse que plus aucun poste
    n'utilise — même règle que pour les chiffres du registre.
    """

    lues: set[str] = set()

    def __init__(self, scenario: str,
                 forcees: dict[str, float] | None = None) -> None:
        self.scenario = scenario
        self.forcees = forcees or {}

    def __call__(self, cle: str) -> float:
        _Lecteur.lues.add(cle)
        if cle in self.forcees:
            return self.forcees[cle]
        return HYPOTHESES[cle].valeur(self.scenario)


def montant(poste: Poste, scenario: str = "central",
            forcees: dict[str, float] | None = None) -> float:
    """Le montant annuel d'un poste en régime de croisière, en euros."""
    return poste.calcul(_Lecteur(scenario, forcees))


def poste(cle: str) -> Poste:
    """Un poste par sa clé ; une clé inconnue casse la construction."""
    return next(p for p in POSTES if p.cle == cle)


def postes(nature: str) -> tuple[Poste, ...]:
    return tuple(p for p in POSTES if p.nature == nature)


def total(nature: str, scenario: str = "central",
          forcees: dict[str, float] | None = None) -> float:
    return sum(montant(p, scenario, forcees) for p in postes(nature))


def solde(scenario: str = "central",
          forcees: dict[str, float] | None = None) -> float:
    """Le solde annuel en régime de croisière, hors coûts de transition.

    Positif : le programme coûte plus que la dépense d'aujourd'hui.
    """
    return (total("charge", scenario, forcees)
            + total("ressource", scenario, forcees))


def solde_tendanciel(scenario: str = "central") -> float:
    """Le solde comparé à la tendance, et non à la dépense d'aujourd'hui.

    Sans le programme, le dividende démographique serait une économie pour
    les finances publiques. Le programme le dépense : comparé à ce que
    l'État aurait dépensé sans lui, son coût est la somme de ses charges,
    moins les seules économies qu'il crée lui-même.
    """
    return solde(scenario) - montant(poste("dividende"), scenario)


def trajectoire(scenario: str = "central") -> list[tuple[int, float, float,
                                                        float, float]]:
    """Année par année : charges, ressources, transition, solde.

    Chaque poste est pris à son montant de croisière, pondéré par sa montée
    en charge. C'est une approximation : les effectifs des années
    intermédiaires sont ceux de 2035, ce qui sous-estime légèrement les
    charges des premières années.
    """
    lignes = []
    for annee in range(PREMIERE_ANNEE, CROISIERE + 1):
        parts = {nature: sum(montant(p, scenario) * p.montee(annee)
                             for p in postes(nature))
                 for nature in ("charge", "ressource", "transition")}
        lignes.append((annee, parts["charge"], parts["ressource"],
                       parts["transition"], sum(parts.values())))
    return lignes


def sensibilite() -> list[tuple[Hypothese, float, float]]:
    """Ce que chaque hypothèse, seule, fait au solde.

    Pour chacune, le solde de croisière quand on la pousse à sa valeur
    favorable puis défavorable, toutes les autres restant centrales. Rangé
    de la plus influente à la moins influente.
    """
    lignes = []
    for h in HYPOTHESES.values():
        favorable = solde(forcees={h.cle: h.favorable})
        defavorable = solde(forcees={h.cle: h.defavorable})
        # Les engagements n'ont qu'une valeur ; les hypothèses de transition
        # ne touchent pas le solde de croisière. Ni les uns ni les autres
        # n'ont de place dans ce classement.
        if abs(defavorable - favorable) < 1e6:
            continue
        lignes.append((h, favorable, defavorable))
    lignes.sort(key=lambda ligne: ligne[2] - ligne[1], reverse=True)
    return lignes


def leviers_equilibre() -> list[tuple[str, str, float]]:
    """Ce que rapporterait, seul, chaque renoncement possible.

    Chaque ligne : ce à quoi l'on renonce, qui le paie, et de combien le
    solde de croisière baisse. Aucune ne suffit seule — c'est le sens du
    tableau.
    """
    central = solde()
    ponderation = poste("ponderation")
    options = (
        ("Aligner le financement du privé sous contrat à moitié seulement",
         "Les familles du privé, qui garderaient une partie de leurs frais "
         "de scolarité.",
         central - solde(forcees={"part_ecart_prive": 0.5})),
        ("Ne combler que la moitié de l'écart de salaire avec l'OCDE",
         "Les enseignants.",
         central - solde(forcees={"part_ecart_comble": 0.5})),
        ("Financer la majoration sociale en prenant sur les autres élèves",
         "Les établissements qui accueillent peu d'élèves défavorisés, "
         "dont le montant par élève baisserait de "
         + pourcent(-montant(ponderation) / (base_par_eleve() * (
             1 - HYPOTHESES["part_defavorises"].central))) + ".",
         montant(ponderation)),
        ("Ramener la majoration de 40 % à 20 %",
         "Les élèves défavorisés.",
         central - solde(forcees={"majoration": 0.2})),
    )
    return [(quoi, qui, gain) for quoi, qui, gain in options]


def base_par_eleve() -> float:
    """Le financement public de tous les élèves au niveau du public, en 2035.

    C'est l'assiette sur laquelle il faudrait prendre si le programme devait
    tenir à dépense constante : la part du solde qu'elle représente est la
    baisse du montant par élève qu'il faudrait imposer à tous.
    """
    return financement_public_aligne() * maintien()


# -- l'écriture des montants -------------------------------------------------

MOINS = "−"


def euros(valeur: float, signe: bool = False) -> str:
    """Un montant en Md€ ou M€, arrondi à ce que le calcul permet de dire.

    Au-dessus du milliard, une décimale ; en dessous, la dizaine de
    millions. Un chiffrage fait d'hypothèses n'a pas de chiffre significatif
    au-delà.
    """
    absolu = abs(valeur)
    if absolu >= 1e9:
        texte = f"{absolu / 1e9:.1f}".replace(".", ",") + " Md€"
    else:
        texte = f"{round(absolu / 1e7) * 10:.0f} M€"
    if texte in ("0 M€", "0,0 Md€"):
        return "0 M€"
    if valeur < 0:
        return MOINS + texte
    return ("+" if signe else "") + texte


def pourcent(valeur: float, signe: bool = False) -> str:
    texte = f"{abs(valeur) * 100:.1f}".replace(".", ",").replace(",0", "")
    prefixe = MOINS if valeur < 0 else ("+" if signe else "")
    return f"{prefixe}{texte} %"


def hypothese_texte(h: Hypothese, scenario: str) -> str:
    """Une valeur d'hypothèse telle qu'elle s'écrit dans le tableau."""
    x = h.valeur(scenario)
    if h.unite == "part":
        return pourcent(x)
    if h.unite == "€":
        if x >= 1e6:
            return euros(x)
        return f"{x:,.0f}".replace(",", " ") + " €"
    return f"{x:g} {h.unite}"
