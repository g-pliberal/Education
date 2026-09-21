"""Le contenu du site, page par page.

Chaque fonction rend le corps d'une page — tout ce qui se trouve entre le
bandeau et le pied. Le gabarit fait le reste.

Les chiffres ne sont jamais écrits ici : ils sont demandés à
`donnees.valeur()`, qui les prend au registre. Une faute de frappe dans un nom
de chiffre casse la construction ; un chiffre corrigé à la source l'est partout
d'un coup, page « Sources » comprise.
"""

from __future__ import annotations

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
        "L'école française dépense beaucoup et apprend peu.",
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
        "son école un effort légèrement supérieur à celui de ses voisins — "
        f"{v('ocde_pib_comparable')} contre {v('ocde_pib_moyenne')} dans "
        "l'OCDE —, et le répartit à contretemps : moins que la moyenne par "
        "écolier, un quart de plus par lycéen. Ses résultats, eux, sont "
        "inférieurs à cette moyenne. Ce n'est donc pas d'abord une question "
        "de montant : c'est une question de qui décide, de qui rend des "
        "comptes, et de qui peut partir quand rien ne change.</p>"
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
         f"un peu supérieur à la moyenne : {v('ocde_pib_comparable')} "
         f"contre {v('ocde_pib_moyenne')}. Mais la France dépense "
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
        ("L'inégalité n'est pas corrigée",
         f"{v('pisa_ecart_social')} séparent en mathématiques les élèves "
         "français les plus favorisés des plus défavorisés. Le système qui "
         "se réclame le plus de l'égalité est l'un de ceux où l'origine "
         "sociale pèse le plus lourd sur les résultats. Nous n'écrivons pas "
         "que l'école fabrique cette inégalité — les enquêtes ne "
         "l'établissent pas. Nous écrivons qu'elle la corrige moins que "
         "celles de nos voisins, ce qui suffit à juger une institution dont "
         "c'est la raison d'être."),
    ))

    corps += g.engagements((
        g.Engagement(
            "100 %",
            "Le financement public suit l'élève, intégralement.",
            "Le même montant public par élève, quel que soit l'établissement "
            "qui l'accueille — public, privé sous contrat, école nouvelle. "
            "Aujourd'hui, la dotation dépend du statut de l'école ; demain, "
            "elle dépendra de l'enfant."),
        g.Engagement(
            "+ 40 %",
            "Un financement majoré pour l'élève défavorisé.",
            "Une pondération sociale du montant versé, et une pondération de "
            "handicap. C'est la réponse à la seule objection sérieuse faite à "
            "la liberté scolaire : un établissement doit avoir intérêt à "
            "accueillir l'élève difficile, et non à l'éviter."),
        g.Engagement(
            "0",
            "Plus de carte scolaire d'affectation.",
            "Les familles classent leurs vœux, les établissements ne "
            "sélectionnent pas, et une procédure publique attribue les places "
            "selon des règles écrites — fratrie, proximité, tirage au sort "
            "en cas de sur-demande. L'adresse cesse d'être un destin."),
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
            '<span class="badge">Non</span> Qu\'il faut dépenser moins. '
            "Nous proposons de dépenser autrement, à enveloppe constante, "
            "et de rémunérer mieux les enseignants.",
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
         "Huit réformes, leur calendrier, leurs garde-fous — et le calcul "
         "de ce qu'elles coûtent, avec ses perdants nommés. "
         f'<a href="{g.lien("proposition")}">La proposition</a>, '
         f'<a href="{g.lien("chiffrage")}">le chiffrage</a>, et '
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
        "Quatre enquêtes indépendantes, trois internationales et une "
        "française, mesurent la même chose depuis vingt ans : le niveau des "
        "élèves français baisse, et il baisse d'abord chez les plus faibles.",
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
                 f"Recul de {v('pisa_maths_chute')} depuis 2018."),
        g.Repere("Élèves en difficulté", v("pisa_faibles"),
                 "sous le niveau 2 en mathématiques, contre "
                 f"{v('pisa_faibles_2018')} en 2018."),
        g.Repere("Écart social", v("pisa_ecart_social"),
                 "entre les élèves les plus favorisés et les plus "
                 "défavorisés."),
    ))

    corps += "<h2 id=\"pisa\">PISA : la chute de 2022</h2>"
    corps += (
        "<p>PISA mesure tous les trois ans ce que les élèves de quinze ans "
        "savent faire d'un savoir dans une situation qu'on ne leur a pas "
        "apprise. En 2022, la France obtient "
        f"{v('pisa_maths')} en mathématiques — techniquement au-dessus de la "
        f"moyenne de l'OCDE ({v('pisa_maths_ocde')}), et en recul de "
        f"{v('pisa_maths_chute')} par rapport à 2018. C'est la plus forte "
        "baisse jamais enregistrée par la France dans cette enquête.</p>"
        "<p>La moyenne rassure à tort. Ce qui a bougé, ce n'est pas le "
        f"sommet : c'est le bas. {v('pisa_faibles')} des élèves français sont "
        "désormais sous le niveau 2 en mathématiques, contre "
        f"{v('pisa_faibles_2018')} quatre ans "
        "plus tôt. Le niveau 2 n'est pas l'excellence : c'est le seuil en "
        "deçà duquel un adulte ne peut pas vérifier une facture, comparer "
        "deux offres de crédit ou lire un graphique de journal.</p>"
    )
    corps += g.tableau(
        "PISA 2022 : les scores français et la moyenne de l'OCDE",
        ("Domaine", "France", "Moyenne OCDE", "Depuis 2018"),
        (
            ("Mathématiques", v("pisa_maths"), v("pisa_maths_ocde"),
             v("pisa_maths_chute")),
            ("Compréhension de l'écrit", v("pisa_lecture"),
             v("pisa_lecture_ocde"), v("pisa_lecture_chute")),
            ("Culture scientifique", v("pisa_sciences"),
             v("pisa_sciences_ocde"), "stable"),
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
        "C'est un arrêt de la chute, obtenu au prix d'un effort considérable "
        "sur les premières années — dédoublement des classes, recentrage sur "
        "les fondamentaux —, et il n'a pas d'équivalent au collège.</p>"
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
        "mille jeunes par an</strong> qui sortent de treize années de "
        "scolarité obligatoire sans savoir lire un mode d'emploi. À "
        "l'échelle d'un quinquennat, un quart de million. Aucun chiffre de "
        "dépense ne pèse contre celui-là.</p>"
    )

    corps += "<h2 id=\"inegalites\">L'école la plus inégalitaire d'Europe</h2>"
    corps += (
        f"<p>{v('pisa_ecart_social')} séparent en mathématiques les élèves "
        "français les plus favorisés des plus défavorisés. La France figure "
        "parmi les pays de l'OCDE où l'origine sociale prédit le mieux les "
        "résultats scolaires — c'est-à-dire parmi ceux où l'école corrige le "
        "moins ce qu'elle reçoit.</p>"
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
        "baissé, la base a décroché, et l'écart social n'a pas été réduit. "
        "Aucune de ces trois affirmations n'est sérieusement contestée.</p>",
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

    corps += ("<h2 id=\"combien\">Un effort un peu supérieur, réparti à "
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
        f"{v('ocde_pib_moyenne')} en moyenne dans l'OCDE. Elle est donc bien "
        "au-dessus de la moyenne, mais de <strong>0,7 point</strong>, et non "
        "des deux points que laissait croire la comparaison d'un agrégat "
        "français avec une moyenne internationale.</p>"
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
        "slogan qu'on entend des deux côtés. <strong class=\"cle-texte\">La "
        "France n'est pas un pays qui dépense trop pour son école : c'est un "
        "pays qui dépense à contretemps</strong> — en dessous de la moyenne "
        "de l'OCDE à l'école élémentaire, où tout se joue, et d'un quart "
        "au-dessus au lycée, où il est déjà tard.</p>"
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
        "deux, au bénéfice de ceux qui ont déjà réussi.</strong> La France "
        "est, parmi les grands pays européens, l'un de ceux où la dépense "
        "penche le plus vers le second degré et le supérieur.</p>"
        "<p>Cette pente est l'inverse de celle que suggère la comparaison "
        "internationale du haut de cette page, où la France est en dessous "
        "de la moyenne de l'OCDE à l'élémentaire et très au-dessus au "
        "lycée.</p>"
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
        "d'éducation : fournitures, cantine, transport, et un marché du "
        "soutien scolaire privé qui prospère exactement là où l'école "
        "échoue. Ce chiffre est une mesure de la défiance.</p>"
    )

    corps += "<h2 id=\"rendement\">Ce que les grandes réformes ont rendu</h2>"
    corps += (
        "<p>Deux réformes récentes ont engagé des moyens considérables. "
        "Toutes deux ont été évaluées. Aucune n'a tenu ses promesses, et il "
        "faut le dire même quand on approuvait leur intention.</p>"
    )
    corps += g.sections_depliables((
        ("Le dédoublement des classes de CP et CE1 en éducation prioritaire",
         "<p>Engagé en 2017, le dédoublement a ramené les classes de CP "
         "puis de CE1 en REP et REP+ à une douzaine d'élèves. Son coût "
         f"annuel est estimé à {v('dedoublement_cout')} par la Cour des "
         f"comptes, pour {v('dedoublement_etp')} emplois.</p>"
         "<p>L'évaluation est plus nuancée que ce que nous en disions, et "
         "il faut la citer exactement. La DEPP mesure un effet réel sur la "
         "progression des élèves en français et en mathématiques "
         "<strong>pendant les deux premières années</strong> de "
         "l'élémentaire, et un climat de classe plus favorable. Ce qui n'a "
         "pas bougé, c'est l'essentiel : <strong class=\"cle-texte\">"
         "l'écart entre l'éducation prioritaire et le reste du système ne "
         "s'est pas réduit</strong>, et le dispositif ne touche qu'une "
         "minorité des élèves en difficulté de l'école élémentaire ("
         + _source("dedoublement_effets") + ").</p>"
         "<p>Réduire la taille des classes fonctionne donc, mais beaucoup "
         "moins que son coût ne le laissait espérer, et sur un périmètre "
         "trop étroit pour déplacer la moyenne nationale. C'est un argument "
         "contre l'usage <em>uniforme</em> d'un levier coûteux, non contre "
         "le levier lui-même — et c'est bien pourquoi nous proposons que "
         "l'établissement décide lui-même où le mettre.</p>"
         "<p>La Cour des comptes va plus loin, et son verdict est le plus "
         "dur : les écarts entre l'éducation prioritaire et le reste du "
         "système tardent à se réduire alors que le coût de cette politique "
         "n'a cessé de croître, et les progrès de court terme obtenus par "
         "le dédoublement s'estompent à l'entrée au collège ("
         + _source("cour_prioritaire") + ").</p>"),
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

    corps += "<h2 id=\"demographie\">La marge de manœuvre arrive toute seule</h2>"
    corps += (
        f"<p>Les projections du ministère annoncent {v('demographie')} d'ici "
        "2035. À dépense constante, cela signifie mécaniquement un "
        "desserrement considérable : davantage d'adultes par enfant, sans "
        "un euro de plus.</p>"
        "<p>Une précision que nous nous devons, parce que nous expliquons "
        "ailleurs le contraire : <strong>la dépense ne baisse pas "
        "proportionnellement aux effectifs</strong>. Les murs, le chauffage "
        "et la direction ne suivent pas les élèves — c'est exactement ce qui "
        "a mis les communes suédoises en difficulté. Seule la part variable "
        "se libère, et le calcul que nous en faisons, hypothèses comprises, "
        f'est page <a href="{g.lien("chiffrage")}">Le chiffrage</a>.</p>'
        "<p>Cette baisse est une occasion, et elle ne se représentera pas. "
        "Deux usages en sont possibles. Le premier est de ne rien décider et "
        "de laisser l'économie se faire silencieusement, poste par poste, au "
        "gré des lois de finances. Le second est de décider ce qu'on en fait : "
        "<strong class=\"cle-texte\">relever la rémunération des enseignants "
        "et financer la liberté de choix, à enveloppe constante</strong>. "
        "C'est le choix de ce programme.</p>"
    )
    corps += g.note(
        "<p><strong>Notre proposition ne demande pas un euro de plus.</strong> "
        "Elle redirige l'euro existant : vers les premières années, vers la "
        "rémunération des enseignants, et vers l'élève plutôt que vers "
        f'l\'institution. Le détail est sur la page <a href="'
        f'{g.lien("proposition")}">La proposition</a>.</p>',
        "resume",
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

    corps += "<h2 id=\"centralisation\">Le pays le plus centralisé de l'OCDE</h2>"
    corps += (
        f"<p>{v('decisions_central')} des décisions qui concernent un collège "
        "public français se prennent au niveau de l'État central. La moyenne "
        f"de l'OCDE est de {v('decisions_central_ocde')}. À l'autre bout de "
        f"la chaîne, {v('decisions_etablissement')} des décisions se prennent "
        "dans l'établissement — et sur ces dix points, deux seulement "
        "s'exercent en pleine autonomie ; le reste s'applique dans un cadre "
        "fixé plus haut.</p>"
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
    )

    corps += "<h2 id=\"recrutement\">Un chef d'établissement qui ne choisit personne</h2>"
    corps += (
        f"<p>En France, {v('recrutement_france')} des élèves fréquentent un "
        "établissement dont le chef a la responsabilité principale du "
        f"recrutement des enseignants. La moyenne de l'OCDE est de "
        f"{v('recrutement_ocde')}. En Estonie, premier pays européen aux "
        f"épreuves PISA, c'est {v('estonie_recrutement')}.</p>"
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
        f"second degré — {v('prive_eleves_part')} de l'ensemble, soit plus "
        "de deux millions d'élèves. Ses enseignants sont rémunérés par "
        "l'État ; ses établissements suivent les programmes nationaux.</p>"
        f"<p>Mais {v('prive_catholique')} des élèves du privé sous contrat "
        "sont scolarisés dans un établissement de l'enseignement "
        "catholique. Ce n'est pas un "
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
    )

    corps += "<h2 id=\"enseignants\">Un métier qu'on n'a pas les moyens de rendre attractif</h2>"
    corps += (
        "<p>Les enseignants français sont, rapportés aux autres diplômés du "
        "supérieur de leur pays, parmi les moins bien payés de l'OCDE : leur "
        f"salaire effectif est inférieur de {v('salaire_ecart_elementaire')} "
        "à celui des autres diplômés dans l'élémentaire et de "
        f"{v('salaire_ecart_college')} au collège, contre respectivement "
        f"{v('salaire_ecart_elementaire_ocde')} et "
        f"{v('salaire_ecart_college_ocde')} en moyenne dans l'OCDE.</p>"
        "<p>Dans le même temps, ils enseignent davantage d'heures que leurs "
        f"collègues : {v('heures_elementaire')} d'enseignement obligatoire "
        f"par an dans l'élémentaire contre {v('heures_elementaire_ocde')} "
        f"en moyenne, {v('heures_college')} au collège contre "
        f"{v('heures_college_ocde')}. Et la taille moyenne "
        f"d'une classe élémentaire française, {v('taille_classe')}, est "
        "au-dessus de la moyenne de l'OCDE.</p>"
        "<p>Plus d'heures, des classes un peu plus chargées, un salaire "
        "relatif plus bas : la crise de recrutement n'a rien de mystérieux. "
        "Aucune réforme de l'école ne réussira contre ses enseignants, et "
        "aucune ne réussira sans les payer.</p>"
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
        "Huit réformes, à enveloppe constante — et le calcul qui le "
        f'montre est sur la page <a href="{g.lien("chiffrage")}">Le '
        "chiffrage</a>. Aucune n'est nouvelle : "
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
        ("autorite", "8. L'autorité"),
        ("droit", "Ce qu'il faut changer dans le droit"),
        ("calendrier", "Le calendrier"),
        ("garde-fous", "Les garde-fous"),
    ))

    corps += g.note(
        "<p><strong>La logique d'ensemble.</strong> Les huit réformes ne sont "
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
        "moyenne par élève du niveau considéré — de l'ordre de "
        f"{v('die_premier_degre')} dans le premier degré et "
        f"{v('die_college')} au collège. Il n'y a pas d'argent nouveau, il y "
        "a un destinataire nouveau.</p>"
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
        "majoré de 40 % pour un élève d'origine défavorisée, et d'un montant "
        "calculé pour un élève en situation de handicap ou allophone. Un "
        "établissement a alors un intérêt financier direct à accueillir les "
        "élèves que le système actuel se renvoie, et à les faire "
        "progresser — puisque l'évaluation (réforme 5) mesure la valeur "
        "ajoutée et non le niveau brut.</p>"
        "<p><strong>Sur quoi se calcule la majoration.</strong> Une "
        "pondération sociale dont personne ne sait mesurer l'assiette n'est "
        "qu'un slogan. Nous n'en inventons pas : l'instrument existe, il "
        "est français, il est public. La DEPP calcule pour chaque école, "
        "collège et lycée un <strong class=\"cle-texte\">indice de "
        "position sociale</strong>, publié en données ouvertes, "
        "établissement par établissement (" + _source("ips") + "). C'est "
        "lui qui sert d'assiette, et il a l'avantage d'être déjà contesté, "
        "discuté et corrigé publiquement depuis des années.</p>"
        "<p>Le taux de 40 %, lui, est un choix politique et non un "
        "résultat d'étude, et nous ne lui inventons pas de caution "
        "savante : il doit être révisable au vu de ce qu'il produit. Ce qui "
        "est établi, en revanche, c'est le principe — la Cour des comptes "
        "recommande elle-même de moduler les moyens selon la composition "
        "sociale des établissements. "
        f'Ce qu\'il coûte est calculé page <a href="{g.lien("chiffrage")}">'
        "Le chiffrage</a> — et il y a un perdant.</p>"
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
        f"concernés à la totalité — la norme dans l'OCDE, où la moyenne est "
        f"de {v('recrutement_ocde')}.",
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
        "l'entrée sur dossier, entretien, ni tarif ; l'affectation passe par "
        "la procédure publique de la réforme 5.",
        "<strong>Passer les évaluations nationales</strong> et en publier les "
        "résultats, y compris la valeur ajoutée.",
        "<strong>Ouvrir ses comptes</strong> — financement, rémunérations, "
        "excédents. Un établissement financé par l'impôt rend publics ses "
        "comptes.",
    ))
    corps += (
        f"<p>Qui tient ce contrat est financé. Aujourd'hui, "
        f"{v('prive_catholique')} des élèves du privé sous contrat sont dans "
        "un établissement catholique, non parce que les familles n'en "
        "voudraient pas "
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
        "sélectionne.",
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
        f"système scolaire doit perdre {v('demographie')} d'ici 2035. Nous "
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
        f"<p>Ce n'est pas une question d'heures : la France enseigne déjà "
        f"{v('heures_elementaire')} par an dans l'élémentaire, contre "
        f"{v('heures_elementaire_ocde')} en moyenne dans l'OCDE. Nous enseignons plus longtemps, sur un "
        "programme plus large, et nous obtenons "
        f"{v('timss_cm1_maths')} en mathématiques en CM1. La contrainte n'est "
        "pas le temps disponible : c'est ce qu'on y met.</p>"
    )

    corps += "<h2 id=\"autorite\">8. Une autorité qui ferme les écoles</h2>"
    corps += (
        "<p>C'est la réforme que nous avions oubliée, et c'était la plus "
        "grosse faille de ce programme. Nous écrivions qu'une école qui "
        "échoue durablement doit « changer de direction ou fermer » sans "
        "dire <strong>qui le décide, à partir de quel seuil, et avec quel "
        "recours</strong>. Une promesse de responsabilité sans autorité qui "
        "la prononce n'engage personne.</p>"
        "<p>Les Pays-Bas, que nous citons en modèle, ne tiennent pas par "
        "leur liberté scolaire : ils tiennent par leur inspection. Elle "
        "juge « très faible » l'établissement qui passe sous la norme "
        "légale, publie la liste de ces établissements, y retourne dans "
        "l'année puis contre-visite au bout d'un an au plus, et peut "
        "recommander au ministre la fermeture de celui qui ne se redresse "
        "pas (" + _source("inspection_nl") + "). Nous avions retenu le "
        "résultat néerlandais en omettant la machine qui le produit.</p>"
        "<p>Nous proposons donc une <strong class=\"cle-texte\">autorité "
        "indépendante d'évaluation des établissements</strong>, distincte du "
        "ministère qui pilote et des rectorats qui gèrent, sur le modèle des "
        "autorités administratives indépendantes existantes : membres "
        "nommés pour un mandat non renouvelable, budget propre, rapports "
        "publics, et compte rendu annuel devant le Parlement.</p>"
    )
    corps += g.gestes((
        "<strong>Le seuil est écrit à l'avance.</strong> Un établissement "
        "dont la valeur ajoutée est significativement négative trois années "
        "consécutives entre en procédure. Non pas un mauvais résultat, qui "
        "peut tenir au public accueilli : une progression des élèves "
        "inférieure à ce que leur niveau d'entrée laissait attendre, trois "
        "ans de suite.",
        "<strong>La procédure est contradictoire.</strong> L'établissement "
        "répond, produit son analyse, et dispose de deux ans avec un appui "
        "renforcé et des moyens supplémentaires. Une école en difficulté "
        "reçoit d'abord de l'aide, pas une sanction.",
        "<strong>La sanction est graduée.</strong> Changement de direction, "
        "puis retrait du contrat et réaffectation des élèves, avec "
        "obligation pour l'autorité publique d'assurer une place à chacun. "
        "Aucune fermeture ne peut laisser un enfant sans école.",
        "<strong>Le recours existe.</strong> Les décisions de l'autorité "
        "sont susceptibles de recours devant le juge administratif, comme "
        "toute décision administrative faisant grief.",
    ))
    corps += g.note(
        "<p><strong>Ce que cela nous coûte politiquement, et que nous "
        "assumons.</strong> Créer une autorité, c'est créer de "
        "l'administration — ce qu'un programme libéral n'aime pas faire. "
        "Nous le faisons parce que l'alternative est pire : une liberté "
        "scolaire sans arbitre, c'est la version suédoise, et nous avons "
        "passé une page entière à expliquer pourquoi nous n'en voulons "
        "pas. <strong>L'autonomie sans autorité n'est pas du libéralisme, "
        "c'est de l'abandon.</strong></p>",
        "vigilance",
    )

    corps += ("<h2 id=\"droit\">Ce qu'il faut changer dans le droit, et ce "
              "qui résistera</h2>")
    corps += (
        "<p>Un programme scolaire français qui ne dit rien du droit "
        "constitutionnel n'a pas été écrit sérieusement. Trois textes se "
        "dressent devant cette proposition. Nous les nommons, parce que nos "
        "contradicteurs le feront, et parce qu'il vaut mieux avoir lu "
        "l'obstacle que le découvrir.</p>"
    )
    corps += g.sections_depliables((
        ("La liberté de l'enseignement a valeur constitutionnelle",
         "<p>Le Conseil constitutionnel a jugé que la liberté de "
         "l'enseignement figure parmi les principes fondamentaux reconnus "
         "par les lois de la République, et qu'elle a donc valeur "
         "constitutionnelle. La même décision reconnaît le <em>caractère "
         "propre</em> des établissements privés sous contrat ("
         + _source("liberte_enseignement") + ").</p>"
         "<p><strong>Ce que cela nous oppose.</strong> Notre contrat unique "
         "impose à tout établissement financé d'enseigner le socle en "
         "totalité et de n'exercer aucune sélection à l'entrée. On peut "
         "soutenir que cela vide le caractère propre de sa substance, et "
         "donc porte atteinte à une liberté constitutionnelle.</p>"
         "<p><strong>Ce que nous répondons.</strong> La liberté "
         "d'enseignement reste entière hors financement public : le hors "
         "contrat continue d'exister, et notre réforme ne le touche pas. Ce "
         "que nous encadrons, c'est la contrepartie de l'argent public. Un "
         "établissement demeure libre de son projet, de sa pédagogie, de son "
         "recrutement d'enseignants et de son organisation ; il ne l'est pas "
         "de choisir ses élèves avec l'argent du contribuable. Nous pensons "
         "cette lecture défendable. Nous ne garantissons pas qu'elle "
         "l'emporterait.</p>"),
        ("La loi Falloux plafonne le financement des murs",
         "<p>Hérité de la loi Falloux de 1850, un article du code de "
         "l'éducation plafonne à un dixième de leurs dépenses annuelles les "
         "subventions publiques aux établissements privés d'enseignement "
         "général du second degré (" + _source("falloux") + ").</p>"
         "<p><strong>Ce que cela nous oppose.</strong> Notre réforme 1 exige "
         "une dotation consolidée « murs compris ». C'est une collision "
         "frontale : en l'état du droit, le financement à parité du second "
         "degré privé est illégal.</p>"
         "<p><strong>Ce que nous répondons.</strong> Rien, sinon qu'il "
         "faut abroger cet article par une loi ordinaire — et regarder "
         "précisément pourquoi la dernière tentative a échoué. En 1994, le "
         "Conseil constitutionnel a partiellement censuré la révision : la "
         "loi laissait les collectivités libres de subventionner sans "
         "encadrement, et ne comportait donc pas les garanties nécessaires "
         "au respect de l'égalité, entre établissements privés comme au "
         "détriment des établissements publics ("
         + _source("falloux_1994") + "). Elle a aussi provoqué l'une des "
         "plus grandes manifestations de l'après-guerre.</p>"
         "<p>Ce précédent ne nous condamne pas : il nous dicte la "
         "rédaction. Ce qui a été censuré, c'est la <em>liberté laissée aux "
         "collectivités</em> de financer qui elles voulaient, comme elles "
         "voulaient. Notre proposition est l'inverse : une règle nationale "
         "uniforme, un même montant par élève, les mêmes obligations "
         "opposables à tout établissement financé, public compris. "
         "<strong>C'est une difficulté politique majeure, pas un verrou "
         "juridique infranchissable</strong> — et la nuance tient "
         "entièrement à ce que l'égalité soit garantie par la loi elle-même "
         "plutôt que laissée à l'appréciation locale.</p>"),
        ("La loi de 1905 et le financement des écoles confessionnelles",
         "<p>La République ne reconnaît, ne salarie ni ne subventionne "
         "aucun culte (" + _source("laicite_1905") + ").</p>"
         "<p><strong>Ce que cela nous oppose.</strong> "
         f"{v('prive_catholique')} des élèves du privé sous contrat sont "
         "scolarisés dans un établissement catholique. Porter leur "
         "financement à "
         "parité, investissement compris, sera présenté comme un "
         "financement public du culte.</p>"
         "<p><strong>Ce que nous répondons.</strong> La loi Debré de 1959 a "
         "déjà tranché ce point : l'État rémunère des enseignants qui "
         "dispensent un enseignement, non un culte, et le Conseil "
         "constitutionnel l'a validé. Notre contrat unique <em>renforce</em> "
         "cette séparation plutôt qu'il ne l'affaiblit, puisqu'il rend le "
         "socle républicain intégralement opposable à tout établissement "
         "financé — ce qu'il n'est pas aujourd'hui. Reste que le "
         "financement des bâtiments est d'une autre nature que celui des "
         "traitements, et que ce point sera le plus disputé des trois.</p>"),
    ))
    corps += g.note(
        "<p><strong>Ce que ces trois obstacles impliquent.</strong> Les "
        "réformes 3, 5, 6, 7 et 8 — autonomie, évaluation, métier, socle, "
        "autorité — se font à droit constant ou par loi ordinaire. Les "
        "réformes 1, 2 et 4 — financement à parité, pondération, contrat "
        "unique — supposent d'abroger l'article L. 151-4 et d'accepter un "
        "contrôle de constitutionnalité que nous pouvons perdre. "
        "<strong class=\"cle-texte\">C'est une raison de plus de commencer "
        "par ce qui ne demande pas la loi.</strong></p>",
        "resume",
    )

    corps += "<h2 id=\"calendrier\">En quel ordre</h2>"
    corps += g.gestes((
        "<strong>Première année — la transparence, et la mise en place de "
        "la mesure.</strong> Publication des moyens, des comptes et de la "
        "composition sociale de chaque établissement, et des résultats bruts "
        "contextualisés. <em>Pas</em> la valeur ajoutée : elle exige deux "
        "vagues d'évaluation appariées au niveau de l'élève, et ne peut donc "
        "pas exister la première année. Ce qui se fait l'année 1, c'est le "
        "dispositif qui la rendra possible. L'étape ne coûte presque rien et "
        "ne retire rien à personne.",
        "<strong>Deuxième année — l'autonomie du public.</strong> Dotation "
        "globale et recrutement par l'établissement, d'abord sur les postes "
        "vacants et dans les académies volontaires. Installation de "
        "l'autorité indépendante (réforme 8), qui doit exister avant qu'on "
        "lui donne quelque chose à surveiller.",
        "<strong>Troisième année — l'affectation et la valeur ajoutée.</strong> "
        "Procédure de vœux publique à la place de la sectorisation, à "
        "l'entrée en sixième d'abord. Première publication de la valeur "
        "ajoutée, deux vagues d'évaluation étant désormais disponibles — "
        "l'IVAL des lycées fait cela depuis des années, nous l'étendons.",
        "<strong>Quatrième année — le contrat unique</strong> et la "
        "pondération sociale du financement, appliqués ensemble : l'un sans "
        "l'autre serait la faute suédoise. C'est aussi le poste coûteux, et "
        f'il arrive <a href="{g.lien("chiffrage")}">quand la démographie a '
        "commencé à rendre</a>.",
        "<strong>En continu — la rémunération.</strong> Chaque euro libéré "
        "par la baisse démographique est affecté au salaire des enseignants, "
        "et la loi de finances le documente.",
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


def chiffrage() -> str:
    corps = g.affiche(
        "La proposition · le coût",
        "Ce que la réforme coûte, et qui le paie.",
        "Nous écrivions jusqu'ici que notre proposition tenait à enveloppe "
        "constante sans l'avoir démontré. Cette page fait le calcul. Il est "
        "grossier, entièrement écrit, et il désigne un perdant — "
        "<strong class=\"cle-texte\">sans quoi ce ne serait pas un "
        "chiffrage, mais une promesse</strong>.",
    )

    corps += g.plan((
        ("methode", "La méthode"),
        ("couts", "Ce que ça coûte"),
        ("ressources", "Ce qui le finance"),
        ("perdant", "Qui paie"),
        ("bilan", "Le bilan, et son trou"),
        ("limites", "Ce que ce calcul ne prouve pas"),
    ))

    corps += g.note(
        "<p><strong>La seule page de ce site qui calcule.</strong> Ailleurs, "
        "nous ne faisons que citer : les sources publient des agrégats, et "
        "recalculer un chiffre qu'on n'a pas produit soi-même donne "
        "l'illusion d'un modèle. Ici, il faut bien un modèle. Nous le "
        "posons donc à découvert : <strong>chaque entrée est un chiffre "
        "sourcé du site, chaque opération est écrite, chaque hypothèse est "
        "signalée comme telle</strong>. Un lecteur qui conteste une "
        "hypothèse peut refaire le calcul avec la sienne en dix lignes. "
        "C'est tout ce qu'on peut demander à un chiffrage d'opposition, qui "
        "n'a ni la direction du budget ni les fichiers de paie.</p>",
        "entree",
    )

    corps += "<h2 id=\"methode\">Trois dépenses, deux ressources</h2>"
    corps += (
        "<p>La proposition engage trois dépenses nouvelles : porter le "
        "financement public à parité pour tous les élèves, majorer le "
        "montant versé pour l'élève défavorisé, et relever la rémunération "
        "des enseignants. Elle dispose de deux ressources : la baisse "
        "démographique, et le réalignement de la dépense par lycéen sur ce "
        "que font les autres pays.</p>"
        "<p>Les trois dépenses ne se déploient pas au même rythme, et c'est "
        "ce qui rend le calendrier de la page "
        f'<a href="{g.lien("proposition")}">La proposition</a> aussi '
        "important que les montants.</p>"
    )

    corps += "<h2 id=\"couts\">Ce que ça coûte</h2>"
    corps += "<h3 class=\"serif\">1. Le financement à parité</h3>"
    corps += (
        "<p>C'est le poste principal, et le moins discuté par les partisans "
        "de la liberté scolaire — qui présentent volontiers leur réforme "
        "comme gratuite. Elle ne l'est pas. Aujourd'hui, un élève du privé "
        f"sous contrat coûte moins à l'État qu'un élève du public : "
        f"{v('prive_cout_etat_primaire')} contre "
        f"{v('public_cout_etat_primaire')} dans le premier degré, d'après la "
        "Cour des comptes. <strong>Verser le même montant pour tous, c'est "
        "combler cet écart, et donc dépenser davantage.</strong></p>"
    )
    corps += g.tableau(
        "Le coût du financement à parité, par an, à la fin du déploiement",
        ("Ligne", "Calcul", "Ordre de grandeur"),
        (
            ("Élèves du premier degré dans le privé sous contrat",
             f"{v('eleves_premier_degre')} × {v('prive_premier_degre')}",
             "≈ 840 000"),
            ("Écart de financement par élève, premier degré",
             f"{v('public_cout_etat_primaire')} − "
             f"{v('prive_cout_etat_primaire')}",
             "≈ 1 970 €"),
            ("Coût du premier degré", "840 000 × 1 970 €", "≈ 1,7 Md€"),
            ("Élèves du second degré dans le privé sous contrat",
             f"{v('eleves_second_degre')} × {v('prive_second_degre')}",
             "≈ 1 190 000"),
            ("Écart de financement par élève, second degré",
             "hypothèse dérivée des parts de budget publiées par la Cour : "
             f"l'État couvre {v('prive_budget_etat_secondaire')} du budget "
             f"du privé contre {v('public_budget_etat_secondaire')} de "
             "celui du public, soit six points d'écart — d'où une "
             "fourchette de 1 000 à 2 000 €",
             "1,2 à 2,4 Md€"),
            ("Total", "", "3 à 4 Md€ par an"),
        ),
        ("long", "long", "nombre"),
    )
    corps += g.note(
        "<p><strong>L'hypothèse contestable est la deuxième</strong>, et "
        "c'est la seule du tableau. La Cour des comptes publie l'écart en "
        "euros pour le premier degré, mais pas pour le second : elle y "
        f"donne des parts de budget ({v('prive_budget_etat_secondaire')} "
        f"pour le privé, {v('public_budget_etat_secondaire')} pour le "
        "public). Nous en déduisons une "
        "fourchette, et nous la présentons comme une déduction.</p>"
        "<p>Un point que ce tableau ne dit pas assez fort : <strong>si le "
        "privé sous contrat coûte moins cher, c'est aussi parce qu'il "
        "dépense moins</strong> — classes plus chargées, enseignants plus "
        "souvent contractuels, pas de remplaçants. Financer à parité ne "
        "fait donc pas que déplacer de l'argent : cela porte la dépense par "
        f"élève du privé vers celle du public. Dit sans détour, nous "
        f"proposons de verser 3 à 4 Md€ de plus à un réseau dont "
        f"{v('prive_catholique')} des élèves sont dans une école "
        "catholique. Qui trouve cela inacceptable a une objection réelle, "
        "et nous préférons qu'il la formule sur ce chiffre-là que sur un "
        "chiffre que nous aurions tu. "
        f'<a href="{g.DEPOT}/issues">L\'adresse pour nous corriger est '
        "ici</a>.</p>",
        "vigilance",
    )

    corps += "<h3 class=\"serif\">2. La pondération sociale</h3>"
    corps += (
        "<p>Elle ne coûte rien — et c'est précisément ce qui la rend "
        "douloureuse. <strong class=\"cle-texte\">Majorer le montant versé "
        "pour l'élève défavorisé sans augmenter l'enveloppe, c'est diminuer "
        "celui versé pour les autres.</strong> Le calcul est immédiat : si "
        "l'on retient le quart des élèves les moins favorisés et qu'on "
        "majore leur dotation de 40 %, les trois autres quarts voient la "
        "leur baisser d'environ 13 %.</p>"
        "<p>Nous ne connaissons aucune manière d'éviter cela, et nous ne "
        "cherchons pas à la masquer. C'est le cœur de la réforme : un "
        "établissement qui accueille des élèves favorisés reçoit moins qu'il "
        "ne reçoit aujourd'hui. Le lecteur dont l'enfant est scolarisé dans "
        "un tel établissement sait maintenant ce que nous lui proposons.</p>"
    )

    corps += "<h3 class=\"serif\">3. La rémunération des enseignants</h3>"
    corps += (
        "<p>C'est le poste le plus lourd, et celui sans lequel rien d'autre "
        "ne tient. Le salaire effectif d'un professeur des écoles français "
        f"est inférieur de {v('salaire_ecart_elementaire')} à celui des "
        "autres diplômés du supérieur, contre "
        f"{v('salaire_ecart_elementaire_ocde')} en moyenne dans l'OCDE. "
        "Combler seulement cet écart-là — non pas rattraper les autres "
        "diplômés, mais rejoindre la position relative moyenne de "
        "l'OCDE — demande une hausse d'environ 12 % de la rémunération "
        "enseignante.</p>"
        "<p>Appliquée à une masse salariale enseignante que nous supposons "
        f"de l'ordre de 50 Md€ — la mission Enseignement scolaire pèse "
        f"{v('budget_mission')} hors pensions, dont l'essentiel en "
        "salaires —, cette hausse coûte <strong>environ 6 Md€ par "
        "an</strong>. Les 50 Md€ sont une hypothèse de notre part, pas un "
        "chiffre publié.</p>"
    )

    corps += "<h2 id=\"ressources\">Ce qui le finance</h2>"
    corps += "<h3 class=\"serif\">1. La baisse démographique</h3>"
    corps += (
        f"<p>Le système scolaire doit perdre {v('demographie')} d'ici 2035. "
        "À dépense par élève inchangée, la tentation est de multiplier ce "
        "nombre par le coût moyen et d'annoncer une quinzaine de milliards. "
        "<strong>Ce serait faux, et c'est nous-mêmes qui avons expliqué "
        "pourquoi</strong> : la page "
        f'<a href="{g.lien("comparaisons")}">Ailleurs en Europe</a> raconte '
        "comment les communes suédoises se sont retrouvées avec des écoles à "
        "demi vides dont les coûts fixes ne baissaient pas. Les murs, le "
        "chauffage, la direction et l'entretien ne suivent pas les "
        "effectifs.</p>"
        "<p>Seule la part variable — pour l'essentiel les postes "
        "d'enseignant — se libère réellement. Nous retenons l'hypothèse "
        "qu'elle représente environ 60 % de la dépense par élève.</p>"
    )
    corps += g.tableau(
        "Ce que la démographie libère réellement d'ici 2035",
        ("Ligne", "Calcul", "Ordre de grandeur"),
        (
            ("Élèves en moins d'ici 2035", "projection DEPP",
             v("demographie")),
            ("Dépense par élève, premier degré", "chiffre DEPP",
             v("die_premier_degre")),
            ("Part variable retenue", "hypothèse : 60 %", "≈ 5 450 €"),
            ("Ressource annuelle à l'horizon 2035",
             "1,7 million × 5 450 €", "≈ 9 Md€"),
        ),
        ("long", "long", "nombre"),
    )
    corps += g.note(
        "<p>Cette ressource <strong>n'existe pas encore</strong>. Elle "
        "arrive par tranches, au rythme des générations, sur dix ans. Une "
        "réforme qui dépenserait tout de suite ce que la démographie "
        "rapportera en 2035 serait financée à crédit, et il faut le dire.</p>",
        "vigilance",
    )

    corps += "<h3 class=\"serif\">2. Le réalignement du lycée</h3>"
    corps += (
        f"<p>La France dépense {v('ocde_lycee_fr')} par lycéen contre "
        f"{v('ocde_lycee_ocde')} en moyenne dans l'OCDE, soit "
        f"{v('ocde_ecart_lycee')} — quand elle dépense "
        f"{v('ocde_ecart_elementaire')} que cette moyenne par écolier. "
        "Ramener la dépense par lycéen à la moyenne de l'OCDE, et porter "
        "l'écart sur l'élémentaire, est la seconde ressource de ce "
        "programme. Elle ne demande pas un euro de plus : elle déplace.</p>"
        "<p>Nous ne chiffrons pas ce transfert à l'euro, faute de connaître "
        "la répartition exacte des effectifs du second cycle. Nous indiquons "
        "seulement son sens et son ampleur : de l'ordre d'un quart de la "
        "dépense par élève du second cycle du secondaire.</p>"
    )

    corps += "<h2 id=\"perdant\">Qui paie</h2>"
    corps += g.encadre(
        "<h3 class=\"serif\">Les trois perdants, nommés</h3>"
        "<p>Un programme sans perdant est un programme qui ment. Voici les "
        "nôtres.</p>"
        "<p><strong>Les familles favorisées.</strong> La pondération sociale "
        "abaisse d'environ 13 % la dotation attachée à un élève qui n'est "
        "pas défavorisé. Les établissements qui en accueillent beaucoup "
        "recevront moins qu'aujourd'hui.</p>"
        "<p><strong>Le second cycle du secondaire.</strong> Le lycée général "
        "et technologique, et au premier chef les classes préparatoires, "
        f"dont l'élève reçoit {v('die_cpge')} quand l'écolier en reçoit "
        f"{v('die_premier_degre')}. Moins d'options, des groupes moins "
        "dédoublés, une carte des formations resserrée : c'est le prix de "
        "l'école primaire.</p>"
        "<p><strong>L'administration centrale et académique.</strong> "
        "L'autonomie des établissements retire leur objet à une partie des "
        "fonctions d'affectation, de dotation horaire et de contrôle "
        "a priori. Nous ne prétendons pas que ces postes disparaissent sans "
        "douleur ni sans conflit.</p>"
    )

    corps += "<h2 id=\"bilan\">Le bilan, et son trou</h2>"
    corps += g.tableau(
        "Le compte, à l'horizon 2035, en milliards d'euros par an",
        ("", "Dépense", "Ressource"),
        (
            ("Financement à parité", "3 à 4", "—"),
            ("Pondération sociale", "0 (redéploiement interne)", "—"),
            ("Rémunération des enseignants", "≈ 6", "—"),
            ("Baisse démographique (part variable)", "—", "≈ 9"),
            ("Réalignement du lycée", "—", "non chiffré, positif"),
            ("Total", "9 à 10", "9 et plus"),
        ),
        ("long", "nombre", "nombre"),
    )
    corps += (
        "<p>Le compte tombe juste à l'horizon 2035, et <strong>il ne tombe "
        "juste qu'à cet horizon</strong>. C'est le trou de ce programme, et "
        "nous préférons l'écrire que le laisser trouver : entre la première "
        "année et la dixième, les dépenses arrivent plus vite que la "
        "ressource démographique.</p>"
        "<p>Nous en tirons une conséquence sur le calendrier plutôt qu'une "
        "pirouette. Les deux premières années ne coûtent presque rien — "
        "publier des résultats et des comptes, donner de l'autonomie à des "
        "académies volontaires. Le financement à parité, qui est le poste "
        "coûteux, vient en quatrième année, quand la démographie a déjà "
        "commencé à rendre. <strong class=\"cle-texte\">L'ordre des réformes "
        "n'est pas une prudence politique : c'est une contrainte de "
        "trésorerie.</strong></p>"
    )

    corps += "<h2 id=\"limites\">Ce que ce calcul ne prouve pas</h2>"
    corps += g.note(
        "<p>Il ne prouve pas que la réforme est finançable. Il établit "
        "qu'elle est <em>plausiblement</em> finançable à l'horizon d'une "
        "décennie, sous trois hypothèses que nous avons écrites en toutes "
        "lettres : l'écart de financement au second degré, la part variable "
        "de la dépense, et la masse salariale enseignante. Aucune n'est "
        "publiée telle quelle ; chacune peut être fausse.</p>"
        "<p>Il ne dit rien non plus des coûts de transition — systèmes "
        "d'information, double régime statutaire pendant vingt ans, "
        "accompagnement des établissements qui perdent des élèves. Ces "
        "coûts existent, nous ne savons pas les évaluer, et ils vont dans "
        "le mauvais sens.</p>"
        "<p>Ce qu'on peut nous opposer de plus fort, c'est qu'un "
        "gouvernement disposant de la direction du budget ferait ce calcul "
        "mieux que nous. C'est exact. Nous demandons qu'il le fasse, et "
        "qu'il le publie.</p>",
        "vigilance",
    )
    return corps


def comparaisons() -> str:
    corps = g.affiche(
        "La proposition · le précédent",
        "Ce que la liberté scolaire donne, en bien et en mal.",
        "Quatre pays européens ont, chacun à sa manière, séparé le "
        "financement de l'école de sa propriété. Deux l'ont bien fait. Un "
        "l'a fait autrement. Un l'a mal fait — et c'est de celui-là que nous "
        "avons le plus appris.",
    )

    corps += g.plan((
        ("paysbas", "Pays-Bas"),
        ("danemark", "Danemark"),
        ("estonie", "Estonie"),
        ("suede", "Suède"),
        ("lecons", "Les leçons"),
    ))

    corps += g.tableau(
        "Quatre systèmes, et ce qu'ils font de l'argent public",
        ("Pays", "Financement du non-public", "Sélection à l'entrée",
         "Résultat"),
        (
            ("Pays-Bas", "Intégral, constitutionnel depuis "
             + v("paysbas_article23"), "Interdite pour les écoles financées",
             "Au-dessus de la moyenne OCDE, stable"),
            ("Danemark", v("danemark_prive") + " des élèves, financés à "
             + v("danemark_financement"), "Encadrée",
             "Au-dessus de la moyenne OCDE"),
            ("Estonie", "Écoles publiques très autonomes",
             "Interdite", v("estonie_pisa") + " en mathématiques, premier "
             "rang européen"),
            ("Suède", "Intégral depuis " + v("suede_reforme") + ", y compris "
             "à but lucratif", "Files d'attente, de fait sélectives",
             "Ségrégation en hausse, notes gonflées, résultats en recul"),
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
        "<p>Ce système n'a pas produit d'école à deux vitesses : les écoles "
        "financées ne peuvent pas sélectionner, l'inspection publie ses "
        "rapports établissement par établissement, et les Pays-Bas restent "
        "au-dessus de la moyenne de l'OCDE. C'est le précédent le plus "
        "proche de notre proposition, et le plus long — plus d'un siècle, "
        "dans un pays qui n'a jamais cessé d'être un État social.</p>"
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
        "montre aussi, et que nous ne reprenons pas : un reste à charge "
        "familial, même modeste, filtre. <strong class=\"cle-texte\">Notre "
        "proposition finance à 100 %, précisément pour que le choix ne "
        "dépende pas du revenu.</strong></p>"
    )

    corps += "<h2 id=\"estonie\">Estonie : l'autonomie sans le marché</h2>"
    corps += (
        f"<p>L'Estonie obtient {v('estonie_pisa')} en mathématiques aux "
        "épreuves PISA 2022 : le premier rang européen, et le troisième rang "
        "des pays de l'OCDE derrière le Japon et la Corée — avec une dépense "
        "par élève inférieure à la française. Son école est pourtant très "
        "majoritairement publique.</p>"
        "<p>Un mot sur ce « premier rang européen », parce que nous nous "
        "sommes imposé une règle et qu'elle vaut aussi contre nous : "
        "l'Estonie devance la Suisse de deux points, <strong>un écart "
        "inférieur à la marge d'erreur de l'enquête</strong>. Les deux pays "
        "ne sont pas départagés, et c'est le niveau estonien qui nous "
        "intéresse ici, non sa place sur un podium.</p>"
        f"<p>Ce qu'elle a, et que nous n'avons pas : {v('estonie_recrutement')} "
        "des élèves sont dans un établissement dont le directeur recrute "
        "lui-même son équipe et répartit lui-même son enveloppe. Le cadre "
        "national dit ce qui doit être appris ; l'école décide comment, et "
        "répond des résultats.</p>"
        "<p>C'est le contre-exemple utile à notre propre camp : <strong>"
        "l'essentiel du gain estonien ne vient pas de la concurrence entre "
        "écoles, mais de l'autonomie et de la responsabilité de chacune</strong>. "
        "La réforme 3 de notre proposition compte davantage que la "
        "réforme 1, et c'est elle qui pourrait commencer dès l'an "
        "prochain.</p>"
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
        "scolaire, elle, reste discutée.",
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
         "L'Estonie obtient les meilleurs résultats d'Europe avec une école "
         "presque entièrement publique, mais très autonome. C'est le levier "
         "le plus sûr, et le moins coûteux politiquement."),
        ("La liberté sans le tri",
         "Pays-Bas et Danemark financent largement le non-public depuis des "
         "décennies sans produire d'école à deux vitesses, parce que les "
         "écoles financées ne choisissent pas leurs élèves."),
        ("Le financement décide du reste",
         "La différence entre le modèle néerlandais et le modèle suédois "
         "n'est pas l'ampleur de la liberté : c'est la manière dont l'argent "
         "est attaché à l'élève, et ce qu'on exige en échange."),
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


# -- la confiance ------------------------------------------------------------


def objections() -> str:
    corps = g.affiche(
        "La confiance · 1",
        "Les objections, y compris celles qui ont raison.",
        "Quatorze objections sérieuses à ce programme. Nous les formulons "
        "dans leur version la plus forte, et non dans leur caricature — six "
        "d'entre elles, à notre avis, touchent juste.",
    )

    corps += g.note(
        "<p>Une proposition politique qui ne publie pas ses points faibles "
        "demande qu'on lui fasse confiance sur parole. Celle-ci les publie. "
        "Six objections nous paraissent fondées, en tout ou en partie — "
        "l'écrémage, le refus des enseignants, l'absence de preuve "
        "française, l'école du village, les élèves handicapés, et le refus "
        "probable de l'enseignement catholique. Nous le disons à l'endroit "
        "où on les lit, et non dans une note de bas de page.</p>",
        "resume",
    )

    corps += g.section_cle(
        "deux-vitesses",
        "N'est-ce pas une école à deux vitesses ?",
        "Elle existe déjà, et elle se paie en mètres carrés. Le prix de "
        "l'immobilier intègre la qualité des établissements : ceux qui "
        "peuvent déménager choisissent leur école, les autres subissent la "
        "leur. Notre proposition ne crée pas le choix — elle le rend gratuit "
        "et le soumet à des règles écrites, avec interdiction de "
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
        "route.",
    )

    corps += g.section_cle(
        "moyens",
        "Il faudrait surtout donner plus de moyens.",
        "<strong>Objection partiellement fondée — et nous avons corrigé "
        "notre propre argument sur ce point.</strong> Nous écrivions que la "
        "France dépense plus que ses voisins. C'est faux là où cela compte "
        f"le plus : par écolier, elle dépense {v('ocde_elementaire_fr')} "
        f"contre {v('ocde_elementaire_ocde')} en moyenne dans l'OCDE. À ce "
        "niveau, la demande de moyens est fondée — et c'est précisément là "
        "que notre proposition redirige l'argent. Ce qui ne tient pas, c'est "
        "la demande de moyens <em>en général</em> : au lycée, la France "
        f"dépense {v('ocde_lycee_fr')} par élève contre "
        f"{v('ocde_lycee_ocde')} dans l'OCDE, un quart de plus, pour des "
        "résultats qui ne le sont pas. Et le dédoublement des classes, qui "
        f"coûte {v('dedoublement_cout')}, a produit des effets réels sans "
        "réduire l'écart avec le reste du système. Les moyens comptent, et "
        "ils manquent au "
        "primaire ; ailleurs, ils ne compensent pas une organisation qui "
        "empêche quiconque d'agir.",
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
        f"{v('prive_catholique')} des élèves du privé sous contrat sont "
        "dans une école catholique : vous allez financer la religion.",
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
        "C'est vrai, et c'est pourquoi la réforme 1 n'est pas la première du "
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
        "recevoir de bons élèves. La presse publiera de toute façon des "
        "classements : autant qu'ils reposent sur la bonne grandeur.",
    )

    corps += g.section_cle(
        "separatisme",
        "Vous allez financer des écoles séparatistes.",
        "C'est l'objection la plus lourde qui nous soit faite, et notre "
        "silence sur ce point aurait valu aveu. Voici la réponse, et elle "
        "est à notre avantage. Aujourd'hui, une école qui veut échapper au "
        "socle républicain ouvre hors contrat : elle choisit ses élèves, "
        "fixe ses tarifs, n'ouvre pas ses comptes, ne passe aucune "
        "évaluation externe, et le contrôle de l'État s'y limite à "
        "l'instruction. C'est dans cet espace-là que prospère ce que la loi "
        "du 24 août 2021 a cherché à contenir, en soumettant l'instruction "
        "en famille à autorisation et en renforçant le contrôle du hors "
        "contrat (" + _source("loi_2021") + "). <strong>Notre contrat "
        "unique fait "
        "exactement l'inverse</strong> : socle national enseigné en "
        "totalité, aucune sélection à l'entrée, évaluations nationales "
        "corrigées à l'extérieur, comptes publics, et une autorité "
        "indépendante qui peut retirer le financement. Un établissement qui "
        "voudrait trier ses élèves sur un critère religieux ou "
        "communautaire ne remplit pas le contrat, et n'est donc pas financé. "
        "Nous ne proposons pas d'ouvrir les vannes : nous proposons "
        "d'échanger de l'argent public contre un contrôle qui n'existe pas "
        "aujourd'hui, et de rendre le hors contrat moins attractif en "
        "rendant le contrat accessible.",
        "Voir la réforme 4 et la réforme 8, page « La proposition ».",
    )

    corps += g.section_cle(
        "ecole-du-village",
        "Le libre choix va fermer l'école du village.",
        "<strong>Objection fondée</strong>, et c'est nous qui en avons "
        "fourni la démonstration : notre page sur la Suède explique que les "
        "communes se sont retrouvées avec des écoles à demi vides dont les "
        "coûts fixes ne baissaient pas. Le même mécanisme jouerait ici, "
        "aggravé par une baisse démographique qui fermera des écoles de "
        "toute façon. Nous en tirons trois règles, et non une dénégation. "
        "D'abord, une <strong>dotation socle garantie</strong> sous un "
        "effectif plancher : en deçà, l'école est financée sur un forfait "
        "fixe et non au nombre d'élèves, parce qu'une école de village n'est "
        "pas divisible. Ensuite, aucune fermeture décidée par la seule "
        "arithmétique de la dotation : la décision revient à la commune et à "
        "l'autorité indépendante, sur des critères publiés. Enfin, le "
        "calendrier — le libre choix vient en quatrième année, après "
        "l'autonomie, qui est ce qui sert réellement à l'école rurale. Nous "
        "ne prétendons pas que cela suffira partout.",
    )

    corps += g.section_cle(
        "handicap",
        "Et les élèves handicapés, dans votre système ?",
        "<strong>Objection partiellement fondée : nous les avions traités "
        "en une incise, et ils méritent mieux.</strong> L'école inclusive "
        "française est aujourd'hui à la fois une obligation légale et une "
        "promesse mal tenue — des notifications qui ne sont pas honorées, "
        "des accompagnants payés à temps incomplet et sans carrière, des "
        "familles qui plaident pendant des mois. Un financement à l'élève "
        "sans pondération de handicap sérieuse rendrait ces enfants "
        "financièrement indésirables, et aggraverait tout. Nous proposons "
        "donc que la majoration de handicap soit <strong>attachée à la "
        "notification, versée à l'établissement qui scolarise "
        "effectivement</strong>, et d'un montant qui couvre le coût réel de "
        "l'accompagnement — condition sans laquelle l'établissement a "
        "intérêt à décourager l'inscription. L'accompagnement devient un "
        "emploi de l'établissement, à temps complet, inscrit dans sa "
        "dotation. L'ordre de grandeur est connu : l'école inclusive pèse "
        f"{v('inclusion_budget')} au budget 2026, dont "
        f"{v('inclusion_aesh')} pour la seule rémunération des "
        f"{v('aesh_nombre')} accompagnants, au bénéfice de "
        f"{v('eleves_handicap')} élèves — soit environ 9 000 € par élève "
        "accompagné, qui s'ajoutent au coût de sa scolarité ordinaire. "
        "<strong>C'est ce montant-là que la majoration de handicap doit "
        "reprendre</strong>, et il est déjà dans le budget de l'État : la "
        "réforme le transforme en dotation attachée à l'enfant au lieu "
        "d'un contingent d'emplois géré par le rectorat.",
        "Voir la réforme 2, page « La proposition ».",
    )

    corps += g.section_cle(
        "catholique",
        "L'enseignement catholique lui-même n'en veut pas.",
        "C'est probablement vrai, et il faut le dire puisque nous passons "
        "pour ses alliés. Le réseau catholique reçoit aujourd'hui "
        f"{v('prive_fonds_etat')} de l'État tout en conservant le droit de "
        "choisir ses élèves, de faire payer une contribution aux familles "
        "et de faire valoir son caractère propre. Notre contrat unique lui "
        "retire les trois : plus de sélection à l'entrée, plus de reste à "
        "charge, et un socle national intégralement opposable. En échange, "
        "il reçoit un financement à parité et la fin du contingentement. "
        "<strong class=\"cle-texte\">Nous proposons donc à nos supposés "
        "alliés un marché qu'ils ont de bonnes raisons de refuser</strong>, "
        "et à nos adversaires une laïcité plus exigeante qu'aujourd'hui. "
        "C'est inconfortable, et c'est la preuve que cette proposition "
        "n'est pas la défense d'un intérêt établi.",
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
        "fabrication : nous n'avons ni modèle ni estimation propre — "
        "seulement des citations, et leur mise en regard.",
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
        "annuelles. Un tableau qui met côte à côte un score de 2022 et une "
        "dépense de 2024 rapproche deux instants différents, et il faut le "
        "savoir.",
        "<strong>Les comparaisons internationales sont fragiles.</strong> "
        "Les pays ne scolarisent ni les mêmes élèves, ni au même âge, ni avec "
        "les mêmes définitions. Nous les utilisons pour des ordres de "
        "grandeur, jamais pour départager deux pays séparés de trois points.",
        "<strong>Les chiffres de gouvernance sont anciens.</strong> Les "
        "indicateurs de répartition des décisions datent de la dernière "
        "vague disponible ; la structure qu'ils décrivent n'a pas changé, "
        "mais les pourcentages précis, eux, peuvent avoir bougé.",
        "<strong>Les propositions ne sont pas chiffrées à l'euro.</strong> "
        "Nous affirmons qu'elles tiennent à enveloppe constante ; nous "
        "n'avons pas construit le modèle budgétaire qui le démontrerait, et "
        "nous ne prétendons pas le contraire.",
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
    "chiffrage": chiffrage,
    "comparaisons": comparaisons,
    "objections": objections,
    "sources": sources_page,
}

__all__ = ["PAGES", "CHIFFRES"]
