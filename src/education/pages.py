"""Le contenu du site, page par page.

Chaque fonction rend le corps d'une page — tout ce qui se trouve entre le
bandeau et le pied. Le gabarit fait le reste.

Les chiffres ne sont jamais écrits ici : ils sont demandés à
`donnees.valeur()`, qui les prend au registre. Une faute de frappe dans un nom
de chiffre casse la construction ; un chiffre corrigé à la source l'est partout
d'un coup, page « Sources » comprise.
"""

from __future__ import annotations

from . import chiffrage as ch
from . import gabarit as g
from .donnees import (CHIFFRES, FAITS, fait, par_theme, sources,
                      valeur as v)


def _source(cle: str) -> str:
    """La citation d'un fait, en lien vers le document qui l'établit."""
    f = fait(cle)
    return f'<a href="{f.url}">{g.echapper(f.source)}</a>' 

# -- l'accueil ---------------------------------------------------------------


def index() -> str:
    corps = g.affiche(
        "Parti libéral français · École",
        "L'école française dépense beaucoup, et apprend de moins en moins.",
        "Ce site fait deux choses, et deux seulement : établir ce que la "
        "politique éducative française coûte et ce qu'elle obtient, puis "
        "exposer l'alternative libérale — <strong class=\"cle-texte\">le "
        "financement suit l'élève, l'établissement s'administre, les "
        "résultats se publient</strong>. Les constats sont sourcés. Les "
        "propositions sont assumées.",
    )

    corps += g.reperes((
        g.Repere("Ce que l'école coûte",
                 v("die_montant"),
                 f"Soit {v('die_pib')}, et {v('die_par_eleve')} par élève ou "
                 "étudiant."),
        g.Repere("Ce que les élèves savent",
                 v("timss_cm1_maths"),
                 "En mathématiques en CM1, contre "
                 f"{v('timss_cm1_maths_ue')} dans l'Union européenne : la "
                 "France est au dernier rang des pays de l'Union ayant "
                 "participé."),
        g.Repere("Ce qu'il en reste à vingt ans",
                 v("jdc_difficultes"),
                 "des jeunes sont en difficulté de lecture à la Journée "
                 f"défense et citoyenneté, dont {v('jdc_illettrisme')} en "
                 "situation d'illettrisme."),
    ))

    corps += g.note(
        "<p><strong>Ce site en deux minutes.</strong> La France consacre à "
        "son école une part de sa richesse supérieure à la moyenne de "
        "l'OCDE, et la répartit à contretemps : moins que la moyenne par "
        "écolier, un quart de plus par lycéen. Ses résultats, eux, "
        "reculent : à quinze ans, la France est dans la moyenne de l'OCDE, "
        "à son plus bas niveau en mathématiques et en lecture ; en "
        "CM1, elle est au dernier rang des pays de l'Union ayant participé à "
        "l'enquête. Ce n'est donc pas d'abord "
        "une question de montant : c'est une question de qui décide, de qui "
        "rend des comptes, et de qui peut partir quand rien ne change.</p>"
        f'<p class="actions"><a class="bouton" href="{g.lien("proposition")}">'
        "Lire la proposition</a>"
        f'<a class="bouton second" href="{g.lien("resultats")}">Voir d\'abord '
        "les résultats</a></p>",
        "entree",
    )

    corps += "<h2>Le diagnostic en trois points</h2>"
    corps += g.points((
        ("Le problème n'est pas le montant, c'est la répartition",
         "Sur le périmètre comparable de l'OCDE, l'effort français est "
         f"supérieur à la moyenne : {v('ocde_pib_comparable')}, contre "
         f"{v('ocde_pib_comparable_ocde')}. Mais la France dépense "
         f"{v('ocde_elementaire_fr')} par écolier quand la moyenne de l'OCDE "
         f"est de {v('ocde_elementaire_ocde')}, et {v('ocde_lycee_fr')} par "
         f"lycéen quand cette moyenne est de {v('ocde_lycee_ocde')}. Nous "
         "dépensons peu là où tout se joue, et beaucoup là où il est déjà "
         "tard."),
        ("Le pilotage est le problème",
         f"{v('decisions_central')} des décisions d'un collège public se "
         f"prennent au niveau de l'État central, contre "
         f"{v('decisions_central_ocde')} en moyenne dans l'OCDE. Un chef "
         "d'établissement français ne choisit pas son équipe : il reçoit des "
         "affectations. On ne peut pas lui demander des résultats dont il ne "
         "tient aucun des leviers."),
        ("L'inégalité est le résultat",
         f"{v('pisa_ecart_social')} séparent en mathématiques les élèves "
         "français très favorisés des très défavorisés, contre "
         f"{v('pisa_ecart_social_ocde')} en moyenne dans l'OCDE. Le système "
         "qui se réclame le plus de l'égalité est l'un de ceux où l'origine "
         "sociale pèse le plus lourd. Ce n'est pas un accident de parcours : "
         "c'est ce qu'il produit."),
    ))

    corps += g.engagements((
        g.Engagement(
            "0 €",
            "Le financement public suit l'élève ; la famille modeste ne paie "
            "rien.",
            "La dotation est attachée à l'enfant, et versée à l'établissement "
            "qui l'accueille — public, privé sous contrat, école nouvelle. "
            "L'écart de financement public entre le privé et le public se "
            "réduit d'un cinquième ; ce qui reste peut être demandé aux "
            "familles, sous un plafond, et jamais aux familles modestes."),
        g.Engagement(
            "+ 40 %",
            "Un financement majoré pour l'élève défavorisé.",
            "Une pondération sociale du montant versé, et une pondération de "
            "handicap. C'est la réponse à l'objection la plus sérieuse faite à "
            "la liberté scolaire : un établissement doit avoir intérêt à "
            "accueillir l'élève difficile, et non à l'éviter."),
        g.Engagement(
            "0",
            "Plus de carte scolaire d'affectation.",
            "Les familles classent leurs vœux, les établissements ne "
            "sélectionnent pas, et une procédure publique attribue les places "
            "selon des règles écrites — fratrie, proximité, tirage au sort "
            "en cas de sur-demande. L'adresse compte encore, mais elle ne "
            "décide plus seule."),
        g.Engagement(
            "1 seul",
            "Un contrat unique pour tout établissement financé.",
            "Enseigner le socle, ouvrir ses comptes, passer les évaluations "
            "nationales, accueillir sans sélectionner. Qui tient ce contrat "
            "est financé, quelle que soit sa nature juridique. Qui ne le "
            "tient plus cesse de l'être."),
        g.Engagement(
            "Le chef recrute",
            "L'établissement choisit son équipe et son projet.",
            f"Aujourd'hui {v('recrutement_france')} des élèves français sont "
            "dans un établissement dont le chef recrute ses enseignants, "
            f"contre {v('recrutement_ocde')} dans l'OCDE. Autonomie de "
            "recrutement, de budget et de méthode, contre reddition de "
            "comptes publique."),
        g.Engagement(
            "Tout est publié",
            "Les résultats, les moyens et les comptes de chaque école.",
            "Non pas le palmarès brut, qui ne mesure que le public recruté, "
            "mais la <em>valeur ajoutée</em> : ce que l'établissement apporte "
            "à ses élèves, à niveau d'entrée comparable. C'est la condition "
            "pour que le choix des familles soit un choix éclairé."),
    ), "Les six engagements du programme")

    corps += g.paire(
        "<h2>Ce que nous disons</h2>" + g.leviers((
            '<span class="badge proposition">Oui</span> L\'argent public de '
            "l'école appartient à l'élève, pas à l'institution qui "
            "l'accueille.",
            '<span class="badge proposition">Oui</span> Un établissement qui '
            "ne choisit rien ne peut répondre de rien : l'autonomie est la "
            "condition de la responsabilité.",
            '<span class="badge proposition">Oui</span> Le contribuable a le '
            "droit de savoir ce que produit chaque euro, école par école.",
            '<span class="badge proposition">Oui</span> Une école qui échoue '
            "durablement, publique ou privée, doit changer de direction ou "
            "fermer.",
        )),
        "<h2>Ce que nous ne disons pas</h2>" + g.leviers((
            '<span class="badge">Non</span> Que l\'école publique devrait '
            "disparaître. Elle scolarisera toujours la grande majorité des "
            "élèves, et c'est elle que la réforme doit libérer en premier.",
            '<span class="badge">Non</span> Qu\'il faut dépenser plus. '
            "Chiffré poste par poste, le programme tient dans la dépense "
            "d'aujourd'hui — au prix de choix que nous nommons, et de "
            "perdants que nous désignons. "
            f'<a href="{g.lien("chiffrage")}">Le chiffrage</a>.',
            '<span class="badge">Non</span> Que le marché réglera tout. '
            "La Suède a montré ce que donne une liberté scolaire sans "
            "garde-fous : nous en tirons quatre règles précises.",
            '<span class="badge">Non</span> Que les enseignants sont le '
            "problème. Ils sont, dans l'OCDE, parmi les moins payés par "
            "rapport aux autres diplômés du supérieur.",
        )),
    )

    corps += "<h2>Lire la suite</h2>"
    corps += g.points((
        ("Le constat",
         "Ce que les enquêtes internationales mesurent vraiment, où va "
         "l'argent, et qui décide dans l'école française. "
         f'<a href="{g.lien("resultats")}">Les résultats</a>, '
         f'<a href="{g.lien("depense")}">la dépense</a>, '
         f'<a href="{g.lien("gouvernance")}">la gouvernance</a>.'),
        ("La proposition",
         "Sept réformes, leur calendrier, leur coût et leurs garde-fous. "
         f'<a href="{g.lien("proposition")}">La proposition</a>, '
         f'<a href="{g.lien("chiffrage")}">son chiffrage</a>, et '
         f'<a href="{g.lien("comparaisons")}">ce que font nos voisins</a>.'),
        ("La contradiction",
         "Les dix objections sérieuses, y compris celles qui ont raison, et "
         "tous les chiffres avec leur source. "
         f'<a href="{g.lien("objections")}">Les objections</a>, '
         f'<a href="{g.lien("sources")}">les sources</a>.'),
    ))

    corps += g.note(
        "<p><strong>Ce que ce site ne peut pas faire.</strong> Comparer des "
        "systèmes éducatifs, c'est comparer des pays qui ne scolarisent ni "
        "les mêmes élèves, ni au même âge, ni avec la même définition de "
        "l'échec. Les enquêtes citées ici sont solides, mais elles mesurent "
        "ce qu'elles mesurent : des compétences écrites, à un moment donné. "
        "Aucune ne dit ce qu'une école fait d'un enfant sur vingt ans. Nous "
        "les citons pour ce qu'elles montrent, et nous disons où elles "
        f"s'arrêtent — sur la page <a href=\"{g.lien('objections')}\">"
        "Objections</a>.</p>",
        "vigilance",
    )
    return corps


# -- le constat --------------------------------------------------------------


def resultats() -> str:
    corps = g.affiche(
        "Le constat · 1",
        "Ce que les élèves savent, et ce qu'ils ne savent plus.",
        "Quatre enquêtes, trois internationales et une française, disent la "
        "même chose : le niveau des élèves français baisse, la part des "
        "élèves en difficulté augmente, et l'origine sociale pèse plus "
        "lourd qu'ailleurs.",
    )

    corps += g.plan((
        ("pisa", "PISA, 15 ans"),
        ("timss", "TIMSS, CM1 et 4e"),
        ("pirls", "PIRLS, lecture"),
        ("jdc", "À la sortie"),
        ("inegalites", "Les inégalités"),
        ("limites", "Ce que cela ne dit pas"),
    ))

    corps += g.reperes((
        g.Repere("Mathématiques à 15 ans", v("pisa_maths"),
                 f"Moyenne OCDE : {v('pisa_maths_ocde')}. "
                 f"{v('pisa_maths_chute')} depuis 2022."),
        g.Repere("Élèves en difficulté", v("pisa_faibles"),
                 "sous le niveau 2 en mathématiques, contre "
                 f"{v('pisa_faibles_2022')} en 2022 et "
                 f"{v('pisa_faibles_2018')} en 2018."),
        g.Repere("Écart social", v("pisa_ecart_social"),
                 "entre les élèves très favorisés et très défavorisés, "
                 f"contre {v('pisa_ecart_social_ocde')} dans l'OCDE."),
    ))

    corps += "<h2 id=\"pisa\">PISA 2025 : le plus bas niveau jamais mesuré</h2>"
    corps += (
        "<p>PISA mesure tous les trois ans ce que les élèves de quinze ans "
        "savent faire d'un savoir dans une situation qu'on ne leur a pas "
        f"apprise. En 2025, la France obtient {v('pisa_maths')} en "
        f"mathématiques et {v('pisa_lecture')} en compréhension de l'écrit : "
        f"dans la moyenne de l'OCDE ({v('pisa_maths_ocde')} et "
        f"{v('pisa_lecture_ocde')}), mais à son plus bas niveau depuis sa "
        "première participation. En mathématiques : "
        f"{v('pisa_maths_chute')} depuis 2022, après "
        f"{v('pisa_maths_chute_2022')} entre 2018 et 2022 ("
        + _source("ocde_pisa_2025") + ").</p>"
        "<p>Il faut dire aussi ce qui nuance ce constat, parce qu'on nous "
        "l'opposera : la baisse n'est pas propre à la France. La moyenne de "
        f"l'OCDE baisse aussi : {v('pisa_maths_chute_ocde')} en "
        f"mathématiques, {v('pisa_lecture_chute_ocde')} en compréhension de "
        "l'écrit ; en "
        "lecture, la France suit depuis 2000 à peu près la tendance de "
        "l'OCDE, et en mathématiques son score était stable de 2006 à 2018 ("
        + _source("depp_pisa_tendance") + "). Ce qui la distingue, c'est "
        "l'ampleur de sa chute en mathématiques depuis 2018, et le point où "
        "elle la conduit.</p>"
        "<p>La moyenne rassure à tort. Le bas s'élargit : "
        f"{v('pisa_faibles')} des élèves sont sous le niveau 2 en "
        f"mathématiques, contre {v('pisa_faibles_2022')} en 2022 et "
        f"{v('pisa_faibles_2018')} en 2018 ; en compréhension de l'écrit, "
        f"{v('pisa_faibles_lecture')}, contre {v('pisa_faibles_lecture_2000')} "
        "en 2000. Et le haut fond : "
        f"{v('pisa_tres_bons')} d'élèves très performants en mathématiques, "
        f"contre {v('pisa_tres_bons_2003')} en 2003 et "
        f"{v('pisa_tres_bons_ocde')} en moyenne dans l'OCDE. Le niveau 2 "
        "n'est pas l'excellence : c'est le seuil à partir duquel un élève "
        "sait reconnaître comment une situation simple se traduit en "
        "mathématiques — comparer la longueur de deux itinéraires, convertir "
        "un prix dans une autre devise.</p>"
    )
    corps += g.tableau(
        "PISA 2025 : les scores français et la moyenne de l'OCDE",
        ("Domaine", "France", "Moyenne OCDE", "France depuis 2022",
         "Élèves sous le niveau 2"),
        (
            ("Mathématiques", v("pisa_maths"), v("pisa_maths_ocde"),
             v("pisa_maths_chute"),
             f"{v('pisa_faibles')} (OCDE : {v('pisa_faibles_ocde')})"),
            ("Compréhension de l'écrit", v("pisa_lecture"),
             v("pisa_lecture_ocde"), v("pisa_lecture_chute"),
             f"{v('pisa_faibles_lecture')} (OCDE : "
             f"{v('pisa_faibles_lecture_ocde')})"),
            ("Culture scientifique", v("pisa_sciences"),
             v("pisa_sciences_ocde"), "stable", "—"),
        ),
    )

    corps += ("<h2 id=\"timss\">TIMSS : au dernier rang des pays de "
              "l'Union européenne évalués</h2>")
    corps += (
        "<p>PISA interroge des jeunes de quinze ans sur des compétences "
        "transversales. TIMSS fait l'inverse : elle évalue, en CM1 puis en "
        "quatrième, les mathématiques et les sciences telles qu'elles sont "
        "enseignées. C'est l'enquête la plus proche de ce que l'école dit "
        "faire, et c'est celle où la France est la plus mal placée.</p>"
        f"<p>En CM1, la France obtient {v('timss_cm1_maths')} en "
        f"mathématiques, contre {v('timss_cm1_maths_ue')} en moyenne dans "
        "l'Union européenne. <strong class=\"cle-texte\">C'est le dernier "
        "rang des pays de l'Union ayant participé à l'enquête</strong> — une "
        "quinzaine d'États membres, les autres n'y participant pas. "
        f"{v('timss_cm1_seuil')} des élèves français de CM1 n'atteignent pas "
        "le niveau élémentaire : ils sortiront de l'école primaire sans les "
        "opérations. En sciences, "
        f"{v('timss_cm1_sciences')} contre {v('timss_cm1_sciences_ue')} "
        f"dans l'Union. En quatrième, {v('timss_quatrieme_maths')} contre "
        f"{v('timss_quatrieme_maths_ue')}.</p>"
        "<p>Ces scores sont <em>stables</em> depuis 2019. C'est la phrase la "
        "plus grave du rapport : le décrochage français n'est plus une chute, "
        "c'est un palier. Nous nous sommes installés en bas.</p>"
    )

    corps += "<h2 id=\"pirls\">PIRLS : lire en CM1</h2>"
    corps += (
        f"<p>PIRLS mesure la compréhension de l'écrit en CM1. La France y "
        f"obtient {v('pirls')}, contre {v('pirls_ue')} en moyenne "
        "européenne. C'est la "
        "seule bonne nouvelle de cette page : le score est stable, après "
        "quinze années de baisse continue, et l'écart avec l'Europe s'est "
        "réduit — les autres pays ayant reculé davantage.</p>"
        "<p>Un palier après quinze ans de baisse n'est pas un redressement. "
        "C'est un arrêt de la chute, contemporain d'un effort considérable "
        "sur les premières années — dédoublement des classes en éducation "
        "prioritaire, recentrage sur les fondamentaux —, sans qu'aucune "
        "évaluation permette de le lui attribuer ; et il n'a pas "
        "d'équivalent au collège.</p>"
    )

    corps += "<h2 id=\"jdc\">À la sortie : un jeune sur huit</h2>"
    corps += (
        "<p>Les enquêtes internationales portent sur des élèves. La Journée "
        "défense et citoyenneté, elle, teste presque toute une classe d'âge — "
        f"{v('jdc_testes')} jeunes en 2024 — au moment où l'école les a "
        "quittés. Le "
        "résultat est le bilan le plus brutal du système :</p>"
    )
    corps += g.leviers((
        f"<strong>{v('jdc_difficultes')}</strong> des jeunes sont en "
        "difficulté de lecture.",
        f"<strong>{v('jdc_illettrisme')}</strong> — un sur vingt — sont "
        "considérés en situation d'illettrisme, après au moins dix ans "
        "d'école obligatoire.",
        "Les jeunes sortis du système sans diplôme sont les plus touchés, et "
        "les écarts entre territoires sont considérables.",
    ))
    corps += g.encadre(
        "<h3 class=\"serif\">Cinquante mille par an, ce n'est pas une "
        "statistique</h3>"
        f"<p>{v('jdc_illettrisme')} des {v('jdc_testes')} jeunes testés en "
        "2024, cela fait <strong class=\"cle-texte\">plus de cinquante "
        "mille jeunes par an</strong> qui sortent d'au moins dix années de "
        "scolarité obligatoire sans savoir lire un mode d'emploi. À "
        "l'échelle d'un quinquennat, un quart de million. Aucun chiffre de "
        "dépense ne pèse contre celui-là.</p>"
    )

    corps += ("<h2 id=\"inegalites\">L'une des écoles les plus inégalitaires "
              "de l'OCDE</h2>")
    corps += (
        f"<p>{v('pisa_ecart_social')} séparent en mathématiques les élèves "
        "français très favorisés des très défavorisés, contre "
        f"{v('pisa_ecart_social_ocde')} en moyenne dans l'OCDE ; en "
        f"compréhension de l'écrit, {v('pisa_ecart_lecture')} contre "
        f"{v('pisa_ecart_lecture_ocde')} ; en sciences, "
        f"{v('pisa_ecart_sciences')} contre {v('pisa_ecart_sciences_ocde')}. "
        "La France figure parmi les pays de l'OCDE où l'origine sociale "
        "prédit le mieux les résultats scolaires — c'est-à-dire parmi ceux "
        "où l'école corrige le moins ce qu'elle reçoit.</p>"
        "<p>Et quand l'écart se réduit, ce n'est pas pour une bonne raison. "
        "Entre 2015 et 2025, il s'est resserré en sciences parce que les "
        "élèves favorisés ont baissé, les défavorisés restant au même niveau "
        "— un rapprochement par le bas (" + _source("ocde_pisa_2025") + ").</p>"
        "<p>Ce constat est le plus embarrassant pour tout le monde. Il l'est "
        "pour ceux qui défendent le système tel quel, puisque l'égalité est "
        "sa justification première. Il l'est aussi pour nous : une réforme "
        "libérale mal faite aggraverait cet écart au lieu de le réduire. "
        "C'est pourquoi la pondération sociale du financement n'est pas un "
        "ornement de notre proposition — c'en est la clé de voûte, et la "
        f'page <a href="{g.lien("objections")}">Objections</a> y revient.</p>'
    )

    corps += "<h2 id=\"limites\">Ce que ces chiffres ne disent pas</h2>"
    corps += g.note(
        "<p>Ces enquêtes mesurent des compétences écrites en mathématiques, "
        "en sciences et en lecture. Elles ne mesurent ni ce qu'un élève "
        "devient, ni ce qu'une école lui a transmis d'autre. Elles portent "
        "sur des échantillons, avec des marges d'erreur de quelques points : "
        "deux pays séparés de trois points ne sont pas départagés. Et un "
        "score national masque toujours des écarts internes plus grands que "
        "les écarts entre pays.</p>"
        "<p>Ce qu'elles établissent en revanche solidement, parce que trois "
        "enquêtes indépendantes le disent ensemble : le niveau moyen a "
        "baissé, la base a décroché, et l'écart social reste parmi les plus "
        "marqués de l'OCDE. Aucune de ces trois affirmations n'est "
        "sérieusement contestée.</p>"
        "<p>Ce qu'elles n'établissent pas, c'est la cause. La baisse de 2025 "
        "touche presque toute l'OCDE, y compris les pays dont nous citons "
        f'l\'organisation en exemple (<a href="{g.lien("comparaisons")}">'
        "Ailleurs en Europe</a>). Le lien entre la manière dont l'école "
        "française est gouvernée et ses résultats est notre thèse ; nous la "
        "défendons, mais ce n'est pas un constat.</p>",
        "vigilance",
    )
    return corps


def depense() -> str:
    corps = g.affiche(
        "Le constat · 2",
        "Où va l'argent de l'école.",
        f"{v('die_montant')} tous financeurs confondus, soit "
        f"{v('die_pib')}. L'enseignement scolaire "
        f"est, avec {v('budget_mission_pensions')}, le premier budget de "
        "l'État. La question n'est pas de savoir si c'est trop : c'est de "
        "savoir où cela va.",
    )

    corps += g.plan((
        ("combien", "Combien"),
        ("repartition", "Pour qui"),
        ("qui-paie", "Qui paie"),
        ("rendement", "Ce que ça rend"),
        ("demographie", "La marge qui vient"),
    ))

    corps += g.reperes((
        g.Repere("Dépense d'éducation", v("die_montant"),
                 f"{v('die_pib')}, en hausse de {v('die_hausse')} en euros "
                 "constants sur un an."),
        g.Repere("Par élève ou étudiant", v("die_par_eleve"),
                 "tous niveaux confondus, apprentissage compris."),
        g.Repere("Mission Enseignement scolaire", v("budget_mission_pensions"),
                 f"pensions comprises ({v('budget_mission')} hors pensions) : "
                 "le premier budget de l'État."),
    ))

    corps += ("<h2 id=\"combien\">Un effort supérieur à la moyenne, réparti à "
              "contretemps</h2>")
    corps += (
        f"<p>La dépense intérieure d'éducation atteint {v('die_montant')} en "
        f"2024, soit {v('die_pib')}. Ce chiffre est un agrégat français : il "
        "compte tout ce que la nation consacre à l'éducation, cantines, "
        "transports scolaires et formation continue compris. <strong>Il ne "
        "se compare donc pas aux moyennes internationales, et nous ne le "
        "comparons pas.</strong> Sur le périmètre retenu par l'OCDE — les "
        "seuls établissements d'enseignement —, la France consacre "
        f"{v('ocde_pib_comparable')} à son école et à son supérieur, contre "
        f"{v('ocde_pib_comparable_ocde')} en moyenne dans l'OCDE : un effort "
        "supérieur à la moyenne.</p>"
        "<p>Rapportée à l'élève, cette dépense dit quelque chose de plus "
        "précis, et de plus embarrassant, qu'un total.</p>"
    )
    corps += g.tableau(
        "Dépense annuelle par élève, France et moyenne OCDE, en 2022 "
        "(équivalents USD, à parité de pouvoir d'achat)",
        ("Niveau", "France", "Moyenne OCDE", "Écart"),
        (
            ("Élémentaire", v("ocde_elementaire_fr"),
             v("ocde_elementaire_ocde"), v("ocde_ecart_elementaire")),
            ("Collège", v("ocde_college_fr"), v("ocde_college_ocde"),
             v("ocde_ecart_college")),
            ("Lycée", v("ocde_lycee_fr"), v("ocde_lycee_ocde"),
             v("ocde_ecart_lycee")),
        ),
        ("texte", "nombre", "nombre", "nombre"),
    )
    corps += (
        "<p>Le fait central de ce site est là, et il est plus précis que le "
        "slogan qu'on entend des deux côtés. <strong class=\"cle-texte\">Le "
        "problème de la France n'est pas d'abord ce qu'elle dépense pour son "
        "école : c'est qu'elle dépense à contretemps</strong> — en dessous "
        "de la moyenne de l'OCDE à l'école élémentaire, où tout se joue, et "
        "d'un quart au-dessus au lycée, où il est déjà tard.</p>"
        "<p>Cela retire sa force à la réponse habituelle — « il faut des "
        "moyens » — prise comme réponse unique, sans la rendre absurde : au "
        "primaire, le niveau de dépense est réellement bas, et nous "
        "l'écrivons. Ce que ces chiffres désignent, c'est où prendre et où "
        "mettre — ce qu'aucune enveloppe supplémentaire ne fait toute "
        "seule.</p>"
    )

    corps += "<h2 id=\"repartition\">Un euro qui va d'abord aux grands</h2>"
    corps += g.tableau(
        "Dépense moyenne par élève et par niveau, en 2024 (DEPP)",
        ("Niveau", "Dépense annuelle par élève"),
        (
            ("Premier degré (école)", v("die_premier_degre")),
            ("Collège", v("die_college")),
            ("Lycée général et technologique", v("die_lycee_general")),
            ("Lycée professionnel", v("die_lycee_pro")),
            ("Université", v("die_universite")),
            ("Classe préparatoire aux grandes écoles", v("die_cpge")),
            ("Ensemble", v("die_par_eleve")),
        ),
    )
    corps += (
        "<p>Un écolier reçoit "
        f"{v('die_premier_degre')} par an ; un élève de classe préparatoire, "
        f"{v('die_cpge')}. <strong class=\"cle-texte\">Le rapport est de un à "
        "deux.</strong> Mais le surcoût du second degré ne va pas d'abord à "
        f"ceux qui ont déjà réussi : le lycéen professionnel ({v('die_lycee_pro')}) "
        f"coûte plus que le lycéen général ({v('die_lycee_general')}), et une "
        "part de l'écart tient à la diversité des filières et des options, "
        "et aux services annexes — transports scolaires, internats, "
        f"cantines, médecine scolaire —, qui pèsent {v('services_annexes')} "
        f"de la dépense d'éducation en France contre "
        f"{v('services_annexes_ocde')} dans l'OCDE.</p>"
        "<p>Cette pente, du primaire vers le lycée, existe partout. Ce qui "
        "distingue la France, c'est son ampleur : en dessous de la moyenne "
        "de l'OCDE à l'élémentaire, très au-dessus au lycée.</p>"
        "<p>Un mot sur ce que nous ne tirons pas de la littérature. Le "
        "Conseil d'analyse économique a proposé en 2025 de lire la dépense "
        "scolaire à travers le <strong>rendement social net</strong> de "
        "chaque euro investi — l'outil dont ce débat manquait. Nous ne lui "
        "faisons pas dire que les premières années viennent en tête du "
        "classement : <strong class=\"cle-texte\">son périmètre exclut "
        "explicitement la petite enfance et l'enseignement supérieur</strong>, "
        "et porte sur les leviers du premier et du second degré. Ce qu'il "
        "établit, et qui suffit ici, c'est que des dépenses de coût "
        "comparable produisent des résultats très inégaux — ce qui est un "
        "argument sur la répartition, non sur l'âge des élèves ("
        + _source("cae_rendement") + ").</p>"
        "<p>Il faut dire aussi ce qu'il conclut, et qui ne va pas dans notre "
        "sens : il range la réduction de la taille des classes au primaire "
        "parmi les politiques qui se remboursent d'elles-mêmes, et recommande "
        "de consacrer la baisse démographique à l'amplifier, en éducation "
        "prioritaire d'abord (" + _source("cae_taille_classes") + "). Notre "
        "programme fait un autre choix — la rémunération des enseignants — "
        "et laisse chaque établissement décider de ses dédoublements sur sa "
        "dotation. C'est un désaccord, et nous le signalons plutôt que de le "
        "taire.</p>"
    )

    corps += "<h2 id=\"qui-paie\">Qui paie, et pour qui</h2>"
    corps += g.tableau(
        "Les financeurs de la dépense d'éducation, en 2024 (DEPP)",
        ("Financeur", "Part"),
        (
            ("État", v("die_etat")),
            ("Collectivités territoriales", v("die_collectivites")),
            ("Entreprises", v("die_entreprises")),
            ("Ménages", v("die_menages")),
            ("Autres administrations publiques", v("die_autres_apu")),
        ),
    )
    corps += (
        f"<p>L'État verse {v('die_etat')} du total, essentiellement en "
        "salaires. Les collectivités en portent "
        f"{v('die_collectivites')} : les communes pour les écoles, les "
        "départements pour les collèges, les régions pour les lycées. Ce "
        "partage a une conséquence directe sur la proposition de ce site — "
        "<strong>le financement à l'élève doit être organisé à ces trois "
        "niveaux à la fois</strong>, faute de quoi il ne financerait que les "
        "salaires et laisserait les murs hors du dispositif.</p>"
        f"<p>Les ménages, eux, paient {v('die_menages')} de la dépense "
        "d'éducation : fournitures, cantine, transport, soutien scolaire. "
        "C'est moins qu'ailleurs : de l'élémentaire au post-secondaire, les "
        f"pouvoirs publics assurent en France {v('part_publique')} du "
        f"financement, contre {v('part_publique_ocde')} en moyenne dans "
        "l'OCDE.</p>"
    )

    corps += "<h2 id=\"rendement\">Ce que les grandes réformes ont rendu</h2>"
    corps += (
        "<p>Deux réformes récentes ont engagé des moyens considérables. "
        "Toutes deux ont été évaluées, et leur bilan est en deçà de ce "
        "qu'elles annonçaient. Il faut le dire même quand on approuvait leur "
        "intention — et dire aussi ce qui, dans ces évaluations, gêne notre "
        "argumentation.</p>"
    )
    corps += g.sections_depliables((
        ("Le dédoublement des classes de CP et CE1 en éducation prioritaire",
         "<p>Engagé en 2017, le dédoublement a ramené les classes de CP puis "
         "de CE1 en REP et REP+ à une douzaine d'élèves, avant d'être étendu "
         "à la grande section. Son coût est estimé à "
         f"{v('dedoublement_cout')} par la Cour des comptes, pour "
         f"{v('dedoublement_etp')} équivalents temps plein.</p>"
         "<p>L'évaluation de la DEPP mesure un effet positif en CP, surtout "
         "en mathématiques ; <strong>au CE1, la progression des élèves ne se "
         "distingue plus</strong> de celle d'élèves comparables ("
         + _source("dedoublement_depp") + "). Ce bilan divise les "
         "économistes : le Conseil d'analyse économique, s'appuyant sur "
         "l'effet mesuré en CP et sur les gains de long terme observés à "
         "l'étranger, juge la réduction de la taille des classes au primaire "
         "rentable pour la collectivité. Nous "
         "en tirons une leçon plus étroite : une mesure uniforme, attachée à "
         "un zonage et décidée au centre, coûte cher pour un effet modeste, "
         "et serait mieux décidée par chaque école, là où elle sert.</p>"),
        ("Les groupes de niveau puis de besoins au collège",
         "<p>Annoncés en 2023 sous le nom de « choc des savoirs », mis en "
         "place à la rentrée 2024 en sixième et cinquième, les groupes de "
         "besoins en français et en mathématiques devaient relever le niveau "
         "par un enseignement différencié.</p>"
         "<p>L'inspection générale a évalué le dispositif dans trente-neuf "
         "collèges de huit académies. Son rapport de juin 2025 conclut que "
         "la mesure n'a pas bénéficié aux élèves les plus fragiles, que la "
         "mobilité entre groupes est restée faible, et qu'elle risque de "
         "<strong>creuser les écarts</strong> en isolant les élèves en "
         "difficulté dans des groupes peu adaptés. Il relève aussi un gain "
         "réel, et qu'il faut citer parce qu'il gêne une partie de notre "
         "argumentation : la baisse du nombre d'élèves par groupe. Sa "
         "recommandation est d'abandonner le caractère systématique du "
         "dispositif et de rendre aux établissements une autonomie réelle ("
         + _source("igesr_groupes") + ").</p>"
         "<p>L'obligation a été levée par le "
         + _source("decret_groupes")
         + ", qui lui substitue un « accompagnement pédagogique renforcé » "
         "applicable à la rentrée 2026 — après deux années de réorganisation "
         "des emplois du temps de tous les collèges de France.</p>"
         "<p>La leçon n'est pas que la mesure était mauvaise. C'est qu'un "
         "dispositif uniforme, décidé au centre et imposé à tous les "
         "collèges de France, qui n'ont ni les mêmes élèves ni les mêmes "
         "équipes, ne "
         "peut pas produire autre chose qu'une moyenne nulle.</p>"),
    ))

    corps += "<h2 id=\"demographie\">La marge de manœuvre qui vient</h2>"
    corps += (
        f"<p>Les projections du ministère annoncent {v('demographie')} d'ici "
        "2035. À dépense constante, cela signifie mécaniquement un "
        "desserrement considérable : davantage d'adultes par enfant, sans "
        "un euro de plus — ou, si l'on garde la dépense par élève, "
        f"{ch.euros(-ch.montant(ch.poste('dividende')))} d'économie par an "
        "pour l'État.</p>"
        "<p>Cette économie n'a rien d'automatique : elle suppose que les "
        "emplois suivent les élèves. À taux d'encadrement constant, c'est "
        f"environ {ch.milliers(ch.postes_non_remplaces())} postes "
        "d'enseignants de moins qu'aujourd'hui en 2035, par départs non "
        "remplacés. Le précédent le plus récent dit la difficulté : en "
        "janvier 2025, le gouvernement a renoncé à la suppression de "
        f"{v('postes_2025')} d'enseignants prévue au budget.</p>"
        "<p>Cette baisse est une occasion, et elle ne se représentera pas. "
        "Deux usages en sont possibles. Le premier est de ne rien décider et "
        "de laisser l'économie se faire silencieusement, poste par poste, au "
        "gré des lois de finances. Le second est de décider ce qu'on en fait : "
        "<strong class=\"cle-texte\">relever la rémunération des enseignants "
        "et financer la liberté de choix</strong>. C'est le choix de ce "
        "programme : la baisse démographique paie la revalorisation, et le "
        "reste se finance en redistribuant.</p>"
    )
    corps += g.note(
        "<p><strong>Notre proposition tient dans la dépense d'aujourd'hui "
        "— parce que nous l'avons corrigée.</strong> Telle que nous l'avions "
        "d'abord écrite, elle coûtait "
        f"{ch.euros(ch.solde_initial())} de plus par an. La baisse "
        "démographique libère "
        f"{ch.euros(-ch.montant(ch.poste('dividende')))} par an ; elle paie "
        "la revalorisation des enseignants. La majoration sociale est prise "
        "sur les autres élèves, et l'écart de financement entre le privé et "
        "le public n'est comblé qu'au cinquième. Solde en 2035 : "
        f"{ch.euros(ch.solde(), True)} par an ; revalorisé de l'inflation "
        "depuis 2021, "
        f"{ch.euros(ch.solde() + ch.surcout_inflation(), True)}, et c'est "
        "alors la règle de sauvegarde qui tient l'enveloppe. Le détail, "
        "poste par poste, "
        f'et le nom de ceux qui paient, sont sur la page <a href="'
        f'{g.lien("chiffrage")}">Chiffrage</a>.</p>',
        "vigilance",
    )
    return corps


def gouvernance() -> str:
    corps = g.affiche(
        "Le constat · 3",
        "Personne ne décide, donc personne ne répond.",
        "Dans l'école française, celui qui dirige un établissement ne choisit "
        "ni son équipe, ni son budget, ni ses méthodes — et l'on s'étonne "
        "qu'il ne réponde pas des résultats.",
    )

    corps += g.plan((
        ("centralisation", "La centralisation"),
        ("recrutement", "Le recrutement"),
        ("affectation", "L'affectation des élèves"),
        ("prive", "Le privé sous contrat"),
        ("enseignants", "Le métier"),
    ))

    corps += g.reperes((
        g.Repere("Décisions prises au centre", v("decisions_central"),
                 f"dans un collège public français, contre "
                 f"{v('decisions_central_ocde')} en moyenne dans l'OCDE."),
        g.Repere("Décisions prises à l'école", v("decisions_etablissement"),
                 f"dont {v('decisions_pleine_autonomie')} seulement en "
                 "pleine autonomie."),
        g.Repere("Chefs qui recrutent", v("recrutement_france"),
                 f"des élèves, contre {v('recrutement_ocde')} dans l'OCDE et "
                 f"{v('estonie_recrutement')} en Estonie."),
    ))

    corps += ("<h2 id=\"centralisation\">L'un des systèmes les plus centralisés "
              "de l'OCDE</h2>")
    corps += (
        f"<p>{v('decisions_central')} des décisions qui concernent un collège "
        "public français se prennent au niveau de l'État central. La moyenne "
        f"de l'OCDE est de {v('decisions_central_ocde')}. À l'autre bout de "
        f"la chaîne, {v('decisions_etablissement')} des décisions se prennent "
        "dans l'établissement — et sur ces dix points, deux seulement "
        "s'exercent en pleine autonomie ; le reste s'applique dans un cadre "
        "fixé plus haut. Ce n'est pas un record : l'Espagne, la Suisse, la "
        "Grèce, la Turquie et la Finlande laissent moins encore à leurs "
        "établissements (" + _source("ocde_decentralisation") + ").</p>"
        "<p>Ce n'est pas une anomalie administrative : c'est le principe "
        "d'organisation. Les programmes, les horaires, les méthodes "
        "recommandées, le recrutement, l'affectation, l'avancement, la "
        "répartition des moyens sont décidés par l'administration centrale "
        "ou académique. L'établissement exécute.</p>"
        "<p>Il n'en résulte pas de l'uniformité : les écarts de résultats "
        "entre établissements français sont importants. Il en résulte une "
        "uniformité des <em>moyens d'agir</em> — quand un établissement va "
        "mal, ceux qui y travaillent ne disposent d'aucun des leviers qui "
        "permettraient d'y remédier.</p>"
        "<p>Nous ne lui faisons pas porter la chute récente des résultats en "
        "mathématiques à quinze ans : la centralisation est ancienne, et "
        "cette chute date de 2018. Ce qu'elle "
        "explique, c'est qu'un établissement qui décroche n'a aucun moyen de "
        "se redresser par lui-même.</p>"
    )

    corps += "<h2 id=\"recrutement\">Un chef d'établissement qui ne choisit personne</h2>"
    corps += (
        f"<p>En France, {v('recrutement_france')} des élèves fréquentent un "
        "établissement dont le chef a la responsabilité principale du "
        f"recrutement des enseignants. La moyenne de l'OCDE est de "
        f"{v('recrutement_ocde')}. En Estonie, en tête de l'Europe aux "
        f"épreuves PISA avec la Suisse, c'est {v('estonie_recrutement')}.</p>"
        "<p>Les enseignants français sont affectés par un barème national "
        "fondé sur l'ancienneté et la situation familiale. Le barème est "
        "impartial, et c'est sa vertu. Sa conséquence est qu'un collège "
        "difficile reçoit statistiquement les enseignants les moins "
        "expérimentés — ceux qui n'ont pas encore les points pour partir — "
        "et les voit partir dès qu'ils les ont. <strong "
        "class=\"cle-texte\">Nous envoyons nos débutants là où il faudrait "
        "nos meilleurs, et nous appelons cela l'égalité.</strong></p>"
    )
    corps += g.tableau(
        "Qui recrute les enseignants : part des élèves dont le chef "
        "d'établissement en a la responsabilité principale (PISA 2022)",
        ("Pays", "Part des élèves"),
        (
            ("France", v("recrutement_france")),
            ("Moyenne OCDE", v("recrutement_ocde")),
            ("Pays-Bas", v("recrutement_paysbas")),
            ("Royaume-Uni", v("recrutement_royaume_uni")),
            ("Estonie", v("estonie_recrutement")),
        ),
    )

    corps += "<h2 id=\"affectation\">L'adresse décide de l'école</h2>"
    corps += (
        "<p>Un élève français est affecté, en principe, à l'établissement "
        "public de son secteur. La dérogation existe, mais elle est accordée "
        "selon des critères et des capacités que la famille ne connaît pas à "
        "l'avance. Le résultat est un marché immobilier qui intègre la "
        "qualité des établissements dans le prix du mètre carré : "
        "<strong>la carte scolaire n'a pas supprimé le choix de l'école, elle "
        "l'a rendu payant</strong>.</p>"
        "<p>Ceux qui peuvent déménager choisissent. Ceux qui peuvent payer "
        "une scolarité privée choisissent. Les autres subissent. C'est "
        "exactement l'inégalité que la carte scolaire prétend empêcher, "
        "obtenue par le dispositif censé l'empêcher.</p>"
    )

    corps += "<h2 id=\"prive\">Un privé plafonné, et presque entièrement confessionnel</h2>"
    corps += (
        f"<p>Le privé sous contrat scolarise {v('prive_premier_degre')} des "
        f"élèves du premier degré et {v('prive_second_degre')} de ceux du "
        "second degré. Ses enseignants sont rémunérés par l'État ; ses "
        "établissements suivent les programmes nationaux.</p>"
        f"<p>Mais {v('prive_catholique')} des établissements privés sous "
        "contrat relèvent de l'enseignement catholique. Ce n'est pas un "
        "reproche fait à ces établissements : c'est le constat que <strong "
        "class=\"cle-texte\">la liberté scolaire française se réduit, en "
        "pratique, au choix entre l'école publique de son quartier et une "
        "école confessionnelle</strong> — quand il y a de la place, et quand "
        "la famille peut payer le reste à charge.</p>"
        "<p>La raison est dans le droit : le nombre de contrats est contingenté "
        "par l'enveloppe budgétaire, et l'ouverture d'une classe sous contrat "
        "dépend d'une décision administrative. Une école nouvelle, laïque, "
        "pédagogiquement différente, n'a pratiquement aucune chance d'être "
        "financée. La liberté d'enseignement existe ; la liberté de la "
        "financer, non.</p>"
        "<p>Le privé sous contrat est aussi de plus en plus marqué "
        "socialement : la part des élèves de familles très favorisées y "
        f"est passée de {v('prive_tres_favorises_2000')} en 2000 à "
        f"{v('prive_tres_favorises')} en 2021, selon la Cour des comptes. "
        "Financer davantage le privé sans rien exiger en retour aggraverait "
        "ce tri ; c'est pourquoi notre programme conditionne tout "
        "financement à l'accueil sans sélection, le rend gratuit pour les "
        "familles modestes et majore la dotation de l'élève défavorisé.</p>"
    )

    corps += "<h2 id=\"enseignants\">Un métier qu'on n'a pas les moyens de rendre attractif</h2>"
    corps += (
        "<p>Les enseignants français sont, rapportés aux autres diplômés du "
        "supérieur de leur pays, parmi les moins bien payés de l'OCDE : leur "
        f"salaire effectif est inférieur de {v('salaire_ecart_elementaire')} "
        "à celui des autres diplômés dans l'élémentaire et de "
        f"{v('salaire_ecart_college')} au collège, contre respectivement "
        f"{v('salaire_ecart_elementaire_ocde')} et "
        f"{v('salaire_ecart_college_ocde')} en moyenne dans l'OCDE. Et "
        "le retard s'accroît : entre 2015 et 2024, les salaires de début de "
        f"carrière ont augmenté de {v('salaire_debut_hausse')} en France, "
        f"contre {v('salaire_debut_hausse_ocde')} en moyenne dans l'OCDE à "
        "l'école élémentaire.</p>"
        "<p>Leurs élèves, eux, passent plus d'heures en classe qu'ailleurs : "
        f"{v('heures_elementaire')} d'instruction obligatoire par an dans "
        f"l'élémentaire contre {v('heures_elementaire_ocde')} en moyenne, "
        f"{v('heures_college')} au collège contre {v('heures_college_ocde')}. "
        "Et les classes sont plus chargées : "
        f"{v('taille_classe')} en moyenne à l'école élémentaire, un peu plus "
        f"que la moyenne de l'OCDE ; {v('taille_classe_college')} au collège, "
        "contre "
        f"{v('taille_classe_college_ue')} dans les autres pays de "
        "l'Union.</p>"
        "<p>Des classes plus chargées, un salaire relatif plus bas, et qui "
        "progresse moins qu'ailleurs : la crise de recrutement n'a rien de "
        "mystérieux. Aucune réforme de l'école ne réussira contre ses "
        "enseignants, et aucune ne réussira sans les payer.</p>"
    )
    corps += g.encadre(
        "<h3 class=\"serif\">Le nœud de tout le reste</h3>"
        f"<p>{v('enseignants_public')} enseignants exercent dans le public et "
        f"{v('enseignants_prive')} dans le privé sous contrat, pour "
        f"{v('eleves_premier_degre')} d'élèves du premier degré et "
        f"{v('eleves_second_degre')} du second. Aucun de ces adultes n'a été "
        "choisi par l'établissement où il travaille ; presque aucun n'y a de "
        "perspective d'évolution qui dépende de ce qu'il y fait. "
        "<strong class=\"cle-texte\">Rendre le métier désirable et rendre "
        "l'établissement responsable sont la même réforme.</strong></p>"
    )
    return corps


# -- la proposition ----------------------------------------------------------


def proposition() -> str:
    corps = g.affiche(
        "La proposition",
        "Le financement suit l'élève. L'école s'administre. Les résultats se publient.",
        "Sept réformes, chiffrées une par une. Aucune n'est nouvelle : "
        "chacune est appliquée quelque part en Europe, et l'on sait donc à "
        "quoi s'attendre — <strong class=\"cle-texte\">y compris quand cela "
        "tourne mal</strong>.",
    )

    corps += g.plan((
        ("financement", "1. Le financement à l'élève"),
        ("ponderation", "2. La pondération sociale"),
        ("autonomie", "3. L'autonomie de l'établissement"),
        ("contrat", "4. Le contrat unique"),
        ("evaluation", "5. L'évaluation publique"),
        ("metier", "6. Le métier d'enseignant"),
        ("socle", "7. Le socle"),
        ("calendrier", "Le calendrier"),
        ("garde-fous", "Les garde-fous"),
    ))

    corps += g.note(
        "<p><strong>La logique d'ensemble.</strong> Les sept réformes ne sont "
        "pas un catalogue : elles tiennent ensemble ou elles échouent. Le "
        "financement à l'élève sans pondération sociale produit de la "
        "ségrégation. L'autonomie sans évaluation produit de l'arbitraire. "
        "L'évaluation sans autonomie produit du découragement. "
        "<strong class=\"cle-texte\">Liberté de choix, liberté de gestion et "
        "reddition de comptes sont les trois pieds du même "
        "tabouret.</strong></p>",
        "resume",
    )

    corps += "<h2 id=\"financement\">1. Le financement public suit l'élève</h2>"
    corps += (
        "<p>Aujourd'hui, l'argent public va à des institutions : des postes "
        "sont affectés à des établissements, selon des barèmes de dotation "
        "horaire. Nous proposons qu'il aille à des élèves : "
        "<strong class=\"cle-texte\">un montant public attaché à chaque "
        "enfant, versé à l'établissement qui l'accueille</strong>, quel que "
        "soit son statut, dès lors qu'il respecte le contrat unique "
        "(réforme 4).</p>"
        "<p>Le montant de base est celui qui existe déjà : la dépense "
        "publique moyenne par élève du niveau considéré, État et "
        f"collectivités compris — de l'ordre de {v('public_eleve_1d')} dans "
        f"le premier degré et {v('public_eleve_2d')} dans le second. Pour "
        "l'élève du public, il n'y a pas d'argent nouveau : il y a un "
        "destinataire nouveau. Ce montant reprend la répartition actuelle "
        "entre les niveaux ; à lui seul, il ne déplace rien du lycée vers "
        "l'école.</p>"
        "<p>L'élève du privé sous contrat reçoit aujourd'hui "
        f"{v('prive_eleve_1d')} d'argent public à l'école contre "
        f"{v('public_eleve_1d')} dans le public. Combler tout l'écart "
        "coûterait "
        f"{ch.euros(ch.montant(ch.poste('alignement_prive'), forcees={'part_ecart_prive': 1.0}))} "
        "par an, plus que la baisse démographique ne libère. <strong>Nous "
        "en comblons un cinquième</strong>, soit "
        f"{ch.euros(ch.montant(ch.poste('alignement_prive')))} par an. "
        "L'établissement peut demander aux familles une contribution, "
        "plafonnée à l'écart restant et nulle pour les familles modestes : "
        "le choix ne dépend plus du revenu pour ceux qui n'en ont pas. Le "
        f'détail est dans le <a href="{g.lien("chiffrage")}">chiffrage</a>.'
        "</p>"
        "<p>Parce que l'État, les départements, les régions et les communes "
        f"financent ensemble l'école — respectivement {v('die_etat')} et "
        f"{v('die_collectivites')} de la dépense —, la dotation doit être "
        "consolidée entre ces niveaux, murs compris. Une dotation qui ne "
        "porterait que les salaires laisserait le bâti hors du dispositif et "
        "rendrait toute ouverture d'école impossible.</p>"
    )

    corps += "<h2 id=\"ponderation\">2. L'élève difficile rapporte plus</h2>"
    corps += (
        "<p>C'est la réforme la plus importante de cette page, et celle qui "
        "distingue cette proposition d'un simple chèque éducation.</p>"
        "<p>Le montant attaché à l'élève est <strong>pondéré</strong> : "
        "majoré d'environ 40 % pour un élève d'origine défavorisée, et d'un "
        "montant calculé pour un élève en situation de handicap ou "
        "allophone. Un établissement a alors un intérêt financier direct à "
        "accueillir les élèves que le système actuel se renvoie, et à les "
        "faire progresser — puisque l'évaluation (réforme 5) mesure la "
        "valeur ajoutée et non le niveau brut.</p>"
        "<p>Cette majoration n'est pas de l'argent nouveau. Elle remplace "
        "l'éducation prioritaire, et le surplus est pris sur le montant de "
        "base des autres élèves, qui baisse de "
        f"{ch.pourcent(ch.baisse_autres_eleves())}. Un établissement qui "
        "n'accueille que des enfants favorisés reçoit donc un peu moins "
        "qu'aujourd'hui par élève ; c'est voulu.</p>"
        "<p>Sans cette pondération, la liberté de choix organise le tri. "
        f"C'est ce qui s'est produit en Suède après {v('suede_reforme')}, et "
        "nous ne demandons à personne de nous croire sur parole : "
        f'la page <a href="{g.lien("comparaisons")}">Ailleurs en Europe</a> '
        "raconte cet échec en détail, parce que c'est de lui que ce "
        "programme tire ses garde-fous.</p>"
    )

    corps += "<h2 id=\"autonomie\">3. L'établissement s'administre</h2>"
    corps += (
        "<p>Chaque établissement, public comme privé sous contrat, reçoit une "
        "dotation globale — la somme des montants de ses élèves — et en "
        "décide l'emploi : <strong>recrutement de son équipe, organisation "
        "du temps scolaire, choix des méthodes, répartition entre postes et "
        "équipements</strong>.</p>"
    )
    corps += g.leviers((
        "<strong>Recrutement.</strong> Le chef d'établissement recrute ses "
        "enseignants sur des postes ouverts, parmi les candidats titulaires "
        f"du concours. Nous passons de {v('recrutement_france')} des élèves "
        "concernés à la totalité, quand la moyenne de l'OCDE est de "
        f"{v('recrutement_ocde')} et l'Estonie à {v('estonie_recrutement')}.",
        "<strong>Budget.</strong> La dotation est globale et fongible, avec "
        "publication annuelle des comptes de l'établissement.",
        "<strong>Pédagogie.</strong> Les programmes nationaux fixent ce qui "
        "doit être su (réforme 7) ; les méthodes pour y parvenir relèvent de "
        "l'équipe.",
        "<strong>Organisation.</strong> Rythmes, groupes, soutien, "
        "dédoublements ciblés : l'établissement décide, et rend compte de ce "
        "qu'il obtient.",
    ))
    corps += (
        "<p>L'autonomie n'est pas une croyance : l'OCDE observe qu'elle "
        "n'améliore les résultats que lorsqu'elle porte sur les personnels et "
        "la pédagogie, <em>et</em> qu'elle s'accompagne d'une évaluation "
        "externe. Une autonomie purement budgétaire ne produit rien. C'est "
        "pourquoi les réformes 3 et 5 ne se séparent pas.</p>"
        "<p>Le recrutement par l'établissement, lui, reste un pari : la "
        "recherche ne converge pas sur l'efficacité des politiques de "
        "recrutement des enseignants (" + _source("cae_recrutement") + "). "
        "C'est pourquoi il commence dans des académies volontaires, et qu'il "
        "est évalué avant d'être étendu.</p>"
    )

    corps += "<h2 id=\"contrat\">4. Un contrat unique, ouvert à tous</h2>"
    corps += (
        "<p>Le régime actuel distingue le public, le privé sous contrat "
        "d'association, le privé sous contrat simple et le hors contrat, avec "
        "des règles de financement différentes et un nombre de contrats "
        "contingenté par l'enveloppe budgétaire. Nous proposons un seul "
        "contrat, ouvert à tout établissement qui accepte quatre "
        "obligations :</p>"
    )
    corps += g.gestes((
        "<strong>Enseigner le socle</strong> — les programmes nationaux de "
        "français, de mathématiques et d'instruction civique, dans leur "
        "totalité.",
        "<strong>Accueillir sans sélectionner</strong> — aucune sélection à "
        "l'entrée sur dossier ni entretien ; une contribution des familles "
        "plafonnée à l'écart de financement avec le public, et nulle pour "
        "les familles modestes ; l'affectation passe par la procédure "
        "publique de la réforme 5.",
        "<strong>Passer les évaluations nationales</strong> et en publier les "
        "résultats, y compris la valeur ajoutée.",
        "<strong>Ouvrir ses comptes</strong> — financement, rémunérations, "
        "excédents. Un établissement financé par l'impôt rend publics ses "
        "comptes.",
    ))
    corps += (
        f"<p>Qui tient ce contrat est financé. Aujourd'hui, "
        f"{v('prive_catholique')} des établissements privés sous contrat sont "
        "catholiques, non parce que les familles n'en voudraient pas "
        "d'autres, mais parce qu'eux seuls étaient là quand les contrats ont "
        "été distribués. <strong class=\"cle-texte\">Nous ouvrons le contrat "
        "à qui remplit les conditions, sans plafond de nombre et sans "
        "préférence de statut.</strong></p>"
        "<p>Le hors contrat continue d'exister — la liberté d'enseignement "
        "est constitutionnelle — mais sans financement public, et sous le "
        "même contrôle de l'instruction qu'aujourd'hui.</p>"
    )

    corps += "<h2 id=\"evaluation\">5. Tout se publie, et l'affectation est écrite</h2>"
    corps += (
        "<p>La contrepartie de la liberté est la transparence, et elle doit "
        "être organisée avec soin : <strong>un palmarès brut est nuisible</strong>, "
        "parce qu'il mesure surtout le public recruté et récompense donc la "
        "sélection. Ce que nous publions est autre chose :</p>"
    )
    corps += g.leviers((
        "<strong>La valeur ajoutée</strong> de chaque établissement : la "
        "progression de ses élèves entre deux évaluations nationales, à "
        "caractéristiques d'entrée comparables. C'est la seule mesure qui "
        "récompense l'école qui fait progresser plutôt que celle qui "
        "sélectionne. Elle existe déjà pour les lycées et les collèges, "
        "calculée sur le baccalauréat et le brevet ("
        + _source("ivac") + ") ; il s'agit de l'étendre aux écoles et aux "
        "évaluations nationales.",
        "<strong>Les moyens</strong> : dotation reçue, taux d'encadrement, "
        "ancienneté moyenne de l'équipe, taux de rotation des enseignants.",
        "<strong>Les comptes</strong>, en données ouvertes et réutilisables.",
        "<strong>Les règles d'affectation</strong> : les familles classent "
        "leurs vœux, une procédure publique attribue les places selon des "
        "critères écrits — fratrie, proximité, pondération sociale — et "
        "tranche par tirage au sort en cas de sur-demande. L'établissement ne "
        "choisit jamais ses élèves.",
    ))
    corps += (
        "<p>Les évaluations nationales sont corrigées hors de l'établissement "
        "qui les fait passer. Cette précaution technique est essentielle : "
        "c'est l'absence d'une telle règle qui a produit l'inflation des "
        "notes en Suède, où les écoles avaient intérêt à noter "
        "généreusement pour attirer des élèves.</p>"
    )

    corps += "<h2 id=\"metier\">6. Le métier d'enseignant redevient un métier</h2>"
    corps += (
        "<p>Rien de ce qui précède ne fonctionne si l'on ne peut pas recruter "
        "d'enseignants. Or leur salaire effectif est inférieur de "
        f"{v('salaire_ecart_elementaire')} à celui des autres diplômés du "
        "supérieur dans l'élémentaire, contre "
        f"{v('salaire_ecart_elementaire_ocde')} en moyenne dans l'OCDE.</p>"
    )
    corps += g.leviers((
        "<strong>Une revalorisation financée par la démographie.</strong> Le "
        f"système scolaire comptera {v('demographie')} d'ici 2035. Nous "
        "proposons d'affecter l'essentiel de la dépense ainsi libérée à la "
        "rémunération, au lieu de la laisser s'évaporer en économies "
        "budgétaires annuelles.",
        "<strong>Un recrutement par l'établissement</strong>, sur un poste "
        "identifié, avec un projet — et non une affectation par barème de "
        "points.",
        "<strong>Une rémunération différenciée</strong> : surcroît significatif "
        "et durable pour enseigner dans les établissements difficiles, "
        "décidé par l'établissement dans sa dotation, et non par une prime "
        "nationale uniforme.",
        "<strong>Une liberté pédagogique réelle</strong> : l'équipe répond de "
        "ce que ses élèves apprennent, pas de la conformité de ses méthodes "
        "à une circulaire.",
    ))
    corps += g.note(
        "<p><strong>Ce que cela implique, et que nous assumons.</strong> Un "
        "recrutement par l'établissement est incompatible avec l'affectation "
        "nationale par barème. Les enseignants déjà en poste conservent leur "
        "statut, leur ancienneté et leur garantie d'emploi ; le nouveau "
        "régime s'applique aux recrutements à venir et, sur option, à ceux "
        "qui le demandent. Une réforme qui prétendrait changer du jour au "
        f"lendemain le statut des {v('enseignants_public')} enseignants du "
        f"public et des {v('enseignants_prive')} du privé sous contrat n'est "
        "pas une réforme : c'est un slogan.</p>",
        "vigilance",
    )

    corps += "<h2 id=\"socle\">7. Un socle resserré, et exigeant</h2>"
    corps += (
        "<p>Si les établissements choisissent leurs méthodes, l'État doit "
        "être d'autant plus clair sur ce qui doit être su. Nous proposons de "
        "resserrer les programmes du primaire sur <strong>lire, écrire, "
        "compter, et se repérer dans le temps et l'espace</strong>, avec un "
        "niveau attendu défini année par année et vérifié par les "
        "évaluations nationales.</p>"
        "<p>Ce n'est ni une question d'heures, ni une question de place "
        "faite aux fondamentaux : la France enseigne déjà "
        f"{v('heures_elementaire')} par an dans l'élémentaire, contre "
        f"{v('heures_elementaire_ocde')} en moyenne dans l'OCDE, et en "
        f"consacre {v('fondamentaux')} à la lecture, à l'écriture, à la "
        f"littérature et aux mathématiques, contre {v('fondamentaux_ocde')}. "
        "Nous y passons "
        "plus de temps que la moyenne, et nous obtenons "
        f"{v('timss_cm1_maths')} en mathématiques en CM1. La contrainte n'est "
        "pas le temps disponible : c'est ce que les élèves en retirent — "
        "d'où un niveau attendu, défini et vérifié chaque année.</p>"
    )

    corps += "<h2 id=\"calendrier\">En quel ordre</h2>"
    corps += g.gestes((
        "<strong>Première année — la transparence.</strong> Publication des "
        "évaluations nationales en valeur ajoutée, des moyens et des comptes "
        "de chaque établissement. Rien d'autre. Cette étape ne coûte presque "
        "rien, ne retire rien à personne, et rend toutes les suivantes "
        "discutables sur pièces.",
        "<strong>Deuxième année — l'autonomie du public.</strong> Dotation "
        "globale et recrutement par l'établissement, d'abord sur les postes "
        "vacants et dans les académies volontaires.",
        "<strong>Troisième année — l'affectation.</strong> Procédure de vœux "
        "publique à la place de la sectorisation, à l'entrée en sixième "
        "d'abord.",
        "<strong>Quatrième année — le contrat unique</strong> et la "
        "pondération sociale du financement, appliqués ensemble : l'un sans "
        "l'autre serait la faute suédoise.",
        "<strong>En continu — la rémunération.</strong> La baisse "
        "démographique paie d'abord la revalorisation des enseignants ; ce "
        "qu'elle libère au-delà finance le rapprochement du privé et "
        "l'autonomie, et la loi de finances le documente. Si la démographie "
        "déçoit, la "
        "revalorisation et le rapprochement du privé ralentissent d'autant : "
        "le calendrier ne s'endette pas.",
    ))

    corps += "<h2 id=\"garde-fous\">Les quatre garde-fous, et pourquoi ils existent</h2>"
    corps += (
        "<p>La liberté scolaire a déjà été essayée en Europe, avec des "
        "résultats très différents selon la manière. Les quatre règles "
        "suivantes ne sont pas des concessions : ce sont les conditions "
        "auxquelles la réforme marche, tirées une par une de ce qui a "
        "échoué ailleurs.</p>"
    )
    corps += g.tableau(
        "Les garde-fous, et l'échec qu'ils évitent",
        ("Règle", "Ce qu'elle empêche"),
        (
            ("Aucune sélection à l'entrée d'un établissement financé",
             "L'écrémage : choisir ses élèves pour améliorer ses résultats "
             "sans rien améliorer."),
            ("Pondération sociale et de handicap du financement",
             "La concentration des élèves coûteux dans les établissements "
             "les plus pauvres."),
            ("Correction externe des évaluations nationales",
             "L'inflation des notes, quand noter généreusement devient un "
             "argument commercial."),
            ("Comptes publics, et excédents réinvestis dans l'école",
             "Le financement public d'une rente privée."),
        ),
        ("long", "long"),
    )
    corps += g.note(
        "<p>Ces quatre règles sont la réponse à l'objection la plus sérieuse "
        "qui nous soit faite. Nous ne prétendons pas qu'elles suffisent, ni "
        "qu'elles sont faciles à tenir. Nous disons qu'une proposition "
        "libérale qui ne les porterait pas serait une proposition "
        f'irresponsable. <a href="{g.lien("objections")}">Les objections, '
        "une par une</a>.</p>",
        "vigilance",
    )
    return corps


def comparaisons() -> str:
    corps = g.affiche(
        "La proposition · le précédent",
        "Ce que la liberté scolaire donne, en bien et en mal.",
        "Quatre pays européens ont, chacun à sa manière, séparé le "
        "financement de l'école de sa propriété, ou rendu l'école autonome. "
        "Aucun n'est un modèle à recopier, et la dernière enquête PISA l'a "
        "rappelé. Mais chacun dit quelque chose de précis sur ce qui marche "
        "et ce qui échoue — et c'est la Suède qui nous a le plus appris.",
    )

    corps += g.plan((
        ("paysbas", "Pays-Bas"),
        ("danemark", "Danemark"),
        ("estonie", "Estonie"),
        ("suede", "Suède"),
        ("lecons", "Les leçons"),
    ))

    corps += g.tableau(
        "Quatre systèmes, ce qu'ils font de l'argent public, et où ils en "
        "sont à PISA 2025",
        ("Pays", "Financement du non-public", "Sélection à l'entrée",
         "Résultat"),
        (
            ("Pays-Bas", "Intégral, constitutionnel depuis "
             + v("paysbas_article23"),
             "Une école confessionnelle peut exiger l'adhésion à ses "
             "convictions",
             "Au-dessus de la moyenne OCDE en mathématiques, en dessous en "
             "lecture ; écart social aussi marqué qu'en France"),
            ("Danemark", v("danemark_prive") + " des élèves, financés à "
             + v("danemark_financement"), "Encadrée",
             "Au niveau de la France en lecture"),
            ("Estonie", "Écoles publiques très autonomes",
             "Concours d'entrée dans les lycées les plus demandés",
             "En tête de l'Europe avec la Suisse ; " + v("estonie_sciences")
             + " en sciences"),
            ("Suède", "Intégral depuis " + v("suede_reforme") + ", y compris "
             "à but lucratif", "Files d'attente, de fait sélectives",
             "Ségrégation en hausse, notes gonflées ; au niveau de la France "
             "en mathématiques"),
        ),
        ("texte", "long", "long", "long"),
    )

    corps += "<h2 id=\"paysbas\">Pays-Bas : un siècle de liberté financée</h2>"
    corps += (
        f"<p>Depuis {v('paysbas_article23')}, l'article 23 de la Constitution "
        "néerlandaise garantit que toute association peut ouvrir une école et "
        "qu'elle sera financée aux mêmes conditions que l'école publique. "
        "La majorité des élèves néerlandais fréquentent une école non "
        "publique — confessionnelle, Montessori, Dalton, Jenaplan — "
        "entièrement financée par l'impôt.</p>"
        "<p>C'est le précédent le plus proche de notre proposition, et le "
        "plus long — plus d'un siècle, dans un pays qui n'a jamais cessé "
        "d'être un État social, où l'inspection publie ses rapports "
        "établissement par établissement. Il faut pourtant le décrire "
        "exactement, parce qu'on nous le rappellera. Une école "
        "confessionnelle néerlandaise peut exiger de ses élèves qu'ils "
        "adhèrent à ses convictions (" + _source("paysbas_admission") + "). "
        "Et ses résultats ne sont pas ceux d'un modèle : en 2025, les "
        "Pays-Bas sont au-dessus de la moyenne de l'OCDE en mathématiques, "
        "en dessous en compréhension de l'écrit, et à l'un de leurs plus bas "
        "niveaux historiques dans les trois domaines ("
        + _source("ocde_pisa_2025_paysbas") + ") ; l'écart entre élèves "
        f"favorisés et défavorisés y atteint {v('paysbas_ecart_sciences')} "
        f"en sciences — autant qu'en France ({v('pisa_ecart_sciences')}), "
        f"bien plus que la moyenne de l'OCDE ({v('pisa_ecart_sciences_ocde')})."
        "</p>"
        "<p>Ce que les Pays-Bas montrent, c'est qu'une liberté scolaire "
        "financée peut durer un siècle dans un État social. Ce qu'ils ne "
        "montrent pas, c'est qu'elle suffise à faire réussir les élèves, ni "
        "à réduire les inégalités. C'est pourquoi notre proposition ne leur "
        "emprunte pas le droit de choisir ses élèves.</p>"
    )

    corps += "<h2 id=\"danemark\">Danemark : l'école qu'on fonde soi-même</h2>"
    corps += (
        f"<p>{v('danemark_prive')} des élèves danois fréquentent une "
        "<em>friskole</em> ou une école privée. L'État en finance "
        f"{v('danemark_financement')} ; le reste est à la charge des "
        "familles, avec des barèmes sociaux. Un groupe de parents peut fonder une école et obtenir ce "
        "financement dès lors qu'il atteint un effectif minimal et se soumet "
        "au contrôle.</p>"
        "<p>Ce que le Danemark montre, c'est qu'une école n'a pas besoin "
        "d'être fondée par l'État pour être une école commune. Ce qu'il "
        "montre aussi : un reste à charge familial, même modeste, filtre. "
        "Nous aurions voulu financer à 100 % ; le chiffrage nous en empêche, "
        "et nous reprenons donc le barème social danois, en plus strict. "
        "<strong class=\"cle-texte\">La contribution est nulle pour les "
        "familles modestes, et plafonnée pour les autres</strong> : le choix "
        "ne dépend plus du revenu pour ceux qui n'en ont pas.</p>"
        "<p>Le Danemark n'est pas pour autant un modèle de résultats : en "
        "2025, son score en compréhension de l'écrit est au niveau de celui "
        "de la France (" + _source("depp_pisa_voisins") + ").</p>"
    )

    corps += "<h2 id=\"estonie\">Estonie : l'autonomie sans le marché</h2>"
    corps += (
        f"<p>L'Estonie obtenait {v('estonie_pisa')} en mathématiques aux "
        "épreuves PISA 2022, au troisième rang des pays de l'OCDE derrière "
        "le Japon et la Corée ; en 2025, elle reste, avec la Suisse, en tête "
        "de l'Europe en mathématiques (" + _source("depp_pisa_voisins")
        + "), et obtient " + v("estonie_sciences") + " en sciences, le "
        "deuxième score de l'OCDE. Sa dépense par élève est inférieure à la "
        "française, et son école très majoritairement publique.</p>"
        "<p>Un mot sur ce rang, parce que nous nous sommes imposé une règle "
        "et qu'elle vaut aussi contre nous : en 2022, l'Estonie devançait la "
        "Suisse de deux points, <strong>un écart inférieur à la marge "
        "d'erreur de l'enquête</strong>. Les deux pays ne sont pas "
        "départagés, et c'est le niveau estonien qui nous intéresse ici, "
        "non sa place sur un podium.</p>"
        f"<p>Ce qu'elle a, et que nous n'avons pas : {v('estonie_recrutement')} "
        "des élèves sont dans un établissement dont le directeur recrute "
        "lui-même son équipe et répartit lui-même son enveloppe. Le cadre "
        "national dit ce qui doit être appris ; l'école décide comment, et "
        "répond des résultats. Elle n'ignore pas pour autant la sélection : "
        "les lycées les plus demandés de Tallinn recrutent sur concours "
        "d'entrée, à la fin de l'école de base ("
        + _source("tallinn_concours") + ").</p>"
        "<p>C'est le contre-exemple utile à notre propre camp. Rien n'isole "
        "la part de l'autonomie dans les résultats estoniens, et nous ne "
        "prétendons pas le faire ; mais <strong>l'Estonie obtient, avec la "
        "Suisse, les meilleurs résultats d'Europe avec une école presque "
        "entièrement "
        "publique, où chaque établissement recrute et répond de ses "
        "résultats</strong>. C'est pourquoi la réforme 3 de notre "
        "proposition compte, à nos yeux, davantage que la réforme 1 — et "
        "c'est elle que le calendrier engage en premier, après la "
        "transparence.</p>"
    )

    corps += "<h2 id=\"suede\">Suède : le précédent dont nous tirons nos règles</h2>"
    corps += (
        f"<p>En {v('suede_reforme')}, la Suède ouvre le financement public à "
        "l'élève — la <em>skolpeng</em> — à des établissements privés, y "
        "compris à but lucratif, avec très peu de contraintes. C'est la "
        "version de la liberté scolaire que nous ne proposons pas, et il "
        "faut dire pourquoi.</p>"
    )
    corps += g.leviers((
        "<strong>La ségrégation scolaire a augmenté</strong>, entre élèves "
        "d'origine immigrée et natifs, et selon le diplôme des parents. Les "
        "files d'attente, en apparence neutres, favorisent les familles "
        "informées et prévoyantes, et l'absence de pondération rendait "
        "l'élève difficile financièrement peu attractif.",
        "<strong>Les notes ont gonflé.</strong> Les établissements notant "
        "eux-mêmes leurs élèves, la générosité est devenue un argument "
        "commercial, et les notes se sont détachées des résultats mesurés en "
        "externe. C'est l'effet le moins contesté de la réforme.",
        "<strong>Les communes ont porté les coûts fixes</strong> pendant que "
        "la dotation partait avec l'élève : des écoles à demi vides et "
        "coûteuses, sans moyen de s'ajuster.",
        "<strong>Sur les résultats, la recherche est plus prudente que le "
        "débat public.</strong> Les travaux de l'IFAU, l'institut public "
        "suédois d'évaluation, concluent que la part de la hausse de "
        "ségrégation directement imputable au libre choix est modeste — la "
        "ségrégation résidentielle pesant davantage — et que l'effet du "
        "choix sur les résultats a été faiblement positif à court terme, "
        "quasi nul à long terme. La chute suédoise aux enquêtes "
        "internationales est donc réelle ; son attribution à la réforme "
        "scolaire, elle, reste discutée. En 2025, la Suède obtient en "
        "mathématiques un score comparable à celui de la France ("
        + _source("depp_pisa_voisins") + ").",
    ))
    corps += g.encadre(
        "<h3 class=\"serif\">Ce que nous en retenons, littéralement</h3>"
        "<p>Nos quatre garde-fous sont la transcription point par point de "
        "cet échec : <strong>pas de sélection à l'entrée</strong> (contre "
        "l'écrémage par file d'attente), <strong>pondération sociale du "
        "financement</strong> (pour que l'élève difficile soit recherché), "
        "<strong>correction externe des évaluations</strong> (contre "
        "l'inflation des notes), <strong>comptes publics et excédents "
        "réinvestis</strong> (contre la rente). Une proposition libérale qui "
        "ignorerait la Suède ne serait pas libérale : elle serait "
        "négligente.</p>"
    )

    corps += "<h2 id=\"lecons\">Trois leçons, et une réserve</h2>"
    corps += g.points((
        ("L'autonomie avant la concurrence",
         "L'Estonie figure, avec la Suisse, en tête de l'Europe avec une "
         "école presque entièrement publique, mais très autonome. C'est le "
         "levier le moins coûteux politiquement, et celui que nous engageons "
         "en premier."),
        ("La liberté exige des règles contre le tri",
         "Pays-Bas et Danemark financent largement le non-public depuis des "
         "décennies ; mais l'un laisse les écoles confessionnelles exiger "
         "l'adhésion à leurs convictions, l'autre laisse un reste à charge "
         "aux familles. D'où notre contrat unique : aucune sélection, et la "
         "gratuité pour les familles modestes."),
        ("La liberté ne suffit pas",
         "Ce qui distingue la liberté néerlandaise de la liberté suédoise, "
         "c'est ce qu'on exige en échange de l'argent public. Mais ni l'une "
         "ni l'autre n'a empêché la baisse de 2025, qui touche presque toute "
         "l'OCDE. La liberté scolaire est un cadre ; elle ne dispense pas "
         "de savoir ce qui fait apprendre."),
    ))
    corps += g.note(
        "<p><strong>La réserve.</strong> Aucun de ces pays n'a la taille, la "
        "diversité territoriale ni l'histoire scolaire de la France. Un "
        "dispositif qui fonctionne dans un pays de six millions d'habitants "
        "n'est pas transposable tel quel dans un pays qui scolarise "
        f"{v('eleves_premier_degre')} d'écoliers. Les comparaisons "
        "internationales indiquent des directions ; elles ne dispensent "
        "d'aucune expérimentation, ni d'aucune évaluation française.</p>",
        "vigilance",
    )
    return corps



def chiffrage() -> str:
    central = ch.solde()
    favorable = ch.solde("favorable")
    defavorable = ch.solde("defavorable")
    e = ch.euros

    corps = g.affiche(
        "La proposition · le chiffrage",
        "Ce que le programme coûte, et ce qu'il rapporte.",
        "Chaque réforme, chiffrée poste par poste par rapport à la situation "
        "actuelle, avec ses formules et ses hypothèses. Tel que nous "
        f"l'avions d'abord écrit, le programme coûtait {e(ch.solde_initial())} "
        "de plus par an. <strong class=\"cle-texte\">Nous l'avons ajusté pour "
        "qu'il tienne dans la dépense d'aujourd'hui</strong> — et nous disons "
        "à qui cet ajustement coûte.",
    )

    corps += g.reperes((
        g.Repere("Ce que le programme ajoute", e(ch.total("charge")),
                 "par an en 2035 : revalorisation, rapprochement du privé, "
                 "autonomie, évaluation."),
        g.Repere("Ce que la démographie et la réforme libèrent",
                 e(-ch.total("ressource")),
                 f"par an en 2035, dont l'essentiel vient de "
                 f"{v('demographie')}."),
        g.Repere("Le solde", e(central, True),
                 f"par an, entre {e(favorable, True)} et "
                 f"{e(defavorable, True)} selon les hypothèses."),
    ))

    corps += g.plan((
        ("regle", "La règle du chiffrage"),
        ("postes", "Poste par poste"),
        ("lectures", "Deux lectures du solde"),
        ("plus-moins", "Les + et les −"),
        ("gagnants", "Qui y gagne, qui y perd"),
        ("annees", "Année par année"),
        ("equilibre", "Comment il tient l'enveloppe"),
        ("hypotheses", "Les hypothèses"),
        ("depart", "Les chiffres de départ"),
        ("limites-chiffrage", "Ce que ce chiffrage ne fait pas"),
    ))

    corps += g.note(
        "<p><strong>Ce que ce chiffrage a changé au programme.</strong> "
        "Nous écrivions que le programme tenait « à enveloppe constante ». "
        "Le premier chiffrage a dit le contraire : la démographie libère "
        f"{e(-ch.montant(ch.poste('dividende')))} par an, et trois "
        "engagements pesaient davantage — aligner entièrement le financement "
        "public de l'élève du privé sur celui du public, majorer de 40 % "
        "celui de l'élève défavorisé, et ramener l'écart entre le salaire "
        "des enseignants et celui des autres diplômés à la moyenne de "
        "l'OCDE. Nous avons gardé les deux derniers, et "
        "réduit le premier. <strong class=\"cle-texte\">La majoration "
        "sociale est prise sur les autres élèves ; l'écart entre le privé "
        "et le public n'est comblé qu'au cinquième.</strong> Le détail et "
        f'les raisons sont <a href="#equilibre">plus bas</a>.</p>',
        "vigilance",
    )

    corps += "<h2 id=\"regle\">La règle de ce chiffrage</h2>"
    corps += g.leviers((
        "<strong>Le point de comparaison est la situation actuelle</strong>, "
        "en 2035 : l'année où la baisse des effectifs annoncée par la DEPP "
        "sera acquise, et où toutes les réformes du calendrier seront en "
        "place. Les montants sont annuels.",
        "<strong>Le signe est celui du solde public</strong> : un "
        "<span class=\"badge\">+</span> est une dépense de plus pour l'État "
        "ou les collectivités, un <span class=\"badge\">−</span> une "
        "dépense de moins.",
        "<strong>Les chiffres constatés sont ceux du registre</strong> du "
        "site, avec leur source : le calcul les lit, il ne les recopie pas. "
        "Les montants sont dans les euros de leurs années — 2021 pour la "
        "dépense par élève, 2026 pour le budget. Rien n'est revalorisé, ce "
        "qui sous-estime les coûts d'environ "
        f"{e(ch.surcout_inflation())} par an : le détail est "
        '<a href="#limites-chiffrage">plus bas</a>.',
        "<strong>Ce qui n'est pas constaté est une hypothèse</strong>, "
        "donnée avec une valeur favorable, centrale et défavorable, et sa "
        "raison. Le chiffre principal est celui du scénario central ; la "
        "fourchette, celle des deux autres.",
    ))

    corps += "<h2 id=\"postes\">Poste par poste</h2>"
    corps += g.tableau(
        "Effet annuel de chaque poste en 2035, par rapport à la situation "
        "actuelle (+ : dépense de plus ; − : dépense de moins)",
        ("Réforme", "Poste", "Aujourd'hui", "Avec le programme",
         "Effet central", "Fourchette"),
        tuple(
            (
                p.reforme,
                f"<strong>{g.echapper(p.intitule)}</strong><br>"
                f'<span class="discret">{g.echapper(p.formule)}</span>',
                g.echapper(p.actuel),
                g.echapper(p.programme),
                e(ch.montant(p), True),
                f"{e(ch.montant(p, 'favorable'), True)} à "
                f"{e(ch.montant(p, 'defavorable'), True)}",
            )
            for p in ch.postes("charge") + ch.postes("ressource")
        ),
        ("texte", "long", "long", "long", "nombre", "nombre"),
    )
    corps += g.tableau(
        "Le bilan annuel en 2035",
        ("", "Favorable", "Central", "Défavorable"),
        (
            ("Dépenses nouvelles",) + tuple(
                e(ch.total("charge", s), True) for s in ch.SCENARIOS),
            ("Dépenses évitées",) + tuple(
                e(ch.total("ressource", s), True) for s in ch.SCENARIOS),
            ("<strong>Solde</strong>",) + tuple(
                f"<strong>{e(ch.solde(s), True)}</strong>"
                for s in ch.SCENARIOS),
        ),
    )
    corps += (
        "<p>Un poste ne figure pas dans ce bilan parce qu'il ne change pas "
        "la dépense totale : il déplace de l'argent d'un élève à l'autre.</p>"
    )
    corps += g.tableau(
        "Le transfert entre élèves (sans effet sur le solde)",
        ("Réforme", "Poste", "Aujourd'hui", "Avec le programme",
         "Montant déplacé", "Fourchette"),
        tuple(
            (
                p.reforme,
                f"<strong>{g.echapper(p.intitule)}</strong><br>"
                f'<span class="discret">{g.echapper(p.formule)}</span>',
                g.echapper(p.actuel),
                g.echapper(p.programme),
                e(ch.montant(p)),
                f"{e(ch.montant(p, 'favorable'))} à "
                f"{e(ch.montant(p, 'defavorable'))}",
            )
            for p in ch.postes("transfert")
        ),
        ("texte", "long", "long", "long", "nombre", "nombre"),
    )
    corps += (
        "<p>Deux autres postes n'y figurent pas parce qu'ils ne durent pas. "
        "Ils sont comptés dans le tableau année par année.</p>"
    )
    corps += g.tableau(
        "Les coûts de transition, dus seulement pendant la mise en place "
        "(montant par année où ils sont dus)",
        ("Réforme", "Poste", "Pourquoi", "Effet central", "Fourchette"),
        tuple(
            (
                p.reforme,
                f"<strong>{g.echapper(p.intitule)}</strong><br>"
                f'<span class="discret">{g.echapper(p.formule)}</span>',
                g.echapper(p.programme),
                e(ch.montant(p), True),
                f"{e(ch.montant(p, 'favorable'), True)} à "
                f"{e(ch.montant(p, 'defavorable'), True)}",
            )
            for p in ch.postes("transition")
        ),
        ("texte", "long", "long", "nombre", "nombre"),
    )
    corps += (
        "<p>Deux réformes ne coûtent presque rien et n'ont pas de ligne. "
        "Le socle resserré (réforme 7) réécrit des programmes. Les "
        f"{v('groupes_postes')} des groupes de besoins, et les autres "
        "dispositifs nationaux, ne sont pas comptés comme des économies : "
        "leurs moyens restent dans la dotation des établissements, qui en "
        "décideront l'usage. La majoration pour le handicap reprend les "
        f"{v('aesh_credits')} des accompagnants, sans plus.</p>"
    )

    corps += "<h2 id=\"lectures\">Deux lectures du solde, et laquelle compte</h2>"
    corps += g.paire(
        "<h3>Par rapport au budget d'aujourd'hui</h3>"
        f"<p class=\"cle-texte\">{e(central, True)} par an</p>"
        "<p>C'est la question « faut-il plus d'argent que maintenant ? ». La "
        "baisse démographique est comptée comme une ressource du programme. "
        "La réponse est non dans le scénario central, et dans le favorable "
        f"({e(favorable, True)}) ; elle est oui dans le défavorable "
        f"({e(defavorable, True)}), et c'est à cela que sert la règle de "
        'sauvegarde décrite <a href="#equilibre">plus bas</a>.</p>',
        "<h3>Par rapport à ce que l'État dépenserait sans nous</h3>"
        f"<p class=\"cle-texte\">{e(ch.solde_tendanciel(), True)} par an</p>"
        "<p>Sans le programme, les classes se videraient et la dépense "
        "baisserait d'elle-même. Le programme dépense cette baisse au lieu "
        "de la rendre au contribuable. Pour les finances publiques, c'est le "
        "vrai coût : ce que l'on aurait pu économiser, et que l'on "
        "n'économise pas.</p>",
    )
    corps += (
        "<p>Nous tenons la seconde lecture pour la plus honnête, et c'est "
        "celle qu'un adversaire retiendra : le programme ne demande pas "
        "d'argent nouveau, mais il demande de renoncer à une économie. "
        "C'est un choix, et nous l'assumons : la baisse des effectifs est "
        "l'occasion de payer enfin les enseignants.</p>"
        "<p>Ce choix a une traduction en emplois, et nous la donnons. Le "
        "dividende démographique n'existe que si les postes suivent les "
        "élèves : enseignants du public et du privé sous contrat × baisse "
        "des effectifs × part de la dépense qui suit les effectifs, soit "
        f"<strong>environ {ch.milliers(ch.postes_non_remplaces())} postes "
        "d'enseignants de moins qu'aujourd'hui en 2035</strong> (de "
        f"{ch.milliers(ch.postes_non_remplaces('defavorable'))} à "
        f"{ch.milliers(ch.postes_non_remplaces('favorable'))} selon "
        "l'hypothèse), par départs non remplacés. Le taux d'encadrement ne "
        "baisse pas, mais il ne s'améliore pas non plus : le programme "
        "préfère payer mieux des enseignants moins nombreux plutôt "
        "qu'alléger les classes — l'inverse de ce que recommande le Conseil "
        "d'analyse économique (" + _source("cae_taille_classes") + "). Et "
        "la difficulté politique est réelle : en janvier 2025, le "
        f"gouvernement a renoncé à la suppression de {v('postes_2025')}.</p>"
    )

    corps += "<h2 id=\"plus-moins\">Les + et les − de chaque réforme</h2>"
    corps += g.tableau(
        "Ce que chaque réforme améliore et ce qu'elle dégrade ou coûte, par "
        "rapport à la situation actuelle",
        ("Réforme", "+ Ce qui s'améliore", "− Ce qui se dégrade, ou coûte"),
        (
            ("1. Le financement suit l'élève",
             "Le choix de l'école ne dépend plus de l'adresse ; les familles "
             "modestes ne paient plus rien dans le privé sous contrat ; une "
             "école nouvelle peut être financée.",
             f"{e(ch.montant(ch.poste('alignement_prive')))} par an ; les "
             "autres familles du privé continuent de payer une partie des "
             f"{v('prive_frais_familles')} de frais actuels ; des coûts "
             "fixes laissés dans les établissements quittés."),
            ("2. La majoration sociale",
             "L'élève défavorisé devient recherché au lieu d'être évité ; les "
             "moyens le suivent où qu'il aille, au lieu d'être attachés à un "
             "zonage.",
             f"{e(ch.montant(ch.poste('ponderation')))} par an pris sur le "
             "montant de base des autres élèves, qui baisse de "
             f"{ch.pourcent(ch.baisse_autres_eleves())} ; la fin du zonage "
             "retire aux écoles REP leurs classes dédoublées garanties : "
             "elles devront les payer sur leur dotation."),
            ("3. L'autonomie",
             "Le chef d'établissement choisit son équipe ; la fin du "
             "mouvement au barème libère des emplois de gestion ; les "
             "dispositifs uniformes cessent.",
             f"{e(ch.montant(ch.poste('gestion_ecoles')))} par an de gestionnaires pour les "
             "écoles, qui n'en ont pas ; un risque d'arbitraire local dans "
             "le recrutement ; la protection du barème disparaît pour les "
             "nouveaux enseignants."),
            ("4. Le contrat unique",
             "L'offre se diversifie au-delà de l'enseignement catholique ; "
             "le socle et l'accueil sans sélection deviennent opposables à "
             "tous les établissements financés.",
             f"{e(ch.montant(ch.poste('hors_contrat')))} par an pour les établissements "
             "hors contrat qui signeront ; un contrôle à organiser sur "
             "des milliers d'établissements nouveaux."),
            ("5. L'évaluation publique et l'affectation",
             "Les familles choisissent sur pièces ; l'école qui fait "
             "progresser est reconnue ; la dérogation opaque disparaît.",
             f"{e(ch.montant(ch.poste('evaluation')) + ch.montant(ch.poste('affectation')))} par "
             f"an ; et {e(ch.montant(ch.poste('transport')))} de transport pour les "
             "collectivités, faute de quoi le choix resterait réservé aux "
             "familles motorisées."),
            ("6. Le métier d'enseignant",
             "Un écart de salaire avec les autres diplômés ramené à la "
             f"moyenne de l'OCDE : {ch._HAUSSE_1D} à l'école, "
             f"{ch._HAUSSE_2D} au collège et au lycée ; un recrutement sur "
             "projet.",
             f"{e(ch.montant(ch.poste('revalorisation')))} par an, à comparer aux "
             f"{v('mesures_salariales')} de toutes les mesures salariales "
             "décidées depuis 2022 ; c'est la baisse démographique qui la "
             "finance, et l'État renonce donc à l'économiser."),
            ("7. Le socle",
             "Un niveau attendu, défini année par année et vérifié.",
             "Un coût négligeable ; une réécriture des programmes que "
             "chaque changement de majorité peut défaire."),
        ),
        ("texte", "long", "long"),
    )

    corps += "<h2 id=\"gagnants\">Qui y gagne, qui y perd</h2>"
    corps += g.tableau(
        "Effet du programme sur chaque acteur, par rapport à la situation "
        "actuelle",
        ("Acteur", "Effet", "Pourquoi"),
        (
            ("Les enseignants", "+",
             f"{e(ch.montant(ch.poste('revalorisation')))} de rémunération en plus par an. "
             "Ils perdent en revanche, pour les nouveaux recrutés, "
             "l'affectation au barème."),
            ("Les familles modestes du privé sous contrat", "+",
             "Elles ne paient plus de frais de scolarité."),
            ("Les autres familles du privé sous contrat", "+ ou =",
             "Leur contribution est plafonnée à l'écart restant entre le "
             "financement public de leur établissement et celui du public ; "
             "elle baisse d'autant que l'État se rapproche."),
            ("Les élèves défavorisés", "+",
             "Un financement majoré qui les suit, et des établissements qui "
             "ont intérêt à les accueillir."),
            ("Les familles du hors contrat", "+ ou =",
             "Financées si leur école signe le contrat ; inchangées sinon."),
            ("Les collectivités", "−",
             "Le transport des élèves qui choisissent plus loin, et une part "
             "des coûts fixes des établissements quittés."),
            ("Le contribuable", "=",
             "Pas un euro de plus qu'aujourd'hui : "
             f"{e(central, True)} par an dans le scénario central, et, une "
             "fois l'inflation prise en compte, "
             f"{e(central + ch.surcout_inflation(), True)} que la règle de "
             "sauvegarde ramène à zéro. Mais c'est "
             f"{e(ch.solde_tendanciel())} d'économies de moins que sans le "
             "programme."),
            ("Les établissements qui accueillent peu d'élèves défavorisés",
             "−",
             "Leur montant par élève baisse de "
             f"{ch.pourcent(ch.baisse_autres_eleves())} pour financer la "
             "majoration sociale. La baisse démographique, qui desserre "
             "leurs classes, en adoucit l'effet."),
        ),
        ("texte", "texte", "long"),
    )

    corps += "<h2 id=\"annees\">Année par année</h2>"
    corps += (
        "<p>Le calendrier de la proposition commence par ce qui ne coûte "
        "presque rien. Les premières années sont donc excédentaires : la "
        "baisse des effectifs libère plus que la transparence et "
        "l'autonomie ne coûtent. Le solde devient légèrement déficitaire de "
        "2031 à 2034, le temps de payer les coûts de transition du libre "
        "choix ; sur toute la période, le programme dégage "
        f"{e(-sum(l[4] for l in ch.trajectoire()))} au total.</p>"
    )
    corps += g.tableau(
        "Trajectoire annuelle, scénario central (les effectifs de 2035 sont "
        "appliqués à toutes les années, ce qui sous-estime un peu les "
        "premières)",
        ("Année", "Dépenses nouvelles", "Dépenses évitées", "Transition",
         "Solde"),
        tuple(
            (str(annee), e(charges, True), e(ressources, True),
             e(transition, True), f"<strong>{e(solde, True)}</strong>")
            for annee, charges, ressources, transition, solde
            in ch.trajectoire()
        ),
    )

    corps += "<h2 id=\"equilibre\">Comment le programme tient l'enveloppe, et à qui cela coûte</h2>"
    corps += (
        "<p>Le programme tel que nous l'avions écrit coûtait "
        f"{e(ch.solde_initial())} de plus par an. Pour le ramener à la "
        "dépense d'aujourd'hui, il fallait renoncer à quelque chose. Nous "
        "avons choisi selon ce que ce site établit lui-même, et non selon "
        "ce qui gêne le moins.</p>"
    )
    corps += g.gestes((
        "<strong>La majoration sociale reste à 40 %, et elle est prise sur "
        "les autres élèves.</strong> C'est la clé de voûte du programme — "
        "sans elle, la liberté de choix organise le tri, comme en Suède. "
        f"Elle déplace {e(ch.montant(ch.poste('ponderation')))} par an ; le "
        "montant de base des élèves qui n'y ouvrent pas droit baisse de "
        f"{ch.pourcent(ch.baisse_autres_eleves())}. C'est ce que « dépenser "
        "autrement » veut dire.",
        "<strong>La revalorisation des enseignants est entière.</strong> "
        "Aucune réforme ne réussira sans eux, et c'est le seul poste que la "
        "baisse démographique finance à elle seule : "
        f"{e(ch.montant(ch.poste('revalorisation')))} pour "
        f"{e(-ch.montant(ch.poste('dividende')))} libérés.",
        "<strong>L'écart entre le privé sous contrat et le public n'est "
        "comblé qu'au cinquième.</strong> L'alignement complet coûterait "
        f"{e(ch.montant(ch.poste('alignement_prive'), forcees={'part_ecart_prive': 1.0}))} "
        f"par an ; nous en finançons {e(ch.montant(ch.poste('alignement_prive')))}. "
        "Le reste peut être demandé aux familles, sous un plafond, et jamais "
        "aux familles modestes. C'est le renoncement que nous jugeons le "
        "moins grave, et ce site en donne la raison : l'Estonie, en tête de "
        "l'Europe avec la Suisse, a une école presque entièrement publique "
        "mais très autonome — ce qui suggère que l'autonomie compte "
        f'davantage que le libre choix (<a href="{g.lien("comparaisons")}'
        '#estonie">Ailleurs en Europe</a>).',
    ))
    corps += g.encadre(
        "<h3 class=\"serif\">La règle de sauvegarde</h3>"
        "<p>Le scénario central tient ; le défavorable laisse "
        f"{e(defavorable, True)} par an. Pour que la promesse tienne quelle "
        "que soit la démographie, <strong class=\"cle-texte\">le "
        "rapprochement du privé et la revalorisation n'avancent chaque année "
        "que de ce que la baisse des effectifs a effectivement "
        "libéré</strong>, constatée en loi de finances. Si la démographie "
        "déçoit, le calendrier ralentit ; il ne s'endette pas.</p>"
    )
    corps += (
        "<p>Nous avons écarté trois autres manières de tenir l'enveloppe. "
        "Chacune aurait rapporté quelque chose par rapport au programme "
        "initial ; aucune ne suffisait seule, et chacune sacrifiait ce que "
        "nous jugeons essentiel.</p>"
    )
    corps += g.tableau(
        "Les options écartées, ce qu'elles auraient rapporté, et pourquoi "
        "nous ne les retenons pas",
        ("Option", "Pourquoi nous l'écartons", "Ce qu'elle rapportait"),
        tuple((g.echapper(quoi), g.echapper(pourquoi), e(gain))
              for quoi, pourquoi, gain in ch.options_ecartees()),
        ("long", "long", "nombre"),
    )

    corps += "<h2 id=\"hypotheses\">Les hypothèses</h2>"
    corps += g.tableau(
        "Chaque hypothèse du chiffrage, ses trois valeurs et sa raison",
        ("Hypothèse", "Favorable", "Centrale", "Défavorable", "Pourquoi"),
        tuple(
            (g.echapper(h.libelle),
             ch.hypothese_texte(h, "favorable"),
             ch.hypothese_texte(h, "central"),
             ch.hypothese_texte(h, "defavorable"),
             g.echapper(h.fondement))
            for h in ch.HYPOTHESES.values()
        ),
        ("long", "nombre", "nombre", "nombre", "long"),
    )
    corps += (
        "<p>Toutes les hypothèses ne se valent pas. Le tableau suivant pousse "
        "chacune seule à ses deux bornes, les autres restant centrales, et "
        "montre ce que devient le solde. Deux d'entre elles font l'essentiel "
        "de l'incertitude — la part de la dépense qui suit les effectifs, "
        "et le traitement des pensions ; les autres déplacent le résultat "
        "de quelques centaines de millions. La part des élèves défavorisés "
        "n'y figure plus : elle change le montant déplacé entre élèves, non "
        "le solde.</p>"
    )
    corps += g.tableau(
        "Sensibilité du solde annuel en 2035 à chaque hypothèse",
        ("Hypothèse", "Solde si favorable", "Solde si défavorable"),
        tuple((g.echapper(h.libelle), e(f, True), e(d, True))
              for h, f, d in ch.sensibilite()),
        ("long", "nombre", "nombre"),
    )

    corps += "<h2 id=\"depart\">Les chiffres de départ</h2>"
    corps += (
        "<p>Ce que le calcul lit au registre, en plus des chiffres déjà cités "
        "sur les autres pages. Chacun figure avec sa source sur la page "
        f'<a href="{g.lien("sources")}">Sources</a>.</p>'
    )
    corps += g.tableau(
        "Les chiffres constatés dont part le chiffrage",
        ("Ce qui est mesuré", "Valeur", "Année"),
        tuple(
            (g.echapper(c.libelle), g.echapper(c.texte), c.annee)
            for c in CHIFFRES.values() if "chiffrage" in c.themes
        ) + (
            ("Baisse des effectifs d'ici 2035, rapportée aux effectifs "
             "actuels (calculée)", ch.pourcent(ch.baisse_demographique()),
             "2026"),
            ("Part des cotisations de pension dans les dépenses de personnel "
             "(calculée)", ch.pourcent(ch.part_pensions()), "2026"),
        ),
        ("long", "nombre", "nombre"),
    )

    corps += "<h2 id=\"limites-chiffrage\">Ce que ce chiffrage ne fait pas</h2>"
    corps += g.note(
        "<p><strong>Il ne compte aucun bénéfice.</strong> Un élève qui sort "
        "de l'école en sachant lire rapporte, sur une vie, bien plus que ce "
        "qu'il a coûté ; nous ne l'avons pas chiffré, parce que la "
        "littérature ne permet pas d'attribuer un gain à une réforme qui "
        "n'a pas eu lieu. Le chiffrage est un chiffrage de dépense, pas un "
        "calcul de rentabilité.</p>"
        "<p><strong>Il mêle des années.</strong> La dépense par élève du "
        "public et du privé date de 2021 ; le budget, de 2026. Rien n'est "
        "revalorisé de l'inflation, et cela compte : les prix ont augmenté "
        f"de {v('inflation_2022')} en 2022, {v('inflation_2023')} en 2023, "
        f"{v('inflation_2024')} en 2024 et {v('inflation_2025')} en 2025, "
        f"soit {ch.pourcent(ch.inflation_depuis_2021())} en quatre ans. "
        "Revalorisés d'autant, le rapprochement du privé et le financement "
        f"du hors contrat coûteraient {e(ch.surcout_inflation())} de plus "
        f"par an, et le solde central passerait de {e(central, True)} à "
        f"{e(central + ch.surcout_inflation(), True)}. L'enveloppe tiendrait "
        "alors par la règle de sauvegarde, au prix d'un rapprochement un "
        "peu plus lent, et non par le calcul. La majoration sociale, "
        "revalorisée, déplacerait davantage entre élèves, sans changer le "
        "solde.</p>"
        "<p><strong>Il ne suit pas les comportements.</strong> Si le "
        "rapprochement du financement attire vers le privé plus d'élèves "
        "qu'il n'en compte aujourd'hui, le coût du rapprochement augmente "
        "avec eux, et les coûts fixes laissés dans le public aussi. Si la "
        "démographie déçoit les projections, le dividende baisse d'autant — "
        "c'est ce que la règle de sauvegarde corrige.</p>"
        "<p><strong>Il n'est pas un rapport officiel.</strong> C'est un "
        "calcul de campagne, fait avec les chiffres publics disponibles, "
        "dont chaque ligne peut être refaite. Une erreur se signale "
        f'<a href="{g.DEPOT}/issues">sur le dépôt</a>.</p>',
        "vigilance",
    )
    return corps


# -- la confiance ------------------------------------------------------------


def objections() -> str:
    corps = g.affiche(
        "La confiance · 1",
        "Les objections, y compris celles qui ont raison.",
        "Dix objections sérieuses à ce programme. Nous les formulons dans "
        "leur version la plus forte, et non dans leur caricature — cinq "
        "d'entre elles, à notre avis, touchent juste, en tout ou en partie.",
    )

    corps += g.note(
        "<p>Une proposition politique qui ne publie pas ses points faibles "
        "demande qu'on lui fasse confiance sur parole. Celle-ci les publie. "
        "Les objections 3, 4, 7, 8 et 10 nous paraissent fondées, en tout "
        "ou en partie, et nous le disons à l'endroit où on les lit.</p>",
        "resume",
    )

    corps += g.section_cle(
        "deux-vitesses",
        "N'est-ce pas une école à deux vitesses ?",
        "Elle existe déjà, et elle se paie en mètres carrés. Le prix de "
        "l'immobilier intègre la qualité des établissements : ceux qui "
        "peuvent déménager choisissent leur école, les autres subissent la "
        "leur. Notre proposition ne crée pas le choix — elle le rend gratuit "
        "pour les familles modestes, plafonné pour les autres, et le soumet "
        "à des règles écrites, avec interdiction de "
        "sélectionner à l'entrée et financement majoré pour l'élève "
        "défavorisé.",
        "Voir la réforme 2 et les garde-fous, page « La proposition ».",
    )

    corps += g.section_cle(
        "suede",
        "La Suède a essayé, et cela a échoué.",
        "C'est notre principale source, et il faut la citer exactement : la "
        "ségrégation scolaire suédoise a augmenté et les notes ont gonflé, "
        "c'est établi ; en revanche l'IFAU, l'institut public suédois "
        "d'évaluation, attribue au libre choix une part modeste de cette "
        "hausse et ne trouve pas d'effet négatif net sur les résultats des "
        "élèves. Nous ne plaidons donc pas « la Suède a réussi », et nous ne "
        "concédons pas non plus « la liberté scolaire fait chuter un pays ». "
        "Nous retenons ce qui est solide. La Suède a ouvert le "
        f"financement en {v('suede_reforme')} sans interdire la sélection de "
        "fait, sans pondérer le financement selon l'élève, et en laissant "
        "les écoles noter elles-mêmes leurs élèves. Nos quatre garde-fous "
        "corrigent exactement ces quatre points. Si l'on nous répond que ces "
        "garde-fous ne tiendront pas, c'est une objection recevable — mais "
        "c'est alors une objection sur la capacité de l'État à faire "
        "respecter des règles, pas sur le principe.",
        "Voir la page « Ailleurs en Europe ».",
    )

    corps += g.section_cle(
        "ecremage",
        "Les bonnes écoles écrémeront quand même.",
        "<strong>Objection partiellement fondée.</strong> L'interdiction de "
        "sélectionner empêche le tri explicite, pas le tri implicite : une "
        "école peut décourager une famille sans la refuser, par son projet, "
        "ses exigences ou son coût annexe. Nous n'avons pas de remède "
        "parfait. Nous avons trois atténuations — la pondération financière "
        "qui rend l'élève difficile attractif, la publication de la "
        "composition sociale de chaque établissement, et l'attribution des "
        "places par procédure publique — et nous considérons ce risque comme "
        "le principal de la réforme, à surveiller et à corriger en cours de "
        "route. La France en a déjà fait l'expérience : l'assouplissement de "
        "la carte scolaire, en 2007, a fait perdre aux collèges de "
        "l'éducation prioritaire une part significative de leurs entrées en "
        "sixième (" + _source("carte_scolaire_2007") + ") — par des "
        "dérogations, sans pondération ni procédure publique, c'est-à-dire "
        "sans aucune des trois atténuations.",
    )

    corps += g.section_cle(
        "moyens",
        "Il faudrait surtout donner plus de moyens.",
        "<strong>Objection partiellement fondée — et notre programme n'y "
        "répond qu'en partie.</strong> La France consacre à son école une "
        "part de sa richesse supérieure à la moyenne de l'OCDE, mais pas là "
        f"où cela compte le plus : par écolier, elle dépense "
        f"{v('ocde_elementaire_fr')} contre {v('ocde_elementaire_ocde')} en "
        "moyenne dans l'OCDE. À ce niveau, la demande de moyens est fondée. "
        "Notre programme ne redirige pas l'argent du lycée vers l'école : le "
        "montant par élève reprend la répartition actuelle, et seule la "
        "revalorisation, plus forte à l'école qu'au collège, penche vers le "
        "primaire. Il ne crée pas non plus de postes : la baisse "
        "démographique paie la revalorisation, ce qui suppose environ "
        f"{ch.milliers(ch.postes_non_remplaces())} postes d'enseignants de "
        "moins qu'aujourd'hui en 2035, à taux d'encadrement constant — là "
        "où le Conseil d'analyse économique recommande d'employer cette "
        "baisse à réduire la taille des classes. Ce qui ne tient pas, en "
        "revanche, c'est la demande de moyens <em>en général</em> : au "
        f"lycée, la France dépense {v('ocde_lycee_fr')} par élève contre "
        f"{v('ocde_lycee_ocde')} dans l'OCDE, un quart de plus, pour des "
        "résultats qui ne le sont pas. Et le dédoublement des classes, qui "
        f"coûte {v('dedoublement_cout')}, a produit des effets réels mais "
        "modestes, dont la rentabilité divise les économistes.",
        "Voir la page « Dépense ».",
    )

    corps += g.section_cle(
        "prive-lucratif",
        "Vous allez financer des écoles privées à but lucratif.",
        "Le contrat unique impose la publication des comptes et le "
        "réinvestissement des excédents dans l'activité scolaire. Un "
        "établissement qui remplit le contrat — socle enseigné, pas de "
        "sélection, évaluations publiées, comptes ouverts — est financé quel "
        "que soit son statut juridique ; un établissement qui distribuerait "
        "à des actionnaires de l'argent versé par le contribuable ne remplit "
        "pas le contrat. C'est la règle que la Suède n'avait pas.",
    )

    corps += g.section_cle(
        "laicite",
        f"{v('prive_catholique')} des écoles sous contrat sont catholiques : "
        "vous allez financer la religion.",
        "C'est le régime actuel qui produit ce chiffre, et c'est un argument "
        "pour la réforme, pas contre. Le contingentement des contrats a figé "
        "la situation telle qu'elle était : les seuls candidats déjà "
        "installés obtiennent les contrats, et une école laïque nouvelle n'a "
        "pratiquement aucune chance d'être financée. Ouvrir le contrat à "
        "tout établissement qui respecte le socle et l'accueil sans "
        "sélection diversifie l'offre au lieu de la figer — et le socle "
        "républicain, lui, devient opposable à tous les financés.",
    )

    corps += g.section_cle(
        "ruralite",
        "Dans un village avec une seule école, le choix est fictif.",
        "<strong>Objection fondée.</strong> C'est vrai, et c'est pourquoi la "
        "réforme 1 n'est pas la première du "
        "programme. Pour la majorité des communes rurales, ce qui change "
        "utilement est l'autonomie de l'école existante — son équipe, son "
        "organisation, ses moyens propres — et non la possibilité théorique "
        "d'en choisir une autre. Le calendrier proposé commence d'ailleurs "
        "par la transparence et l'autonomie, qui valent partout, et non par "
        "le libre choix, qui ne vaut que là où il y a effectivement le "
        "choix.",
    )

    corps += g.section_cle(
        "enseignants",
        "Les enseignants n'en veulent pas.",
        "<strong>Objection partiellement fondée.</strong> Le recrutement par "
        "l'établissement met fin à l'affectation par barème, qui est perçue "
        "— à juste titre — comme une protection contre l'arbitraire. Nous "
        "n'avons que deux réponses, et il faut les peser : les personnels en "
        "poste conservent statut et garanties, le nouveau régime ne "
        "s'appliquant qu'aux recrutements à venir et sur option ; et la "
        "démographie libère les moyens d'une revalorisation réelle, dans un "
        f"métier payé {v('salaire_ecart_elementaire')} en dessous des autres "
        "diplômés du supérieur. Si la profession refuse malgré tout, la "
        "réforme ne se fera pas contre elle — elle ne se ferait pas, tout "
        "court.",
    )

    corps += g.section_cle(
        "classement",
        "Publier les résultats, c'est créer des palmarès qui stigmatisent.",
        "C'est exact des palmarès bruts, qui mesurent surtout le public "
        "recruté, et c'est pourquoi nous ne publions pas cela. Ce que nous "
        "publions est la valeur ajoutée : la progression des élèves entre "
        "deux évaluations, à niveau d'entrée comparable. Cette mesure "
        "récompense l'école d'un quartier difficile qui fait progresser ses "
        "élèves, et ne récompense pas l'école favorisée qui se contente de "
        "recevoir de bons élèves. Elle a une limite, que nous écrivons : "
        "dans une petite école, calculée sur quelques élèves, sa marge "
        "d'erreur est large, et deux écoles proches ne se départagent pas "
        "davantage que deux pays séparés de trois points. La presse "
        "publiera de toute façon des classements : autant qu'ils reposent "
        "sur la bonne grandeur.",
    )

    corps += g.section_cle(
        "preuve",
        "Rien ne prouve que votre réforme marchera en France.",
        "<strong>Objection fondée.</strong> Aucune expérience étrangère ne "
        "se transpose, et nous l'écrivons sur chaque page de comparaison. "
        "C'est la raison pour laquelle le calendrier commence par ce qui est "
        "réversible et mesurable — publier les résultats, puis donner "
        "l'autonomie à des académies volontaires — avant de toucher au "
        "financement. Une réforme qu'on ne peut pas évaluer en cours de "
        "route ne devrait pas être proposée, et celle-ci est construite pour "
        "l'être.",
        "Voir le calendrier, page « La proposition ».",
    )
    return corps


def sources_page() -> str:
    corps = g.affiche(
        "La confiance · 2",
        "Tous les chiffres, et d'où ils viennent.",
        "Chaque chiffre cité sur ce site figure ici, avec son année, son "
        "émetteur et l'adresse du document. Aucun n'est de notre "
        "fabrication : les seuls calculs du site sont ceux du chiffrage, "
        "qui affiche ses formules et ses hypothèses.",
    )

    corps += g.note(
        "<p><strong>La règle que ce site s'impose.</strong> Les chiffres "
        "vivent à un seul endroit du code, avec leur source. Les pages ne "
        "les écrivent pas : elles les demandent. Un chiffre corrigé l'est "
        "donc partout d'un coup, et cette page ne peut pas se désynchroniser "
        "des autres — elle est construite à partir du même registre.</p>",
        "resume",
    )

    for intitule, chiffres in par_theme():
        lignes = tuple(
            (
                g.echapper(c.libelle)
                + (f'<br><span class="discret">{g.echapper(c.precision)}</span>'
                   if c.precision else ""),
                g.echapper(c.texte),
                g.echapper(c.annee),
                f'<a href="{c.url}">{g.echapper(c.source)}</a>',
            )
            for c in chiffres
        )
        corps += f"<h2>{g.echapper(intitule)}</h2>"
        corps += g.tableau(
            f"{g.echapper(intitule)} : les chiffres cités, leur valeur, leur "
            "année et leur source",
            ("Ce qui est mesuré", "Valeur", "Année", "Source"),
            lignes,
            ("long", "nombre", "nombre", "texte"),
        )

    corps += "<h2>Les faits cités</h2>"
    corps += g.note(
        "<p>Un site peut citer tous ses chiffres et affirmer dans la même "
        "phrase qu'un rapport conclut ceci, ou qu'un décret a fait cela, sans "
        "que le lecteur puisse le vérifier. Ces affirmations-là obéissent "
        "désormais à la même règle que les chiffres : elles vivent au même "
        "endroit du code, avec leur source, et une page ne peut pas en "
        "invoquer une qui n'y figure pas.</p>",
        "resume",
    )
    corps += g.tableau(
        "Les affirmations datées du site, et le document qui les établit",
        ("Ce que le site affirme", "Année", "Source"),
        tuple(
            (
                g.echapper(f.enonce),
                g.echapper(f.annee),
                f'<a href="{f.url}">{g.echapper(f.source)}</a>',
            )
            for f in FAITS.values()
        ),
        ("long", "nombre", "texte"),
    )

    corps += "<h2>Les documents cités</h2>"
    corps += g.leviers(tuple(
        f'<a href="{source.url}">{g.echapper(source.nom)}</a> — '
        f"{len(source.chiffres)} chiffre"
        + ("s" if len(source.chiffres) > 1 else "")
        for source in sources()
    ))

    corps += "<h2>Les limites de ce site</h2>"
    corps += g.leviers((
        "<strong>Les années diffèrent.</strong> Les enquêtes internationales "
        "sont triennales ou quadriennales ; les données financières sont "
        "annuelles. Un tableau qui met côte à côte un score de 2025 et une "
        "dépense de 2022 rapproche deux instants différents, et il faut le "
        "savoir.",
        "<strong>Les comparaisons internationales sont fragiles.</strong> "
        "Les pays ne scolarisent ni les mêmes élèves, ni au même âge, ni avec "
        "les mêmes définitions. Nous les utilisons pour des ordres de "
        "grandeur, jamais pour départager deux pays séparés de trois points.",
        "<strong>Les chiffres de gouvernance sont anciens.</strong> Les "
        "indicateurs de répartition des décisions datent de la dernière "
        "vague disponible ; la structure qu'ils décrivent n'a pas changé, "
        "mais les pourcentages précis, eux, peuvent avoir bougé.",
        "<strong>Le chiffrage est le seul calcul du site.</strong> Il part "
        "des chiffres de cette page, mais il y ajoute des hypothèses : "
        "elles sont données une par une, avec trois valeurs et leur raison, "
        f'sur la page <a href="{g.lien("chiffrage")}">Chiffrage</a>. Il a '
        "démenti ce que nous affirmions — que le programme tenait à "
        "enveloppe constante. Nous avons corrigé le programme, et non le "
        "calcul : la page dit ce que nous avons abandonné, et qui le paie.",
    ))

    corps += g.encadre(
        "<h3 class=\"serif\">Une erreur ? Elle se corrige.</h3>"
        "<p>Ce site est un dépôt public. Un chiffre faux, une source "
        "périmée, une objection oubliée : ouvrez une "
        f'<a href="{g.DEPOT}/issues">issue</a>, et la correction sera '
        "publiée avec sa date. Nous préférons un site qu'on peut prendre en "
        "défaut à un site qu'il faut croire.</p>"
    )
    return corps


PAGES = {
    "index": index,
    "resultats": resultats,
    "depense": depense,
    "gouvernance": gouvernance,
    "proposition": proposition,
    "comparaisons": comparaisons,
    "chiffrage": chiffrage,
    "objections": objections,
    "sources": sources_page,
}

__all__ = ["PAGES", "CHIFFRES"]
