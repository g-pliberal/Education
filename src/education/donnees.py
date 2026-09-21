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

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chiffre:
    """Un chiffre publiable : sa valeur, ce qu'elle mesure, et sa provenance.

    `texte` est la forme telle qu'elle s'écrit dans une phrase — espaces
    insécables comprises. Le site n'en calcule aucune : les sources publient
    des agrégats, pas des séries, et reformater à la volée un nombre qu'on n'a
    pas recalculé soi-même donne l'illusion d'un modèle là où il n'y a qu'une
    citation.
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
# Les décisions et le recrutement viennent de deux enquêtes différentes, et
# c'est pourquoi ils ont deux adresses : une page d'accueil thématique qui ne
# montre aucun des deux chiffres est la plus facile des réfutations.
OCDE_DECISIONS = ("https://www.oecd.org/content/dam/oecd/en/publications/"
                  "reports/2018/11/how-decentralised-are-education-systems-"
                  "and-what-does-it-mean-for-schools_7c1806fc/e14575d5-en.pdf")
PISA_FRANCE = ("https://www.oecd.org/en/publications/"
               "pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/"
               "france_8008535b-en.html")
PISA_ESTONIE = ("https://www.oecd.org/en/publications/"
                "pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/"
                "estonia_dafed886-en.html")
PISA_PAYSBAS = ("https://www.oecd.org/en/publications/"
                "pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/"
                "netherlands_0941b029-en.html")
PISA_RESULTATS = ("https://www.oecd.org/en/publications/"
                  "pisa-2022-results-volume-i_53f23881-en/full-report/"
                  "how-did-countries-perform-in-pisa_dc514907.html")
OCDE_RSE_RAPPORT = ("https://www.oecd.org/content/dam/oecd/en/publications/"
                    "reports/2025/09/education-at-a-glance-2025_c58fc9ae/"
                    "1c0d9c79-en.pdf")
SENAT_PLF2026 = "https://www.senat.fr/rap/l25-139-313/l25-139-31310.html"
CC_FALLOUX_1994 = ("https://www.conseil-constitutionnel.fr/decision/1994/"
                   "93329DC.htm")
LOI_2021 = "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000043964778"
INSPECTIE_NL = ("https://english.onderwijsinspectie.nl/inspection/"
                "inspection-of-schools-by-the-dutch-inspectorate-of-education/"
                "the-inspectorate%E2%80%99s-judgements")
COUR_PRIVE = ("https://www.ccomptes.fr/sites/default/files/2023-10/"
              "20230601-enseignement-prive-sous-contrat.pdf")
CAE_EDUCATION = "https://cae-eco.fr/static/pdf/cae084-education-250514.pdf"
DEPP_DEMOGRAPHIE = ("https://www.education.gouv.fr/"
                    "demographie-scolaire-le-ministere-publie-pour-la-premiere-fois-des-"
                    "projections-d-effectifs-d-eleves-504392")
COUR_PRIORITAIRE = "https://www.ccomptes.fr/fr/publications/leducation-prioritaire"
IFAU_SUEDE = ("https://www.ifau.se/globalassets/pdf/se/2015/"
              "wp2015-08-School-choice-and-segregation.pdf")
GRONDWET = "https://wetten.overheid.nl/BWBR0001840/"
IGESR_GROUPES = ("https://www.ih2ef.gouv.fr/mise-en-place-des-groupes-de-"
                 "besoins-en-francais-et-mathematiques-rapport-de-ligesr")
DECRET_GROUPES = "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053652587"
CC_LIBERTE = "https://www.conseil-constitutionnel.fr/decision/1977/7787DC.htm"
LOI_1905_ART2 = ("https://www.legifrance.gouv.fr/loda/article_lc/"
                 "LEGIARTI000006340314")
CODE_EDUC_L151_4 = ("https://www.legifrance.gouv.fr/codes/article_lc/"
                    "LEGIARTI000006524461")
DEPP_IPS = ("https://www.education.gouv.fr/depp/"
            "l-indice-de-position-sociale-ips-357755")
DEPP_DEDOUBLEMENT = ("https://archives-statistiques-depp.education.gouv.fr/"
                     "Default/doc/SYRACUSE/50756/evaluation-de-l-impact-de-la-"
                     "reduction-de-la-taille-des-classes-de-cp-et-de-ce1-en-"
                     "rep-sur-les-resul")


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
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026, "", ("depense",)),
    _c("budget_mission_pensions", "89,6 Md€",
       "Crédits de la mission « Enseignement scolaire », compte d'affectation "
       "spéciale « Pensions » compris.",
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026,
       "Premier budget de l'État par le montant.", ("depense",)),
    _c("ocde_pib_comparable", "5,4 % du PIB",
       "Part du PIB consacrée aux établissements d'enseignement, de "
       "l'élémentaire au supérieur, sur le périmètre retenu par l'OCDE — "
       "plus étroit que la dépense intérieure d'éducation française.",
       "2022", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "La DIE française y ajoute notamment les cantines, les transports "
       "scolaires et la formation continue : les deux chiffres ne se "
       "comparent pas.", ("depense",)),
    _c("ocde_pib_moyenne", "4,7 % du PIB",
       "Part du PIB consacrée aux établissements d'enseignement, de "
       "l'élémentaire au supérieur, en moyenne dans l'OCDE.",
       "2022", "OCDE, Regards sur l'éducation 2025", OCDE_RSE_RAPPORT,
       "La France est à 5,4 % : au-dessus, mais de 0,7 point — et non des "
       "deux points que laissait croire la comparaison de la dépense "
       "intérieure d'éducation avec cette moyenne.", ("depense",)),
    _c("prive_budget_etat_primaire", "55 %",
       "Part de l'État dans le budget des écoles privées sous contrat, "
       "contre 59 % dans le public.",
       "2022", "Cour des comptes", COUR_PRIVE, "", ("depense", "liberte")),
    _c("prive_budget_etat_secondaire", "68 %",
       "Part de l'État dans le budget des établissements privés sous "
       "contrat du second degré, contre 74 % dans le public.",
       "2022", "Cour des comptes", COUR_PRIVE,
       "C'est cet écart de six points, et non un chiffre publié en euros, "
       "qui sert à estimer le coût du financement à parité au second "
       "degré.", ("depense", "liberte")),
    _c("public_budget_etat_secondaire", "74 %",
       "Part de l'État dans le budget des établissements publics du second "
       "degré, à comparer aux 68 % du privé sous contrat.",
       "2022", "Cour des comptes", COUR_PRIVE, "", ("depense", "liberte")),
    _c("prive_eleves_part", "17,6 %",
       "Part de l'ensemble des élèves scolarisés dans le privé sous "
       "contrat, soit plus de deux millions d'élèves.",
       "2022", "Cour des comptes", COUR_PRIVE, "", ("gouvernance", "liberte")),
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
       "Coût annuel du dédoublement des classes en éducation prioritaire.",
       "2025", "Cour des comptes, L'éducation prioritaire", COUR_PRIORITAIRE,
       "Le coût total de l'éducation prioritaire a été multiplié par 2,5 "
       "entre 2014 et 2023, passant de 1,1 à 2,6 Md€.",
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
    _c("dedoublement_etp", "15 987",
       "Emplois mobilisés par le dédoublement des classes, de la grande "
       "section au CE1, en éducation prioritaire.",
       "2025", "Cour des comptes, L'éducation prioritaire", COUR_PRIORITAIRE,
       "", ("depense",)),

    # -- ce que l'école produit -----------------------------------------------
    _c("pisa_maths", "474 points",
       "Score moyen des élèves français de 15 ans en mathématiques (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "Moyenne OCDE : 472 points.", ("resultats",)),
    _c("pisa_maths_ocde", "472 points",
       "Moyenne OCDE en mathématiques (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA, "", ("resultats",)),
    _c("pisa_maths_chute", "−21 points",
       "Recul du score français en mathématiques entre PISA 2018 et PISA 2022.",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "La plus forte baisse jamais enregistrée par la France dans cette "
       "enquête.", ("resultats",)),
    _c("pisa_lecture", "474 points",
       "Score moyen en compréhension de l'écrit (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "Moyenne OCDE : 476 points. Recul de 19 points depuis 2018.",
       ("resultats",)),
    _c("pisa_sciences", "487 points",
       "Score moyen en culture scientifique (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "Moyenne OCDE : 485 points. Stable depuis 2018.", ("resultats",)),
    _c("pisa_faibles", "29 %",
       "Part des élèves français de 15 ans sous le niveau 2 en mathématiques, "
       "c'est-à-dire incapables d'appliquer une procédure simple à une "
       "situation qui n'a pas été apprise telle quelle.",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "Ils étaient 21 % en 2018.", ("resultats",)),
    _c("pisa_ecart_social", "113 points",
       "Écart de score en mathématiques entre les élèves français les plus "
       "favorisés et les plus défavorisés.",
       "2022", "OCDE / DEPP", DEPP_PISA,
       "La France reste l'un des pays de l'OCDE où l'origine sociale pèse le "
       "plus lourd sur les résultats.", ("resultats", "inegalites")),
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

    _c("eleves_handicap", "520 000",
       "Élèves en situation de handicap scolarisés en milieu ordinaire.",
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026, "", ("moyens",)),
    _c("aesh_nombre", "140 000",
       "Accompagnants d'élèves en situation de handicap.",
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026,
       "En hausse de deux tiers depuis 2017.", ("moyens",)),
    _c("inclusion_budget", "4,74 Md€",
       "Crédits consacrés à l'école inclusive.",
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026,
       "Dont 3,16 Md€ pour la seule rémunération des accompagnants.",
       ("moyens",)),
    _c("inclusion_aesh", "3,16 Md€",
       "Part de ces crédits consacrée à la rémunération des accompagnants.",
       "2026", "Sénat, rapport sur le PLF 2026, mission "
       "« Enseignement scolaire »", SENAT_PLF2026, "", ("moyens",)),
    _c("pisa_faibles_2018", "21 %",
       "Part des élèves français de 15 ans sous le niveau 2 en mathématiques "
       "lors de l'enquête précédente.",
       "2018", "OCDE / DEPP", DEPP_PISA,
       "Ils sont 29 % en 2022 : huit points de plus en quatre ans.",
       ("resultats",)),
    _c("pisa_lecture_ocde", "476 points",
       "Moyenne OCDE en compréhension de l'écrit (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA, "", ("resultats",)),
    _c("pisa_lecture_chute", "−19 points",
       "Recul du score français en compréhension de l'écrit entre PISA 2018 "
       "et PISA 2022.",
       "2022", "OCDE / DEPP", DEPP_PISA, "", ("resultats",)),
    _c("pisa_sciences_ocde", "485 points",
       "Moyenne OCDE en culture scientifique (PISA).",
       "2022", "OCDE / DEPP", DEPP_PISA, "", ("resultats",)),
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
       "2025", "OCDE, Regards sur l'éducation 2025", OCDE_RSE,
       "Moyenne OCDE : 21 élèves. En baisse de près de deux élèves depuis "
       "2013.", ("moyens",)),

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
       "2017", "OCDE, Education Indicators in Focus (2018), d'après "
       "Regards sur l'éducation 2018, tableau D6.1", OCDE_DECISIONS,
       "Moyenne OCDE : 24 %.", ("gouvernance",)),
    _c("decisions_central_ocde", "24 %",
       "La même part, en moyenne dans l'OCDE.",
       "2017", "OCDE, Education Indicators in Focus (2018), d'après "
       "Regards sur l'éducation 2018, tableau D6.1", OCDE_DECISIONS, "", ("gouvernance",)),
    _c("decisions_etablissement", "10 %",
       "Part des décisions prises au niveau de l'établissement en France.",
       "2017", "OCDE, Education Indicators in Focus (2018), d'après "
       "Regards sur l'éducation 2018, tableau D6.1", OCDE_DECISIONS,
       "Dont 2 % seulement en pleine autonomie ; le reste s'exerce dans un "
       "cadre fixé plus haut.", ("gouvernance",)),
    _c("recrutement_france", "10 %",
       "Part des élèves français dont le chef d'établissement a la "
       "responsabilité principale du recrutement des enseignants.",
       "2022", "OCDE, PISA 2022, note France", PISA_FRANCE,
       "Moyenne OCDE : 60 %. Estonie : 94 %. Pays-Bas : 64 %.",
       ("gouvernance",)),
    _c("recrutement_ocde", "60 %",
       "La même part, en moyenne dans l'OCDE.",
       "2022", "OCDE, PISA 2022, note France", PISA_FRANCE, "", ("gouvernance",)),
    _c("prive_premier_degre", "13,6 %",
       "Part des élèves du premier degré scolarisés dans le privé sous "
       "contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("gouvernance", "liberte")),
    _c("prive_second_degre", "21,2 %",
       "Part des élèves du second degré scolarisés dans le privé sous contrat.",
       "2026", "DEPP, L'éducation nationale en chiffres", DEPP_CHIFFRES,
       "", ("gouvernance", "liberte")),
    _c("prive_catholique", "96 %",
       "Part des élèves du privé sous contrat scolarisés dans un "
       "établissement de l'enseignement catholique.",
       "2022", "Cour des comptes", COUR_PRIVE,
       "La « liberté de choix » française est donc, en pratique, le choix "
       "entre l'école publique de son quartier et une école confessionnelle.",
       ("gouvernance", "liberte")),

    _c("decisions_pleine_autonomie", "2 %",
       "Part des décisions prises en pleine autonomie par l'établissement en "
       "France ; le reste des décisions locales s'exerce dans un cadre fixé "
       "plus haut.",
       "2017", "OCDE, Education Indicators in Focus (2018), d'après "
       "Regards sur l'éducation 2018, tableau D6.1", OCDE_DECISIONS, "",
       ("gouvernance",)),
    _c("recrutement_paysbas", "64 %",
       "Part des élèves néerlandais dont le chef d'établissement recrute "
       "les enseignants.",
       "2022", "OCDE, PISA 2022, note Pays-Bas", PISA_PAYSBAS, "",
       ("gouvernance",)),
    # -- ailleurs -------------------------------------------------------------
    _c("prive_fonds_etat", "8 Md€",
       "Fonds versés par l'État à l'enseignement privé sous contrat, "
       "essentiellement en rémunération des enseignants.",
       "2022", "Cour des comptes", COUR_PRIVE,
       "Environ 10 Md€ de fonds publics au total, collectivités comprises. "
       "Les ressources publiques représentent 73 % du budget de ces "
       "établissements.", ("depense", "liberte")),
    _c("prive_cout_etat_primaire", "2 244 €",
       "Ce qu'un écolier du privé sous contrat coûte à l'État.",
       "2022", "Cour des comptes", COUR_PRIVE,
       "Classes plus chargées, enseignants plus souvent contractuels, "
       "absence de remplaçants.", ("depense", "liberte")),
    _c("public_cout_etat_primaire", "4 212 €",
       "Ce qu'un écolier du public coûte à l'État.",
       "2022", "Cour des comptes", COUR_PRIVE,
       "L'écart avec le privé sous contrat est de près du double : c'est lui "
       "que le financement à l'élève doit combler, et c'est le premier poste "
       "de coût de notre proposition.", ("depense", "liberte")),
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
       "Score de l'Estonie en mathématiques (PISA 2022) : premier rang "
       "européen, et troisième rang des pays de l'OCDE derrière le Japon et "
       "la Corée.",
       "2022", "OCDE, PISA 2022, résultats volume I", PISA_RESULTATS,
       "Deux points devant la Suisse (508) : l'écart est inférieur à la "
       "marge d'erreur de l'enquête, et nous ne le présentons donc pas "
       "comme un classement. La dépense estonienne par élève est inférieure "
       "à la française.",
       ("comparaisons",)),
    _c("estonie_recrutement", "94 %",
       "Part des élèves estoniens dont le chef d'établissement recrute "
       "lui-même les enseignants.",
       "2022", "OCDE, PISA 2022, note Estonie", PISA_ESTONIE, "",
       ("comparaisons",)),
    _c("suede_reforme", "1992",
       "Année de la réforme suédoise des friskolor : financement public à "
       "l'élève, ouvert aux établissements privés à but lucratif.",
       "1992", "IFAU, School choice and segregation (2015)", IFAU_SUEDE,
       "Le contre-exemple dont ce programme tire ses garde-fous. La "
       "ségrégation scolaire suédoise a augmenté ; la part qu'en explique le "
       "libre choix est, selon l'IFAU, modeste au regard de la ségrégation "
       "résidentielle.", ("comparaisons",)),
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
    Fait("liberte_enseignement",
         "Le Conseil constitutionnel a jugé que la liberté de l'enseignement "
         "figure parmi les principes fondamentaux reconnus par les lois de "
         "la République, et a valeur constitutionnelle. La même décision "
         "reconnaît l'obligation, pour les maîtres du privé sous contrat, de "
         "respecter le caractère propre de l'établissement, sans que cela "
         "puisse porter atteinte à leur liberté de conscience.",
         "1977", "Conseil constitutionnel, décision n° 77-87 DC du "
         "23 novembre 1977", CC_LIBERTE),
    Fait("falloux",
         "L'article L. 151-4 du code de l'éducation, hérité de la loi "
         "Falloux de 1850, plafonne à un dixième de leurs dépenses annuelles "
         "les subventions que les collectivités et l'État peuvent verser aux "
         "établissements privés d'enseignement général du second degré.",
         "1850", "Article L. 151-4 du code de l'éducation", CODE_EDUC_L151_4),
    Fait("laicite_1905",
         "L'article 2 de la loi du 9 décembre 1905 dispose que la République "
         "ne reconnaît, ne salarie ni ne subventionne aucun culte.",
         "1905", "Loi du 9 décembre 1905, article 2", LOI_1905_ART2),
    Fait("ips",
         "La DEPP calcule pour chaque école, collège et lycée un indice de "
         "position sociale (IPS), qui résume les conditions "
         "socio-économiques et culturelles des familles de ses élèves. Ces "
         "indices sont publiés en données ouvertes, établissement par "
         "établissement.",
         "2022", "DEPP, indice de position sociale", DEPP_IPS),
    Fait("dedoublement_effets",
         "L'évaluation de la DEPP mesure un effet du dédoublement sur la "
         "progression des élèves en français et en mathématiques au cours "
         "des deux premières années de l'élémentaire, ainsi qu'un climat de "
         "classe plus favorable. Mais l'écart de résultats entre l'éducation "
         "prioritaire et le reste du système ne s'est pas réduit, et le "
         "dispositif ne touche qu'une minorité des élèves en difficulté de "
         "l'école élémentaire.",
         "2023", "DEPP, évaluation de l'impact de la réduction de la taille "
         "des classes en REP+", DEPP_DEDOUBLEMENT),
    Fait("falloux_1994",
         "La dernière tentative de révision de la loi Falloux, en 1994, a "
         "été partiellement censurée par le Conseil constitutionnel : la loi "
         "laissait les collectivités libres de subventionner les "
         "investissements des établissements privés sans encadrement, et ne "
         "comportait donc pas les garanties nécessaires au respect du "
         "principe d'égalité — entre établissements privés, et au détriment "
         "des établissements publics.",
         "1994", "Conseil constitutionnel, décision n° 93-329 DC du "
         "13 janvier 1994", CC_FALLOUX_1994),
    Fait("loi_2021",
         "La loi du 24 août 2021 confortant le respect des principes de la "
         "République a soumis l'instruction en famille à autorisation "
         "préalable et renforcé le contrôle des établissements privés hors "
         "contrat.",
         "2021", "Loi n° 2021-1109 du 24 août 2021", LOI_2021),
    Fait("inspection_nl",
         "L'inspection néerlandaise de l'enseignement juge « très faible » "
         "un établissement dont les résultats et la qualité "
         "d'enseignement passent sous la norme légale, publie la liste de "
         "ces établissements, procède à une inspection complète dans "
         "l'année puis à une contre-visite au bout d'un an au plus, et peut "
         "recommander au ministre la fermeture de l'établissement qui ne se "
         "redresse pas.",
         "2024", "Inspection néerlandaise de l'enseignement", INSPECTIE_NL),
    Fait("cour_prioritaire",
         "La Cour des comptes juge que les écarts de résultats entre "
         "l'éducation prioritaire et le reste du système tardent à se "
         "réduire alors que le coût de cette politique n'a cessé de "
         "croître, et que les progrès de court terme obtenus par le "
         "dédoublement s'estompent à l'entrée au collège.",
         "2025", "Cour des comptes, L'éducation prioritaire",
         COUR_PRIORITAIRE),
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
