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
from .donnees import CHIFFRES, par_theme, sources, valeur as v

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
        "son école un effort comparable à celui de ses voisins, et le "
        "répartit à contretemps : moins que la moyenne de l'OCDE par "
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
         f"ordinaire : {v('ocde_pib_comparable')}. Mais la France dépense "
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
         "français les plus favorisés des plus défavorisés. Le système qui se "
         "réclame le plus de l'égalité est l'un de ceux où l'origine sociale "
         "pèse le plus lourd. Ce n'est pas un accident de parcours : c'est "
         "ce qu'il produit."),
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
         "Sept réformes, leur calendrier, leur coût et leurs garde-fous. "
         f'<a href="{g.lien("proposition")}">La proposition</a>, et '
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
                 "sous le niveau 2 en mathématiques, contre 21 % en 2018."),
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
        "désormais sous le niveau 2 en mathématiques, contre 21 % quatre ans "
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
            ("Compréhension de l'écrit", v("pisa_lecture"), "476 points",
             "−19 points"),
            ("Culture scientifique", v("pisa_sciences"), "485 points",
             "stable"),
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
        f"{v('timss_cm1_sciences')} contre 518 dans l'Union. En quatrième, "
        f"{v('timss_quatrieme_maths')} contre 507.</p>"
        "<p>Ces scores sont <em>stables</em> depuis 2019. C'est la phrase la "
        "plus grave du rapport : le décrochage français n'est plus une chute, "
        "c'est un palier. Nous nous sommes installés en bas.</p>"
    )

    corps += "<h2 id=\"pirls\">PIRLS : lire en CM1</h2>"
    corps += (
        f"<p>PIRLS mesure la compréhension de l'écrit en CM1. La France y "
        f"obtient {v('pirls')}, contre 527 en moyenne européenne. C'est la "
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
        "843 500 jeunes en 2024 — au moment où l'école les a quittés. Le "
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
        "<h3 class=\"serif\">Un sur vingt, ce n'est pas une statistique</h3>"
        "<p>Un jeune sur vingt en situation d'illettrisme, sur une classe "
        "d'âge d'environ 800 000 personnes, cela fait <strong "
        "class=\"cle-texte\">quarante mille jeunes par an</strong> qui "
        "sortent de treize années de scolarité obligatoire sans savoir lire "
        "un mode d'emploi. À l'échelle d'un quinquennat, deux cent mille. "
        "Aucun chiffre de dépense ne pèse contre celui-là.</p>"
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
                 f"{v('die_pib')}, en hausse de 1,4 % en euros constants sur "
                 "un an."),
        g.Repere("Par élève ou étudiant", v("die_par_eleve"),
                 "tous niveaux confondus, apprentissage compris."),
        g.Repere("Mission Enseignement scolaire", v("budget_mission_pensions"),
                 f"pensions comprises ({v('budget_mission')} hors pensions) : "
                 "le premier budget de l'État."),
    ))

    corps += "<h2 id=\"combien\">Un effort ordinaire, réparti à contretemps</h2>"
    corps += (
        f"<p>La dépense intérieure d'éducation atteint {v('die_montant')} en "
        f"2024, soit {v('die_pib')}. Ce chiffre est un agrégat français : il "
        "compte tout ce que la nation consacre à l'éducation, cantines, "
        "transports scolaires et formation continue compris. <strong>Il ne "
        "se compare donc pas aux moyennes internationales, et nous ne le "
        "comparons pas.</strong> Sur le périmètre retenu par l'OCDE — les "
        "seuls établissements d'enseignement —, la France consacre "
        f"{v('ocde_pib_comparable')} à son école et à son supérieur, ce qui "
        "la situe dans la moyenne des pays comparables.</p>"
        "<p>Rapportée à l'élève, cette dépense dit quelque chose de plus "
        "précis, et de plus embarrassant, qu'un total.</p>"
    )
    corps += g.tableau(
        "Dépense annuelle par élève, France et moyenne OCDE, en 2022 "
        "(équivalents USD, à parité de pouvoir d'achat)",
        ("Niveau", "France", "Moyenne OCDE", "Écart"),
        (
            ("Élémentaire", v("ocde_elementaire_fr"),
             v("ocde_elementaire_ocde"), "−13 %"),
            ("Collège", v("ocde_college_fr"), v("ocde_college_ocde"), "−5 %"),
            ("Lycée", v("ocde_lycee_fr"), v("ocde_lycee_ocde"), "+24 %"),
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
        "<p>Or tout ce que l'on sait de l'efficacité de la dépense éducative "
        "va dans l'autre sens : c'est dans les premières années que l'euro "
        "investi rapporte le plus, parce qu'un enfant qui ne lit pas en CE1 "
        "ne rattrape presque jamais. Le Conseil d'analyse économique, en "
        "2025, classe précisément les dépenses éducatives par leur rendement "
        "social net, et place les premières années en tête.</p>"
    )

    corps += "<h2 id=\"qui-paie\">Qui paie, et pour qui</h2>"
    corps += g.tableau(
        "Les financeurs de la dépense d'éducation, en 2024 (DEPP)",
        ("Financeur", "Part"),
        (
            ("État", v("die_etat")),
            ("Collectivités territoriales", v("die_collectivites")),
            ("Entreprises", "10 %"),
            ("Ménages", v("die_menages")),
            ("Autres administrations publiques", "4 %"),
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
         "<p>Engagé en 2017, le dédoublement a ramené les classes de CP puis "
         "de CE1 en REP et REP+ à une douzaine d'élèves. Son coût annuel est "
         f"estimé à {v('dedoublement_cout')} par la Cour des comptes, pour "
         "16 000 équivalents temps plein.</p>"
         "<p>Les évaluations de la DEPP montrent des effets positifs "
         "mesurables à la fin du CP, <strong>qui ne persistent pas</strong> : "
         "au-delà de la première année, l'effet supplémentaire n'est plus "
         "significatif. Réduire la taille des classes fonctionne, mais "
         "beaucoup moins que son coût ne le laissait espérer — et le facteur "
         "décisif, dans toute la littérature, reste ce que l'enseignant fait "
         "de ces élèves, non leur nombre.</p>"),
        ("Les groupes de niveau puis de besoins au collège",
         "<p>Annoncés en 2023 sous le nom de « choc des savoirs », mis en "
         "place à la rentrée 2024 en sixième et cinquième, les groupes de "
         "besoins en français et en mathématiques devaient relever le niveau "
         "par un enseignement différencié.</p>"
         "<p>Le rapport de l'inspection générale de juin 2025 conclut que les "
         "effets sur les apprentissages ne sont pas significatifs et que les "
         "écarts entre élèves se creusent. L'obligation a été levée par "
         "décret en mars 2026, après dix-huit mois de réorganisation des "
         "emplois du temps de tous les collèges de France.</p>"
         "<p>La leçon n'est pas que la mesure était mauvaise. C'est qu'un "
         "dispositif uniforme, décidé au centre et imposé à onze mille "
         "collèges qui n'ont ni les mêmes élèves ni les mêmes équipes, ne "
         "peut pas produire autre chose qu'une moyenne nulle.</p>"),
    ))

    corps += "<h2 id=\"demographie\">La marge de manœuvre arrive toute seule</h2>"
    corps += (
        f"<p>Les projections du ministère annoncent {v('demographie')} d'ici "
        "2035. À dépense constante, cela signifie mécaniquement un "
        "desserrement considérable : davantage d'adultes par enfant, sans "
        "un euro de plus.</p>"
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
                 "dont 2 % seulement en pleine autonomie."),
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
            ("Pays-Bas", "64 %"),
            ("Royaume-Uni", "81 %"),
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
    )

    corps += "<h2 id=\"enseignants\">Un métier qu'on n'a pas les moyens de rendre attractif</h2>"
    corps += (
        "<p>Les enseignants français sont, rapportés aux autres diplômés du "
        "supérieur de leur pays, parmi les moins bien payés de l'OCDE : leur "
        f"salaire effectif est inférieur de {v('salaire_ecart_elementaire')} "
        "à celui des autres diplômés dans l'élémentaire et de "
        f"{v('salaire_ecart_college')} au collège, contre respectivement "
        "17 % et 13 % en moyenne dans l'OCDE.</p>"
        "<p>Dans le même temps, ils enseignent davantage d'heures que leurs "
        f"collègues : {v('heures_elementaire')} d'enseignement obligatoire "
        f"par an dans l'élémentaire contre 804 en moyenne, "
        f"{v('heures_college')} au collège contre 909. Et la taille moyenne "
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
        "Sept réformes, à enveloppe constante. Aucune n'est nouvelle : "
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
        "majoré d'environ 40 % pour un élève d'origine défavorisée, et d'un "
        "montant calculé pour un élève en situation de handicap ou "
        "allophone. Un établissement a alors un intérêt financier direct à "
        "accueillir les élèves que le système actuel se renvoie, et à les "
        "faire progresser — puisque l'évaluation (réforme 5) mesure la "
        "valeur ajoutée et non le niveau brut.</p>"
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
        "supérieur dans l'élémentaire, contre 17 % en moyenne dans "
        "l'OCDE.</p>"
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
        "qui le demandent. Une réforme qui prétendrait changer le statut de "
        "850 000 agents du jour au lendemain n'est pas une réforme : c'est "
        "un slogan.</p>",
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
        f"{v('heures_elementaire')} par an dans l'élémentaire, contre 804 en "
        "moyenne dans l'OCDE. Nous enseignons plus longtemps, sur un "
        "programme plus large, et nous obtenons "
        f"{v('timss_cm1_maths')} en mathématiques en CM1. La contrainte n'est "
        "pas le temps disponible : c'est ce qu'on y met.</p>"
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
             "environ 75 %", "Encadrée",
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
        "Environ deux tiers des élèves néerlandais fréquentent une école "
        "non publique — confessionnelle, Montessori, Dalton, Jenaplan — "
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
        "<em>friskole</em> ou une école privée. L'État en finance environ "
        "75 % ; le reste est à la charge des familles, avec des barèmes "
        "sociaux. Un groupe de parents peut fonder une école et obtenir ce "
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
        "Dix objections sérieuses à ce programme. Nous les formulons dans "
        "leur version la plus forte, et non dans leur caricature — trois "
        "d'entre elles, à notre avis, touchent juste.",
    )

    corps += g.note(
        "<p>Une proposition politique qui ne publie pas ses points faibles "
        "demande qu'on lui fasse confiance sur parole. Celle-ci les publie. "
        "Les objections 3, 8 et 10 nous paraissent fondées, en tout ou en "
        "partie, et nous le disons à l'endroit où on les lit.</p>",
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
        f"coûte {v('dedoublement_cout')}, a produit des effets réels mais "
        "qui ne persistent pas. Les moyens comptent, et ils manquent au "
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
    "comparaisons": comparaisons,
    "objections": objections,
    "sources": sources_page,
}

__all__ = ["PAGES", "CHIFFRES"]
