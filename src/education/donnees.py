"""Les chiffres du site, et d'où ils viennent.

Un seul endroit. Une page qui cite « 197,1 Md€ » ne l'écrit pas : elle
demande `CHIFFRES["die_montant"]`, qui porte la valeur, l'année, la source et
son adresse. La page « Sources » est construite à partir de ce même registre,
si bien qu'aucun chiffre du site ne peut y manquer — et qu'un chiffre retiré
d'une page reste visible ici tant qu'on ne l'a pas retiré du registre.

Deux tests tiennent la promesse (`tests/test_site.py`) : aucun chiffre du
registre ne peut rester inutilisé, et chacun doit apparaître sur la page
« Sources » avec son année et son émetteur. Une promesse de méthode qui n'est
pas vérifiée n'est qu'un paragraphe.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chiffre:
    """Un chiffre publiable : sa valeur, ce qu'elle mesure, et sa provenance.

    `texte` est la forme telle qu'elle s'écrit dans une phrase — espaces
    insécables comprises. Le registre n'en calcule aucune : les sources
    publient des agrégats, pas des séries, et reformater à la volée un nombre
    qu'on n'a pas recalculé soi-même donne l'illusion d'un modèle là où il
    n'y a qu'une citation. Le seul calcul du site est le chiffrage du
    programme (`chiffrage.py`), qui lit ces chiffres par `nombre()` et
    affiche chacune de ses formules.
    """

    cle: str
    texte: str
    libelle: str
    annee: str
    source: str
    url: str
    precision: str = ""
    themes: tuple[str, ...] = field(default_factory=tuple)


def _c(cle: str, texte: str, libelle: str, annee: str, source: str, url: str,
       precision: str = "", themes: tuple[str, ...] = ()) -> Chiffre:
    return Chiffre(cle, texte, libelle, annee, source, url, precision, themes)


# Les adresses des sources, nommées une fois : une source citée par douze
# chiffres ne doit pas pouvoir pourrir en douze endroits.
DEPP_DIE = ("https://www.education.gouv.fr/sites/default/files/2025-09/"
            "depp-ni-2025-52-442155.pdf")
DEPP_CHIFFRES = ("https://www.education.gouv.fr/depp/"
                 "l-education-nationale-en-chiffres-edition-2026-505326")
DEPP_PISA = ("https://www.education.gouv.fr/depp/"
             "pisa-2022-culture-scientifique-comprehension-de-l-ecrit-et-vie-de-l-eleve-380208")
DEPP_TIMSS = ("https://www.education.gouv.fr/"
              "timss-2023-en-cm1-les-resultats-en-mathematiques-et-en-sciences-restent-"
              "stables-en-france-sous-la-415946")
DEPP_PIRLS = ("https://www.education.gouv.fr/depp/"
              "pirls-2021-la-france-stabilise-ses-resultats-contrairement-aux-autres-"
              "pays-europeens-majoritairement-452301")
DEPP_JDC = ("https://www.education.gouv.fr/depp/"
            "journee-defense-et-citoyennete-2024-un-jeune-francais-sur-vingt-en-"
            "situation-d-illettrisme-469313")
OCDE_RSE = ("https://www.oecd.org/content/dam/oecd/fr/publications/reports/2025/09/"
            "education-at-a-glance-2025-country-notes_9749f4ff/france_0639c7fb/"
            "aca6dceb-fr.pdf")
OCDE_AUTONOMIE = "https://www.oecd.org/en/topics/sub-issues/school-autonomy.html"
COUR_PRIVE = ("https://www.ccomptes.fr/sites/default/files/2023-10/"
              "20230601-enseignement-prive-sous-contrat.pdf")
CAE_EDUCATION = "https://cae-eco.fr/static/pdf/cae084-education-250514.pdf"
DEPP_DEMOGRAPHIE = ("https://www.education.gouv.fr/"
                    "demographie-scolaire-le-ministere-publie-pour-la-premiere-fois-des-"
                    "projections-d-effectifs-d-eleves-504392")
VIE_IDEES_DEDOUBLEMENT = "https://laviedesidees.fr/Le-dedoublement-des-classes-de-CP-et-CE1-quel-bilan"
IFAU_SUEDE = ("https://www.ifau.se/globalassets/pdf/se/2015/"
              "wp2015-08-School-choice-and-segregation.pdf")
GRONDWET = "https://wetten.overheid.nl/BWBR0001840/"
IGESR_GROUPES = ("https://www.ih2ef.gouv.fr/mise-en-place-des-groupes-de-"
                 "besoins-en-francais-et-mathematiques-rapport-de-ligesr")
DECRET_GROUPES = "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053652587"
PAP_2026 = ("https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/"
            "1087978/file/PAP2026_BG_Enseignement_scolaire_EC.pdf")
SENAT_NP_2026 = ("https://www.senat.fr/fileadmin/Commissions/Finances/2025-2026/"
                 "PLF_2026/NP/Enseignement_scolaire_NP_PLF_2026.pdf")
SENAT_EP = "https://www.senat.fr/rap/r24-575/r24-575_mono.html"
AN_PRIVE = ("https://www.assemblee-nationale.fr/dyn/16/rapports/cion-cedu/"
            "l16b2423_rapport-information.pdf")
RERS_2026_CH1 = ("https://www.education.gouv.fr/sites/default/files/document/"
                 "1-le-systeme-educatifpdf-519276.pdf")
RERS_2025_CH2 = ("https://www.education.gouv.fr/sites/default/files/2025-07/"
                 "rers2025-chapitre-2-441717.pdf")
DEPP_PISA_2025 = ("https://www.education.gouv.fr/sites/default/files/document/"
                  "depp-ni-2026-40pisa-mathspdf-520231.pdf")
DEPP_PISA_2025_SCIENCES = ("https://www.education.gouv.fr/sites/default/files/"
                           "document/depp-ni-2026-39pisa-sciencespdf-520225.pdf")
OCDE_PISA_2025_FRANCE = ("https://www.oecd.org/content/dam/oecd/fr/publications/"
                         "reports/2026/09/pisa-2025-results-volume-i-country-"
                         "notes_88d1164e/france_69779694/9840dc6b-fr.pdf")
OCDE_PISA_2025_PAYSBAS = ("https://www.oecd.org/content/dam/oecd/en/publications/"
                          "reports/2026/09/pisa-2025-results-volume-i-country-"
                          "notes_88d1164e/netherlands_e5cbc486/1c998a42-en.pdf")
OCDE_DECENTRALISATION = ("https://www.oecd.org/content/dam/oecd/fr/publications/"
                         "reports/2018/11/how-decentralised-are-education-systems-"
                         "and-what-does-it-mean-for-schools_7c1806fc/"
                         "b3b6fcc4-fr.pdf")
PAYSBAS_ADMISSION = ("https://www.government.nl/themes/education/"
                     "freedom-of-education/public-authority-and-private-schools")
TALLINN_CONCOURS = "https://tik.edu.ee/p/1637-nelja-kooli-uhiskatsed-joint-tests"
DEPP_IVAC = ("https://www.education.gouv.fr/sites/default/files/document/"
             "Depp_Guide_m%C3%A9thodologique_IVAC_2025.pdf-515492.pdf")
FACK_GRENET_CARTE = ("https://archives-statistiques-depp.education.gouv.fr/"
                     "Default/doc/SYRACUSE/13199/les-effets-de-l-assouplissement-"
                     "de-la-carte-scolaire-dans-l-education-prioritaire")
INSEE_PRIX_2025 = "https://www.insee.fr/fr/statistiques/8726461"
POSTES_2025 = ("https://www.franceinfo.fr/societe/education/francois-bayrou-"
               "confirme-qu-il-n-y-aura-pas-suppression-de-4-000-postes-d-"
               "enseignants-une-decision-definitive_7040645.html")


CHIFFRES: dict[str, Chiffre] = {c.cle: c for c in (

    # -- ce que l'école coûte -------------------------------------------------
    _c("die_montant", "197,1 Md€",
       "Dépense intérieure d'éducation : tout ce que la France consacre à son "
       "système éducatif, du préélémentaire au supérieur, tous financeurs "
       "confondus.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE,
       "En hausse de 2,8 Md€ en euros constants sur un an (+1,4 %).",
       ("depense",)),
    _c("die_pib", "6,8 % du PIB",
       "Part de la richesse nationale consacrée à l'éducation.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE,
       "", ("depense",)),
    _c("die_par_eleve", "10 920 €",
       "Dépense moyenne par élève ou étudiant, apprentissage compris.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_premier_degre", "9 080 €",
       "Dépense moyenne par écolier (premier degré).",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_college", "10 450 €",
       "Dépense moyenne par collégien.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_lycee_general", "13 020 €",
       "Dépense moyenne par lycéen de l'enseignement général et technologique.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_lycee_pro", "14 700 €",
       "Dépense moyenne par lycéen de l'enseignement professionnel.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_universite", "12 460 €",
       "Dépense moyenne par étudiant à l'université.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_cpge", "19 070 €",
       "Dépense moyenne par élève de classe préparatoire aux grandes écoles.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE,
       "À comparer aux 9 080 € de l'écolier : l'écart est de un à deux.",
       ("depense",)),
    _c("die_etat", "55 %",
       "Part de l'État dans le financement de la dépense d'éducation.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE,
       "Devant les collectivités (23 %), les entreprises (10 %) et les "
       "ménages (8 %).",
       ("depense",)),
    _c("die_collectivites", "23 %",
       "Part des collectivités territoriales dans le financement.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_menages", "8 %",
       "Part des ménages dans le financement de la dépense d'éducation.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("budget_mission", "64,5 Md€",
       "Crédits de la mission « Enseignement scolaire » hors pensions.",
       "2026", "Projet de loi de finances pour 2026",
       "https://www.budget.gouv.fr/", "", ("depense",)),
    _c("budget_mission_pensions", "89,6 Md€",
       "Crédits de la mission « Enseignement scolaire », compte d'affectation "
       "spéciale « Pensions » compris.",
       "2026", "Projet de loi de finances pour 2026",
       "https://www.budget.gouv.fr/",
       "Premier budget de l'État par le montant.", ("depense",)),
    _c("ocde_pib_comparable", "5,4 % du PIB",
       "Part du PIB consacrée aux établissements d'enseignement, de "
       "l'élémentaire au supérieur, sur le périmètre retenu par l'OCDE — "
       "plus étroit que la dépense intérieure d'éducation française.",
       "2022", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Supérieur à la moyenne de l'OCDE (4,7 %). La DIE française y ajoute "
       "notamment les cantines, les transports scolaires et la formation "
       "continue : les deux chiffres ne se comparent pas.", ("depense",)),
    _c("ocde_pib_comparable_ocde", "4,7 %",
       "La même part, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C1.2", OCDE_RSE,
       "", ("depense",)),
    _c("part_publique", "92 %",
       "Part des pouvoirs publics dans le financement de l'enseignement, de "
       "l'élémentaire au post-secondaire non supérieur.",
       "2022", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 90,1 %. Les familles françaises financent donc une "
       "part de l'école un peu plus faible qu'ailleurs.", ("depense",)),
    _c("part_publique_ocde", "90,1 %",
       "La même part, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "",
       ("depense",)),
    _c("services_annexes", "12,2 %",
       "Part des services annexes — transports scolaires, internats, "
       "cantines, médecine scolaire — dans la dépense d'éducation en France.",
       "2025", "Grenet et Landais, notes du CAE n° 84, mai 2025 (données "
       "OCDE)", CAE_EDUCATION,
       "Moyenne OCDE : 5,6 %. C'est l'une des raisons, avec la diversité des "
       "filières et des options, du coût élevé du second degré.",
       ("depense",)),
    _c("services_annexes_ocde", "5,6 %",
       "La même part, en moyenne dans l'OCDE.",
       "2025", "Grenet et Landais, notes du CAE n° 84, mai 2025 (données "
       "OCDE)", CAE_EDUCATION, "", ("depense",)),
    _c("ocde_elementaire_fr", "11 135 USD",
       "Dépense annuelle par élève dans l'enseignement élémentaire en "
       "France, en équivalents USD à parité de pouvoir d'achat.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C3.1", OCDE_RSE,
       "Soit 13 % de moins que la moyenne de l'OCDE.", ("depense",)),
    _c("ocde_elementaire_ocde", "12 730 USD",
       "La même dépense, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C3.1", OCDE_RSE,
       "", ("depense",)),
    _c("ocde_college_fr", "13 622 USD",
       "Dépense annuelle par élève dans le premier cycle du secondaire "
       "(collège) en France.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "Soit 5 % de moins que la moyenne de l'OCDE.", ("depense",)),
    _c("ocde_college_ocde", "14 315 USD",
       "La même dépense, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "", ("depense",)),
    _c("ocde_lycee_fr", "18 127 USD",
       "Dépense annuelle par élève dans le second cycle du secondaire "
       "(lycée) en France.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "Soit 24 % de plus que la moyenne de l'OCDE : c'est le seul niveau où "
       "la France dépense nettement plus que ses voisins.", ("depense",)),
    _c("ocde_lycee_ocde", "14 562 USD",
       "La même dépense, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "", ("depense",)),
    _c("dedoublement_cout", "800 M€ par an",
       "Coût annuel du dédoublement des classes de grande section, de CP et "
       "de CE1 en éducation prioritaire, pour 16 000 équivalents temps plein.",
       "2024", "Sénat, rapport d'information n° 575 (2024-2025) sur "
       "l'éducation prioritaire", SENAT_EP,
       "Chiffre de la Cour des comptes. Effets mesurés par la DEPP : "
       "positifs en CP, surtout en mathématiques ; au CE1, la progression "
       "ne se distingue plus de celle d'élèves comparables.",
       ("depense", "reformes")),

    _c("die_hausse", "+1,4 %",
       "Hausse de la dépense intérieure d'éducation sur un an, en euros "
       "constants.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE,
       "Soit 2,8 Md€.", ("depense",)),
    _c("die_entreprises", "10 %",
       "Part des entreprises dans le financement de la dépense d'éducation.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("die_autres_apu", "4 %",
       "Part des autres administrations publiques dans le financement.",
       "2024", "DEPP, note d'information n° 25.52", DEPP_DIE, "", ("depense",)),
    _c("ocde_ecart_elementaire", "13 % de moins",
       "Écart entre la dépense française par élève de l'élémentaire et la "
       "moyenne de l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C3.1", OCDE_RSE,
       "", ("depense",)),
    _c("ocde_ecart_college", "5 % de moins",
       "Le même écart pour le premier cycle du secondaire.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "", ("depense",)),
    _c("ocde_ecart_lycee", "24 % de plus",
       "Le même écart pour le second cycle du secondaire.",
       "2022", "OCDE, Regards sur l'éducation 2025, tableau C4.1", OCDE_RSE,
       "Seul niveau où la France dépense nettement plus que la moyenne.",
       ("depense",)),
    _c("dedoublement_etp", "16 000",
       "Équivalents temps plein mobilisés par le dédoublement des classes de "
       "grande section, de CP et de CE1 en éducation prioritaire.",
       "2024", "Sénat, rapport d'information n° 575 (2024-2025) sur "
       "l'éducation prioritaire", SENAT_EP, "Chiffre de la Cour des comptes.",
       ("depense",)),

    # -- ce que l'école produit -----------------------------------------------
    _c("pisa_maths", "458 points",
       "Score moyen des élèves français de 15 ans en mathématiques (PISA).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 463 points, un écart qui n'est pas significatif. "
       "Selon l'OCDE, les résultats de 2025 comptent parmi les plus faibles "
       "jamais obtenus par la France dans cette enquête.", ("resultats",)),
    _c("pisa_maths_ocde", "463 points",
       "Moyenne OCDE en mathématiques (PISA).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_maths_chute", "−16 points",
       "Recul du score français en mathématiques entre PISA 2022 et PISA 2025.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Après 21 points de recul entre 2018 et 2022 ; le score était stable "
       "de 2006 à 2018.", ("resultats",)),
    _c("pisa_maths_chute_ocde", "−9 points",
       "Recul de la moyenne de l'OCDE en mathématiques entre PISA 2022 et "
       "PISA 2025.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_maths_chute_2022", "−21 points",
       "Recul du score français en mathématiques entre PISA 2018 et PISA 2022.",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "La plus forte baisse enregistrée par la France dans cette enquête "
       "jusqu'alors.", ("resultats",)),
    _c("pisa_lecture", "456 points",
       "Score moyen en compréhension de l'écrit (PISA).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 461 points, un écart qui n'est pas significatif.",
       ("resultats",)),
    _c("pisa_sciences", "483 points",
       "Score moyen en culture scientifique, domaine principal de l'enquête "
       "2025 (PISA).",
       "2025", "DEPP, note d'information n° 26.39", DEPP_PISA_2025_SCIENCES,
       "Moyenne OCDE : 482 points. Stable depuis 2022 ; 495 points en 2015.",
       ("resultats",)),
    _c("pisa_faibles", "36 %",
       "Part des élèves français de 15 ans sous le niveau 2 en mathématiques : "
       "ils ne savent pas reconnaître, sans consigne, comment une situation "
       "simple se traduit en mathématiques.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 35 %. Ils étaient 29 % en 2022 et 21 % en 2018.",
       ("resultats",)),
    _c("pisa_faibles_ocde", "35 %",
       "La même part, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_faibles_2022", "29 %",
       "La même part en France lors de l'enquête précédente.",
       "2022", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_faibles_lecture", "33 %",
       "Part des élèves français de 15 ans sous le niveau 2 en compréhension "
       "de l'écrit.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 30 %. Ils étaient 27 % en 2022, 21 % en 2018 et 15 % "
       "en 2000.", ("resultats",)),
    _c("pisa_faibles_lecture_ocde", "30 %",
       "La même part, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_faibles_lecture_2000", "15 %",
       "La même part en France lors de la première enquête PISA.",
       "2000", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_tres_bons", "5 %",
       "Part des élèves français de 15 ans très performants en mathématiques "
       "(au-dessus du niveau 4).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 8 %. Ils étaient 15 % en 2003.", ("resultats",)),
    _c("pisa_tres_bons_ocde", "8 %",
       "La même part, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_tres_bons_2003", "15 %",
       "La même part en France en 2003, première enquête centrée sur les "
       "mathématiques.",
       "2003", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_ecart_social", "95 points",
       "Écart de score en mathématiques entre les élèves français très "
       "favorisés et très défavorisés (PISA).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 83 points. La France est l'un des pays de l'OCDE où "
       "cet écart est le plus marqué.", ("resultats", "inegalites")),
    _c("pisa_ecart_social_ocde", "83 points",
       "Le même écart, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_ecart_lecture", "91 points",
       "Le même écart en compréhension de l'écrit.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Moyenne OCDE : 77 points.", ("resultats",)),
    _c("pisa_ecart_lecture_ocde", "77 points",
       "Le même écart en compréhension de l'écrit, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_ecart_sciences", "100 points",
       "Écart de score en culture scientifique entre les 25 % d'élèves "
       "français les plus favorisés et les 25 % les plus défavorisés.",
       "2025", "DEPP, note d'information n° 26.39", DEPP_PISA_2025_SCIENCES,
       "Moyenne OCDE : 85 points.", ("resultats",)),
    _c("pisa_ecart_sciences_ocde", "85 points",
       "Le même écart en culture scientifique, en moyenne dans l'OCDE.",
       "2025", "DEPP, note d'information n° 26.39", DEPP_PISA_2025_SCIENCES,
       "", ("resultats",)),
    _c("timss_cm1_maths", "484 points",
       "Score moyen des élèves français de CM1 en mathématiques (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS,
       "Moyenne de l'Union européenne : 524 points. La France est au dernier "
       "rang des pays de l'Union européenne ayant participé à l'enquête — "
       "une quinzaine d'États membres y participent.", ("resultats",)),
    _c("timss_cm1_maths_ue", "524 points",
       "Moyenne de l'Union européenne en mathématiques en CM1 (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS, "", ("resultats",)),
    _c("timss_cm1_sciences", "488 points",
       "Score moyen des élèves français de CM1 en sciences (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS,
       "Moyenne de l'Union européenne : 518 points.", ("resultats",)),
    _c("timss_quatrieme_maths", "479 points",
       "Score moyen des élèves français de quatrième en mathématiques (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS,
       "Moyenne des pays de l'Union européenne et de l'OCDE participants : "
       "507 points.", ("resultats",)),
    _c("timss_cm1_seuil", "15 %",
       "Part des élèves français de CM1 qui n'atteignent pas le niveau "
       "élémentaire en mathématiques (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS, "", ("resultats",)),
    _c("pirls", "514 points",
       "Score moyen des élèves français de CM1 en compréhension de l'écrit "
       "(PIRLS).",
       "2021", "IEA / DEPP", DEPP_PIRLS,
       "Moyenne européenne : 527 points. Le score français est stable après "
       "quinze ans de baisse.", ("resultats",)),
    _c("jdc_difficultes", "13 %",
       "Part des jeunes Français de 16 à 25 ans en difficulté de lecture, "
       "mesurée à la Journée défense et citoyenneté.",
       "2024", "DEPP, Journée défense et citoyenneté", DEPP_JDC,
       "Sur 843 500 jeunes testés.", ("resultats",)),
    _c("jdc_illettrisme", "6 %",
       "Part des jeunes considérés en situation d'illettrisme à la Journée "
       "défense et citoyenneté.",
       "2024", "DEPP, Journée défense et citoyenneté", DEPP_JDC,
       "Un jeune sur vingt, après au moins dix ans d'école obligatoire.",
       ("resultats",)),

    _c("pisa_faibles_2018", "21 %",
       "Part des élèves français de 15 ans sous le niveau 2 en mathématiques "
       "lors de l'enquête de 2018.",
       "2018", "OCDE / DEPP", DEPP_PISA,
       "Ils sont 36 % en 2025 : quinze points de plus en sept ans.",
       ("resultats",)),
    _c("pisa_lecture_ocde", "461 points",
       "Moyenne OCDE en compréhension de l'écrit (PISA).",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_lecture_chute", "−18 points",
       "Recul du score français en compréhension de l'écrit entre PISA 2022 "
       "et PISA 2025.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025,
       "Après 19 points de recul entre 2018 et 2022.", ("resultats",)),
    _c("pisa_lecture_chute_ocde", "−14 points",
       "Recul de la moyenne de l'OCDE en compréhension de l'écrit entre PISA "
       "2022 et PISA 2025.",
       "2025", "DEPP, note d'information n° 26.40", DEPP_PISA_2025, "",
       ("resultats",)),
    _c("pisa_sciences_ocde", "482 points",
       "Moyenne OCDE en culture scientifique (PISA).",
       "2025", "DEPP, note d'information n° 26.39", DEPP_PISA_2025_SCIENCES,
       "", ("resultats",)),
    _c("timss_cm1_sciences_ue", "518 points",
       "Moyenne de l'Union européenne en sciences en CM1 (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS, "", ("resultats",)),
    _c("timss_quatrieme_maths_ue", "507 points",
       "Moyenne des pays de l'Union européenne et de l'OCDE participants, en "
       "mathématiques en quatrième (TIMSS).",
       "2023", "IEA / DEPP", DEPP_TIMSS, "", ("resultats",)),
    _c("pirls_ue", "527 points",
       "Moyenne européenne en compréhension de l'écrit en CM1 (PIRLS).",
       "2021", "IEA / DEPP", DEPP_PIRLS, "", ("resultats",)),
    _c("jdc_testes", "843 500",
       "Jeunes testés à la Journée défense et citoyenneté, soit presque une "
       "classe d'âge entière.",
       "2024", "DEPP, Journée défense et citoyenneté", DEPP_JDC, "",
       ("resultats",)),

    # -- ce que l'école emploie -----------------------------------------------
    _c("eleves_premier_degre", "6,15 millions",
       "Élèves du premier degré, public et privé sous contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "Dont 86,4 % dans le secteur public.", ("moyens",)),
    _c("eleves_second_degre", "5,62 millions",
       "Élèves du second degré, public et privé sous contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "Dont 78,8 % dans le secteur public.", ("moyens",)),
    _c("enseignants_public", "711 600",
       "Enseignants du secteur public.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("moyens",)),
    _c("enseignants_prive", "139 900",
       "Enseignants du privé sous contrat, rémunérés par l'État.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("moyens",)),
    _c("demographie", "1,7 million d'élèves en moins",
       "Baisse attendue des effectifs scolaires d'ici 2035.",
       "2026", "DEPP, projections démographiques", DEPP_DEMOGRAPHIE,
       "À dépense constante, c'est un desserrement massif — ou une économie "
       "silencieuse.", ("moyens",)),
    _c("salaire_ecart_elementaire", "26 %",
       "Écart entre le salaire effectif d'un professeur des écoles français et "
       "celui d'un actif diplômé du supérieur travaillant à temps plein.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 17 %.", ("moyens", "enseignants")),
    _c("salaire_ecart_college", "18 %",
       "Le même écart pour un enseignant de collège.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 13 %.", ("moyens", "enseignants")),
    _c("heures_elementaire", "864 heures",
       "Heures d'enseignement obligatoire par an dans l'élémentaire en France.",
       "2025", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 804 heures. La France enseigne plus longtemps, sur "
       "moins de jours.", ("moyens",)),
    _c("heures_college", "973 heures",
       "Heures d'enseignement obligatoire par an au collège en France.",
       "2025", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 909 heures.", ("moyens",)),
    _c("taille_classe", "21,6 élèves",
       "Taille moyenne d'une classe élémentaire en France.",
       "2023", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 21 élèves. En baisse de près de deux élèves depuis "
       "2013.", ("moyens",)),
    _c("taille_classe_college", "25,6 élèves",
       "Taille moyenne d'une classe de collège en France.",
       "2023", "Grenet et Landais, notes du CAE n° 84, mai 2025", CAE_EDUCATION,
       "Moyenne des autres pays de l'Union européenne : 20,7 élèves.",
       ("moyens",)),
    _c("taille_classe_college_ue", "20,7 élèves",
       "La même taille, en moyenne dans les autres pays de l'Union "
       "européenne.",
       "2023", "Grenet et Landais, notes du CAE n° 84, mai 2025", CAE_EDUCATION,
       "", ("moyens",)),
    _c("fondamentaux", "59 %",
       "Part du temps d'instruction obligatoire de l'élémentaire consacrée à "
       "la lecture, à l'écriture, à la littérature et aux mathématiques en "
       "France.",
       "2025", "OCDE, Regards sur l'éducation 2025, tableaux D1.3 et D1.4",
       OCDE_RSE,
       "38 % pour la lecture, l'écriture et la littérature, 21 % pour les "
       "mathématiques. Moyenne OCDE : 41 %.", ("moyens",)),
    _c("fondamentaux_ocde", "41 %",
       "La même part, en moyenne dans l'OCDE.",
       "2025", "OCDE, Regards sur l'éducation 2025, tableaux D1.3 et D1.4",
       OCDE_RSE, "", ("moyens",)),
    _c("salaire_debut_hausse", "8 %",
       "Hausse des salaires statutaires de début de carrière des enseignants "
       "français entre 2015 et 2024.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 17 % dans l'élémentaire. Au bout de quinze ans de "
       "carrière, le salaire statutaire d'un professeur des écoles n'a pas "
       "augmenté sur la période.", ("moyens", "enseignants")),
    _c("salaire_debut_hausse_ocde", "17 %",
       "La même hausse dans l'élémentaire, en moyenne dans l'OCDE.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "",
       ("moyens", "enseignants")),
    _c("postes_2025", "4 000 postes",
       "Suppressions de postes d'enseignants prévues au projet de loi de "
       "finances pour 2025, auxquelles le gouvernement a renoncé.",
       "2025", "franceinfo, 28 janvier 2025", POSTES_2025,
       "Le Premier ministre a présenté ce renoncement comme une « décision "
       "définitive ».", ("moyens",)),

    _c("salaire_ecart_elementaire_ocde", "17 %",
       "Écart moyen, dans l'OCDE, entre le salaire d'un enseignant du "
       "primaire et celui des autres diplômés du supérieur.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "",
       ("moyens", "enseignants")),
    _c("salaire_ecart_college_ocde", "13 %",
       "Le même écart moyen dans l'OCDE, au collège.",
       "2024", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "",
       ("moyens", "enseignants")),
    _c("heures_elementaire_ocde", "804 heures",
       "Heures d'enseignement obligatoire par an dans l'élémentaire, en "
       "moyenne dans l'OCDE.",
       "2025", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "", ("moyens",)),
    _c("heures_college_ocde", "909 heures",
       "Heures d'enseignement obligatoire par an au collège, en moyenne dans "
       "l'OCDE.",
       "2025", "OCDE, Regards sur l'éducation 2025", OCDE_RSE, "", ("moyens",)),

    # -- qui décide -----------------------------------------------------------
    _c("decisions_central", "55 %",
       "Part des décisions prises au niveau de l'État central dans le premier "
       "cycle du secondaire public français.",
       "2018", "OCDE, autonomie des établissements", OCDE_AUTONOMIE,
       "Moyenne OCDE : 24 %.", ("gouvernance",)),
    _c("decisions_central_ocde", "24 %",
       "La même part, en moyenne dans l'OCDE.",
       "2018", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "", ("gouvernance",)),
    _c("decisions_etablissement", "10 %",
       "Part des décisions prises au niveau de l'établissement en France.",
       "2018", "OCDE, autonomie des établissements", OCDE_AUTONOMIE,
       "Dont 2 % seulement en pleine autonomie ; le reste s'exerce dans un "
       "cadre fixé plus haut.", ("gouvernance",)),
    _c("recrutement_france", "10 %",
       "Part des élèves français dont le chef d'établissement a la "
       "responsabilité principale du recrutement des enseignants.",
       "2022", "OCDE, autonomie des établissements", OCDE_AUTONOMIE,
       "Moyenne OCDE : 60 %. Estonie : 94 %. Royaume-Uni : 81 %. "
       "Pays-Bas : 64 %.", ("gouvernance",)),
    _c("recrutement_ocde", "60 %",
       "La même part, en moyenne dans l'OCDE.",
       "2022", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "", ("gouvernance",)),
    _c("prive_premier_degre", "13,6 %",
       "Part des élèves du premier degré scolarisés dans le privé sous "
       "contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("gouvernance", "liberte")),
    _c("prive_second_degre", "21,2 %",
       "Part des élèves du second degré scolarisés dans le privé sous contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("gouvernance", "liberte")),
    _c("prive_catholique", "97 %",
       "Part des établissements privés sous contrat relevant de "
       "l'enseignement catholique.",
       "2023", "Cour des comptes", COUR_PRIVE,
       "La « liberté de choix » française est donc, en pratique, le choix "
       "entre l'école publique de son quartier et une école confessionnelle.",
       ("gouvernance", "liberte")),
    _c("prive_tres_favorises", "40,2 %",
       "Part des élèves issus de familles très favorisées dans l'enseignement "
       "privé sous contrat.",
       "2021", "Cour des comptes", COUR_PRIVE,
       "Elle était de 26,4 % en 2000. Les élèves de familles favorisées et "
       "très favorisées y sont désormais majoritaires.",
       ("gouvernance", "liberte")),
    _c("prive_tres_favorises_2000", "26,4 %",
       "La même part en 2000.",
       "2000", "Cour des comptes", COUR_PRIVE, "", ("gouvernance", "liberte")),

    _c("decisions_pleine_autonomie", "2 %",
       "Part des décisions prises en pleine autonomie par l'établissement en "
       "France ; le reste des décisions locales s'exerce dans un cadre fixé "
       "plus haut.",
       "2018", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "",
       ("gouvernance",)),
    _c("recrutement_paysbas", "64 %",
       "Part des élèves néerlandais dont le chef d'établissement recrute "
       "les enseignants.",
       "2022", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "",
       ("gouvernance",)),
    _c("recrutement_royaume_uni", "81 %",
       "La même part au Royaume-Uni.",
       "2022", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "",
       ("gouvernance",)),

    # -- ailleurs -------------------------------------------------------------
    _c("danemark_financement", "environ 75 %",
       "Part du coût d'une école libre danoise prise en charge par l'État ; "
       "le reste est à la charge des familles, avec des barèmes sociaux.",
       "2024", "Réseau Canopé, fiche Danemark",
       "https://www.reseau-canope.fr/fileadmin/user_upload/Projets/"
       "Ecoles-deurope/Focus8_Danemark.pdf", "", ("comparaisons",)),
    _c("danemark_prive", "15 à 16 %",
       "Part des élèves danois scolarisés dans une école libre (friskole) ou "
       "privée.",
       "2024", "Réseau Canopé, fiche Danemark",
       "https://www.reseau-canope.fr/fileadmin/user_upload/Projets/"
       "Ecoles-deurope/Focus8_Danemark.pdf",
       "L'État finance environ 75 % du coût ; le reste est à la charge des "
       "familles, avec des barèmes sociaux.", ("comparaisons",)),
    _c("paysbas_article23", "1917",
       "Année où les Pays-Bas ont inscrit dans leur Constitution le "
       "financement égal des écoles publiques et privées (article 23).",
       "1917", "Constitution néerlandaise, article 23", GRONDWET,
       "Plus d'un siècle de liberté scolaire financée, dans un pays qui n'a "
       "pas cessé d'être un État social.", ("comparaisons",)),
    _c("estonie_pisa", "510 points",
       "Score de l'Estonie en mathématiques (PISA 2022) : troisième rang des "
       "pays de l'OCDE derrière le Japon et la Corée, au niveau de la "
       "Suisse.",
       "2022", "OCDE, PISA 2022",
       "https://www.oecd.org/en/about/programmes/pisa.html",
       "Deux points devant la Suisse (508) : l'écart est inférieur à la "
       "marge d'erreur de l'enquête, et nous ne le présentons donc pas "
       "comme un classement. La dépense estonienne par élève est inférieure "
       "à la française.",
       ("comparaisons",)),
    _c("estonie_sciences", "527 points",
       "Score de l'Estonie en culture scientifique (PISA 2025) : le deuxième "
       "de l'OCDE, derrière le Japon.",
       "2025", "DEPP, note d'information n° 26.39", DEPP_PISA_2025_SCIENCES,
       "", ("comparaisons",)),
    _c("paysbas_ecart_sciences", "105 points",
       "Écart de score en culture scientifique entre les 25 % d'élèves "
       "néerlandais les plus favorisés et les 25 % les plus défavorisés "
       "(PISA 2025).",
       "2025", "OCDE, Résultats du PISA 2025, volume I, note pays : "
       "Pays-Bas", OCDE_PISA_2025_PAYSBAS,
       "Moyenne OCDE : 85 points ; France : 100 points.", ("comparaisons",)),
    _c("estonie_recrutement", "94 %",
       "Part des élèves estoniens dont le chef d'établissement recrute "
       "lui-même les enseignants.",
       "2022", "OCDE, autonomie des établissements", OCDE_AUTONOMIE, "", ("comparaisons",)),
    _c("suede_reforme", "1992",
       "Année de la réforme suédoise des friskolor : financement public à "
       "l'élève, ouvert aux établissements privés à but lucratif.",
       "1992", "IFAU, School choice and segregation (2015)", IFAU_SUEDE,
       "Le contre-exemple dont ce programme tire ses garde-fous. La "
       "ségrégation scolaire suédoise a augmenté ; la part qu'en explique le "
       "libre choix est, selon l'IFAU, modeste au regard de la ségrégation "
       "résidentielle.", ("comparaisons",)),

    # -- ce que le programme coûterait ----------------------------------------
    #
    # Les chiffres dont part le chiffrage (`chiffrage.py`). Ils sont cités, pas
    # calculés : le calcul, lui, est fait à partir d'eux, et affiché avec sa
    # formule sur la page « Chiffrage ».
    _c("t2_p140", "27,85 Md€",
       "Dépenses de personnel (titre 2) du programme « Enseignement scolaire "
       "public du premier degré », cotisations de pension comprises.",
       "2026", "Projet annuel de performances « Enseignement scolaire », "
       "PLF 2026", PAP_2026, "", ("chiffrage",)),
    _c("t2_p141", "39,65 Md€",
       "Dépenses de personnel du programme « Enseignement scolaire public du "
       "second degré », cotisations de pension comprises.",
       "2026", "Projet annuel de performances « Enseignement scolaire », "
       "PLF 2026", PAP_2026,
       "Comprend quelques personnels non enseignants (conseillers principaux "
       "d'éducation, professeurs documentalistes).", ("chiffrage",)),
    _c("t2_p139", "7,97 Md€",
       "Dépenses de personnel du programme « Enseignement privé du premier "
       "et du second degrés », cotisations de pension comprises.",
       "2026", "Projet annuel de performances « Enseignement scolaire », "
       "PLF 2026", PAP_2026, "", ("chiffrage",)),
    _c("t2_mission_hors_pensions", "59,23 Md€",
       "Dépenses de personnel de la mission « Enseignement scolaire », hors "
       "cotisations de pension.",
       "2026", "Sénat, commission des finances, note de présentation du "
       "PLF 2026, mission « Enseignement scolaire »", SENAT_NP_2026,
       "94 % des crédits de la mission hors pensions.", ("chiffrage",)),
    _c("pensions_mission", "25,16 Md€",
       "Cotisations au compte d'affectation spéciale « Pensions » de la "
       "mission « Enseignement scolaire ».",
       "2026", "Sénat, commission des finances, note de présentation du "
       "PLF 2026, mission « Enseignement scolaire »", SENAT_NP_2026,
       "Écart entre les crédits pensions comprises (89,6 Md€) et hors "
       "pensions (64,5 Md€).", ("chiffrage",)),
    _c("mesures_salariales", "6,44 Md€",
       "Coût en 2026 de l'ensemble des mesures salariales décidées pour les "
       "personnels de l'éducation nationale depuis 2022 (revalorisation "
       "« socle », points d'indice).",
       "2026", "Sénat, commission des finances, note de présentation du "
       "PLF 2026, mission « Enseignement scolaire »", SENAT_NP_2026,
       "", ("chiffrage",)),
    _c("public_eleve_1d", "7 331 €",
       "Dépense publique (État et collectivités) par élève du premier degré "
       "dans l'enseignement public.",
       "2021", "Assemblée nationale, rapport d'information n° 2423 sur le "
       "financement public de l'enseignement privé sous contrat", AN_PRIVE,
       "Chiffre de la direction des affaires financières du ministère.",
       ("chiffrage",)),
    _c("prive_eleve_1d", "3 285 €",
       "La même dépense publique par élève du premier degré dans le privé "
       "sous contrat.",
       "2021", "Assemblée nationale, rapport d'information n° 2423 sur le "
       "financement public de l'enseignement privé sous contrat", AN_PRIVE,
       "L'écart tient notamment à l'absence de financement public de "
       "l'investissement et à une structure d'emplois moins coûteuse.",
       ("chiffrage",)),
    _c("public_eleve_2d", "10 339 €",
       "Dépense publique (État et collectivités) par élève du second degré "
       "dans l'enseignement public.",
       "2021", "Assemblée nationale, rapport d'information n° 2423 sur le "
       "financement public de l'enseignement privé sous contrat", AN_PRIVE,
       "", ("chiffrage",)),
    _c("prive_eleve_2d", "5 662 €",
       "La même dépense publique par élève du second degré dans le privé "
       "sous contrat.",
       "2021", "Assemblée nationale, rapport d'information n° 2423 sur le "
       "financement public de l'enseignement privé sous contrat", AN_PRIVE,
       "", ("chiffrage",)),
    _c("prive_frais_familles", "3,3 Md€",
       "Contributions versées par les familles aux établissements privés "
       "sous contrat.",
       "2022", "Assemblée nationale, rapport d'information n° 2423 sur le "
       "financement public de l'enseignement privé sous contrat", AN_PRIVE,
       "Chiffre de la DEPP. La Cour des comptes relevait 2,8 Md€ en 2020.",
       ("chiffrage",)),
    _c("hors_contrat_1d", "59 800",
       "Élèves du premier degré scolarisés dans une école privée hors "
       "contrat.",
       "2025", "DEPP, Repères et références statistiques 2026, fiche 1.02",
       RERS_2026_CH1, "", ("chiffrage",)),
    _c("hors_contrat_2d", "24 800",
       "Élèves de moins de seize ans du second degré scolarisés dans un "
       "établissement privé hors contrat.",
       "2025", "DEPP, Repères et références statistiques 2026, fiche 1.02",
       RERS_2026_CH1, "", ("chiffrage",)),
    _c("ecoles_publiques", "42 396",
       "Écoles publiques du premier degré.",
       "2025", "DEPP, Repères et références statistiques 2026, fiche 1.09",
       RERS_2026_CH1,
       "Une école n'a pas de personnalité juridique : son directeur n'a ni "
       "budget ni autorité sur ses collègues.", ("chiffrage",)),
    _c("eple_publics", "7 821",
       "Collèges et lycées publics de l'éducation nationale.",
       "2025", "DEPP, Repères et références statistiques 2026, fiche 1.09",
       RERS_2026_CH1, "", ("chiffrage",)),
    _c("ep_cout", "2,6 Md€",
       "Coût pour l'État de l'éducation prioritaire (REP et REP+), dont 83 % "
       "au titre de la réduction de la taille des classes.",
       "2023", "Sénat, rapport d'information n° 575 (2024-2025) sur "
       "l'éducation prioritaire", SENAT_EP,
       "Chiffre de la Cour des comptes, en hausse de 86 % depuis 2016.",
       ("chiffrage",)),
    _c("ep_collectivites", "environ 1 Md€",
       "Dépense des collectivités territoriales au titre de l'éducation "
       "prioritaire.",
       "2023", "Sénat, rapport d'information n° 575 (2024-2025) sur "
       "l'éducation prioritaire", SENAT_EP, "Estimation.", ("chiffrage",)),
    _c("ep_eleves", "1,68 million",
       "Élèves des écoles et collèges publics classés en REP ou REP+, soit "
       "environ un sur cinq.",
       "2024", "DEPP, Repères et références statistiques 2025, fiche 2.18",
       RERS_2025_CH2,
       "Somme des quatre effectifs publiés : écoles et collèges, REP et REP+.",
       ("chiffrage",)),
    _c("aesh_credits", "3,16 Md€",
       "Crédits consacrés aux accompagnants d'élèves en situation de "
       "handicap (AESH).",
       "2026", "Sénat, commission des finances, note de présentation du "
       "PLF 2026, mission « Enseignement scolaire »", SENAT_NP_2026,
       "Pour près de 140 000 accompagnants.", ("chiffrage",)),
    _c("p214_rh", "11 248,5 ETPT",
       "Emplois du programme « Soutien de la politique de l'éducation "
       "nationale » consacrés à la gestion des ressources humaines.",
       "2026", "Projet annuel de performances « Enseignement scolaire », "
       "PLF 2026", PAP_2026,
       "Sur 28 974 emplois du programme.", ("chiffrage",)),
    _c("evaluation_controle", "101,4 M€",
       "Crédits de l'action « Évaluation et contrôle » : inspection "
       "générale, DEPP, services statistiques académiques.",
       "2026", "Projet annuel de performances « Enseignement scolaire », "
       "PLF 2026", PAP_2026, "", ("chiffrage",)),
    _c("groupes_postes", "2 800 postes",
       "Emplois d'enseignants mobilisés pour les groupes de besoins en "
       "sixième et cinquième.",
       "2025", "Sénat, commission des finances, note de présentation du "
       "PLF 2026, mission « Enseignement scolaire »", SENAT_NP_2026,
       "", ("chiffrage",)),
    _c("inflation_2022", "5,2 %",
       "Hausse des prix à la consommation en 2022, en moyenne annuelle.",
       "2022", "Insee, Informations rapides n° 8, 15 janvier 2026",
       INSEE_PRIX_2025, "", ("chiffrage",)),
    _c("inflation_2023", "4,9 %",
       "Hausse des prix à la consommation en 2023, en moyenne annuelle.",
       "2023", "Insee, Informations rapides n° 8, 15 janvier 2026",
       INSEE_PRIX_2025, "", ("chiffrage",)),
    _c("inflation_2024", "2,0 %",
       "Hausse des prix à la consommation en 2024, en moyenne annuelle.",
       "2024", "Insee, Informations rapides n° 8, 15 janvier 2026",
       INSEE_PRIX_2025, "", ("chiffrage",)),
    _c("inflation_2025", "0,9 %",
       "Hausse des prix à la consommation en 2025, en moyenne annuelle.",
       "2025", "Insee, Informations rapides n° 8, 15 janvier 2026",
       INSEE_PRIX_2025, "", ("chiffrage",)),
)}


@dataclass(frozen=True)
class Fait:
    """Une affirmation datée, et le document qui l'établit.

    Le registre des chiffres discipline les nombres ; il ne disciplinait pas
    les faits. Or une page peut parfaitement citer tous ses chiffres et
    affirmer dans la même phrase qu'un rapport conclut ceci ou qu'un décret
    a fait cela, sans que le lecteur puisse le vérifier. Ces affirmations-là
    sont les plus faciles à contester, et les plus coûteuses à défendre après
    coup.

    `enonce` est ce que le site affirme, en une phrase, telle qu'elle est
    vérifiable dans le document cité — pas telle qu'elle arrange la page.
    """

    cle: str
    enonce: str
    annee: str
    source: str
    url: str


FAITS: dict[str, Fait] = {f.cle: f for f in (
    Fait("igesr_groupes",
         "L'inspection générale conclut que les groupes de besoins n'ont pas "
         "bénéficié aux élèves les plus fragiles, que la mobilité entre "
         "groupes est restée faible, et que le dispositif risque de creuser "
         "les écarts en isolant les élèves en difficulté ; elle recommande "
         "d'abandonner son caractère systématique et de rendre aux "
         "établissements une autonomie réelle.",
         "2025", "IGÉSR, rapport n° 24-25-007C, juin 2025", IGESR_GROUPES),
    Fait("decret_groupes",
         "Le décret n° 2026-172 du 10 mars 2026 met fin au caractère "
         "obligatoire des groupes en sixième et cinquième et le remplace par "
         "un « accompagnement pédagogique renforcé » en français et en "
         "mathématiques, applicable à la rentrée 2026.",
         "2026", "Décret n° 2026-172 du 10 mars 2026", DECRET_GROUPES),
    Fait("cae_rendement",
         "Le Conseil d'analyse économique propose de lire la dépense "
         "scolaire à travers le rendement social net de chaque euro investi. "
         "Son périmètre est limité au premier et au second degré : les "
         "interventions relevant de la petite enfance et de l'enseignement "
         "supérieur en sont explicitement exclues.",
         "2025",
         "Grenet et Landais, « Éducation : comment mieux orienter la "
         "dépense », notes du CAE n° 84, mai 2025",
         CAE_EDUCATION),
    Fait("cae_taille_classes",
         "Le Conseil d'analyse économique range la réduction de la taille des "
         "classes au primaire parmi les politiques « autofinancées », et "
         "recommande de mobiliser les marges budgétaires ouvertes par la "
         "baisse démographique pour l'amplifier dans le premier degré, en "
         "ciblant les contextes prioritaires.",
         "2025", "Grenet et Landais, notes du CAE n° 84, mai 2025, "
         "recommandation 1", CAE_EDUCATION),
    Fait("cae_recrutement",
         "Le Conseil d'analyse économique relève que la recherche ne converge "
         "pas vers un consensus clair sur l'efficacité des politiques de "
         "recrutement des enseignants ou des incitations financières comme "
         "les primes à la performance.",
         "2025", "Grenet et Landais, notes du CAE n° 84, mai 2025, « Former et "
         "accompagner les enseignants »", CAE_EDUCATION),
    Fait("dedoublement_depp",
         "Selon l'évaluation de la DEPP, les élèves des classes de CP "
         "dédoublées en REP+ progressent davantage que des élèves comparables, "
         "surtout en mathématiques ; au CE1, les différences de progression "
         "ne sont plus significatives.",
         "2022", "DEPP, document de travail n° 2021.E04, analysé par Pierre "
         "Merle, La Vie des idées, 31 mai 2022", VIE_IDEES_DEDOUBLEMENT),
    Fait("ocde_pisa_2025",
         "Les résultats de la France en 2025 comptent parmi les plus faibles "
         "jamais obtenus au test PISA, dans les trois domaines. Entre 2015 et "
         "2025, l'écart en sciences entre les 25 % d'élèves les plus favorisés "
         "et les 25 % les plus défavorisés s'est réduit : les résultats ont "
         "baissé parmi les élèves favorisés et sont restés stables parmi les "
         "défavorisés.",
         "2026", "OCDE, Résultats du PISA 2025, volume I, note pays : France",
         OCDE_PISA_2025_FRANCE),
    Fait("depp_pisa_tendance",
         "En compréhension de l'écrit, l'évolution du score moyen de la France "
         "depuis 2000 suit approximativement la même tendance que celle des "
         "pays de l'OCDE ; en culture mathématique, le score de la France "
         "était stable de 2006 à 2018.",
         "2026", "DEPP, note d'information n° 26.40, septembre 2026",
         DEPP_PISA_2025),
    Fait("depp_pisa_voisins",
         "En 2025, le Danemark a en compréhension de l'écrit un score "
         "similaire à celui de la France, et la Suède en culture "
         "mathématique ; en Europe, l'Estonie et la Suisse présentent les "
         "scores les plus élevés en culture mathématique.",
         "2026", "DEPP, note d'information n° 26.40, septembre 2026, "
         "figures 1 et 4", DEPP_PISA_2025),
    Fait("ocde_pisa_2025_paysbas",
         "Aux Pays-Bas, les résultats de 2025 comptent parmi les plus faibles "
         "jamais observés dans les trois domaines : supérieurs à la moyenne de "
         "l'OCDE en mathématiques, inférieurs en compréhension de l'écrit, "
         "proches de la moyenne en sciences. Depuis 2015, la part d'élèves "
         "sous le niveau 2 en compréhension de l'écrit a augmenté de vingt "
         "points.",
         "2026", "OCDE, Résultats du PISA 2025, volume I, note pays : "
         "Pays-Bas, synthèse", OCDE_PISA_2025_PAYSBAS),
    Fait("paysbas_admission",
         "Aux Pays-Bas, une école privée fondée sur des principes religieux "
         "ou philosophiques peut exiger de ses élèves qu'ils adhèrent aux "
         "convictions de son courant, si c'est nécessaire au respect de ses "
         "principes et à condition de l'appliquer sans discrimination et de "
         "façon constante.",
         "2026", "Gouvernement des Pays-Bas, « Public-authority and private "
         "schools »", PAYSBAS_ADMISSION),
    Fait("tallinn_concours",
         "Quatre lycées de Tallinn — Gustav Adolfi Gümnaasium, Tallinna "
         "Inglise Kolledž, Tallinna Reaalkool et Tallinna 21. Kool — "
         "recrutent leurs élèves par un concours d'entrée commun, passé en "
         "fin de neuvième année, en estonien, en mathématiques, en physique "
         "et en anglais.",
         "2026", "Tallinna Inglise Kolledž, « Nelja kooli ühiskatsed »",
         TALLINN_CONCOURS),
    Fait("ocde_decentralisation",
         "Dans l'enseignement public du premier cycle du secondaire, "
         "l'Espagne, la Suisse, la Grèce, la Turquie et la Finlande laissent "
         "aux établissements une part des décisions plus faible encore que la "
         "France.",
         "2018", "OCDE, Les indicateurs de l'éducation à la loupe n° 64, "
         "novembre 2018", OCDE_DECENTRALISATION),
    Fait("ivac",
         "Le ministère publie, pour chaque collège public et privé sous "
         "contrat, des indicateurs de valeur ajoutée calculés sur le diplôme "
         "national du brevet (IVAC) ; les lycées disposent d'indicateurs du "
         "même type (IVAL) depuis de nombreuses années.",
         "2025", "DEPP, Les indicateurs de valeur ajoutée des collèges publics "
         "et privés sous contrat, diplôme national du brevet 2025", DEPP_IVAC),
    Fait("carte_scolaire_2007",
         "Entre 2006 et 2009, la hausse des dérogations permise par "
         "l'assouplissement de la carte scolaire a entraîné une érosion "
         "significative des effectifs de sixième des collèges de l'éducation "
         "prioritaire : au moins 5 % dans les réseaux « réussite scolaire » et "
         "9 % dans les collèges « ambition réussite ».",
         "2013", "Fack et Grenet, Éducation & formations n° 83, DEPP, juin "
         "2013", FACK_GRENET_CARTE),
)}


def fait(cle: str) -> Fait:
    """Un fait du registre.

    Lève `KeyError` sur une clé inconnue, comme `valeur()` : une affirmation
    dont la source a disparu doit casser la construction.
    """
    return FAITS[cle]


# Les thèmes, dans l'ordre où la page « Sources » les présente. Un chiffre
# porte parfois deux thèmes — le premier de cette liste qu'il porte décide de
# l'endroit où il est rangé, pour qu'aucun ne figure deux fois.
THEMES: tuple[tuple[str, str], ...] = (
    ("resultats", "Ce que l'école produit"),
    ("depense", "Ce que l'école coûte"),
    ("moyens", "Les moyens et les effectifs"),
    ("gouvernance", "Qui décide"),
    ("comparaisons", "Les autres pays"),
    ("chiffrage", "Ce que le programme coûterait"),
)


def par_theme() -> list[tuple[str, tuple[Chiffre, ...]]]:
    """Les chiffres rangés par thème, chacun dans un seul.

    Le rangement suit l'ordre de `THEMES` : c'est l'ordre de la page, et il
    sert aussi d'arbitre quand un chiffre en porte plusieurs.
    """
    restants = dict(CHIFFRES)
    groupes: list[tuple[str, tuple[Chiffre, ...]]] = []
    for cle_theme, intitule in THEMES:
        retenus = tuple(c for c in restants.values() if cle_theme in c.themes)
        for chiffre in retenus:
            del restants[chiffre.cle]
        if retenus:
            groupes.append((intitule, retenus))
    if restants:  # un thème oublié ne doit pas faire disparaître un chiffre
        groupes.append(("Autres", tuple(restants.values())))
    return groupes


@dataclass(frozen=True)
class Source:
    """Une source, telle qu'elle s'affiche sur la page « Sources »."""

    nom: str
    url: str
    chiffres: tuple[Chiffre, ...]


def sources() -> list[Source]:
    """Les sources du site, groupées, dans l'ordre de leur premier usage."""
    ordre: list[str] = []
    par_nom: dict[str, list[Chiffre]] = {}
    urls: dict[str, str] = {}
    for chiffre in CHIFFRES.values():
        if chiffre.source not in par_nom:
            ordre.append(chiffre.source)
            par_nom[chiffre.source] = []
            urls[chiffre.source] = chiffre.url
        par_nom[chiffre.source].append(chiffre)
    return [Source(nom, urls[nom], tuple(par_nom[nom])) for nom in ordre]


def valeur(cle: str) -> str:
    """Le texte d'un chiffre, pour l'insérer dans une phrase.

    Lève `KeyError` sur une clé inconnue : une faute de frappe dans un nom de
    chiffre doit casser la construction, et non écrire une phrase trouée.
    """
    return CHIFFRES[cle].texte


# Les multiplicateurs que le registre écrit en toutes lettres. La liste est
# fermée : une unité inconnue lève une erreur plutôt que d'être lue comme
# une unité simple — « 3 Md€ » lu comme « 3 € » serait une faute de
# neuf ordres de grandeur, et silencieuse.
_MULTIPLICATEURS = (
    ("Md€", 1e9), ("M€", 1e6), ("millions", 1e6), ("million", 1e6),
)


def nombre(cle: str) -> float:
    """La valeur d'un chiffre du registre, en nombre, pour un calcul.

    Le chiffrage (`chiffrage.py`) est le seul endroit du site qui calcule. Il
    ne recopie pas les chiffres du registre : il les lit ici, si bien qu'un
    chiffre corrigé à la source corrige aussi tous les calculs qui en
    dépendent. « 6,15 millions » donne 6 150 000 ; « 197,1 Md€ » donne
    197 100 000 000 ; « 26 % » donne 0,26.
    """
    texte = CHIFFRES[cle].texte
    trouve = re.search(r"[−-]?\d[\d   ]*(?:,\d+)?", texte)
    if not trouve:
        raise ValueError(f"{cle} : aucun nombre dans « {texte} »")
    brut = trouve.group(0)
    valeur = float(re.sub(r"[   ]", "", brut)
                   .replace(",", ".").replace("−", "-"))
    reste = texte[trouve.end():].strip()
    if reste.startswith("%"):
        return valeur / 100
    for unite, facteur in _MULTIPLICATEURS:
        if reste.startswith(unite):
            return valeur * facteur
    return valeur
