# École : le programme libéral

**Le site du Parti libéral français sur la politique éducative.** Il fait deux
choses : établir ce que la politique scolaire française coûte et ce qu'elle
obtient, puis exposer l'alternative libérale.

Huit pages statiques, aucun script chez le lecteur, aucune requête vers un
tiers — ni police, ni mesure d'audience, ni bouton de réseau social. Le
lecteur d'un site politique n'a pas à être compté pour le lire.

| Page | Ce qu'elle contient |
|---|---|
| `index.html` | L'affiche, les trois repères, les six engagements |
| `resultats.html` | PISA, TIMSS, PIRLS, Journée défense et citoyenneté |
| `depense.html` | Où va l'argent : niveaux, financeurs, réformes évaluées |
| `gouvernance.html` | Qui décide : centralisation, recrutement, affectation |
| `proposition.html` | Les sept réformes, leur calendrier, leurs garde-fous |
| `comparaisons.html` | Pays-Bas, Danemark, Estonie, Suède |
| `objections.html` | Dix objections, dont trois que nous jugeons fondées |
| `sources.html` | Tous les chiffres, leur année, leur source |

## L'apparence

Elle est reprise du simulateur de retraite du même parti,
[`retraitecomptenotionelle`](https://github.com/g-pliberal/retraitecomptenotionelle) :
mêmes jetons de couleur, mêmes polices servies par le dépôt, même affiche de
tête, mêmes engagements numérotés. Deux outils du même parti doivent se
reconnaître comme tels — un électeur qui passe de l'un à l'autre ne doit pas
croire avoir changé de site.

Ce qui ne servait qu'au simulateur — graphiques, cascade, formulaire, barre de
partage — n'a pas été repris : une feuille de style qui décrit des composants
absents est une feuille qu'on n'ose plus modifier.

## Construire

```bash
python3 scripts/construire_site.py     # écrit les pages, la feuille, l'icône
python3 -m unittest discover -s tests  # vérifie ce que le site promet
```

Aucune dépendance : Python 3.11 et rien d'autre.

**Les fichiers publiés — `*.html`, `moteur/style.css`, `moteur/icone.svg` — ne
se modifient jamais à la main.** Ils sont produits par le script, et
versionnés pour que les pages GitHub les servent sans rien exécuter et que
quiconque puisse lire le HTML publié sans installer Python. Un test refuse le
dépôt dès qu'ils diffèrent de ce que le code produit
(`construire_site.py --verifier`).

## Où vivent les choses

```
src/education/donnees.py   les chiffres et les faits, avec leur source
src/education/gabarit.py   la feuille de style et les fragments HTML
src/education/pages.py     le texte des huit pages
scripts/construire_site.py écrit le site
tests/test_site.py         ce que le site doit tenir
```

### La règle des chiffres

Aucun chiffre ne s'écrit dans la prose. Une page qui cite la dépense
d'éducation ne tape pas « 197,1 Md€ » : elle demande `valeur("die_montant")`,
et le registre fournit la valeur, l'année, l'émetteur et l'adresse du
document. Trois conséquences, et c'est pour elles que la règle existe :

1. une faute de frappe dans un nom de chiffre **casse la construction**, au
   lieu d'écrire une phrase trouée ;
2. un chiffre corrigé l'est **partout d'un coup**, page « Sources » comprise,
   qui est construite à partir du même registre ;
3. un chiffre que plus aucune page ne cite **fait échouer les tests** — sans
   quoi le site accumulerait des chiffres sourcés qui n'étayent plus rien.

### La règle des faits

La règle des chiffres ne protégeait que les nombres. Or une page peut citer
tous ses chiffres et affirmer dans la même phrase qu'un rapport conclut ceci,
ou qu'un décret a fait cela — affirmations qu'un lecteur ne peut pas vérifier,
et que l'on défend mal après coup.

Ces affirmations vivent donc au même endroit, dans `FAITS` : un énoncé, son
année, son émetteur, l'adresse du document. Une page les cite par
`_source("cle")`, qui rend le lien. Les mêmes contraintes que pour les
chiffres s'appliquent : une clé inconnue casse la construction, un fait
inutilisé fait échouer les tests, et chacun figure sur la page « Sources ».

L'énoncé enregistré est ce que le document établit, **non ce qui arrangerait
la page**. C'est la seule contrainte qui vaille : elle a déjà obligé à retirer
une phrase qui faisait dire à une note du Conseil d'analyse économique
l'inverse de son propre périmètre.

### La typographie

Les espaces insécables du français — devant `; ! ?` et `:`, dans les
guillemets, entre un nombre et son unité — ne sont pas posées à la main : une
seule oubliée, et une page s'ouvre sur « 6,8 » suivi, à la ligne, de « % du
PIB ». Elles sont posées en une passe sur le HTML fini
(`gabarit.typographie`), qui ne touche jamais à ce qui se trouve entre `<`
et `>` — un test le vérifie, parce qu'une espace glissée dans un `href`
donnerait un lien mort que personne ne verrait.

## Ce que ce site n'est pas

Ce n'est pas un rapport officiel, et il ne se donne pas pour tel. Les
**constats** sont sourcés un par un et vérifiables ; les **propositions** sont
des choix politiques, et se discutent comme tels. Les limites que nous
connaissons à notre propre argumentation sont écrites sur le site lui-même,
pas cachées ici : voir la fin de `sources.html` et la page `objections.html`,
où trois objections sur dix sont données pour partiellement fondées.

Une erreur, un chiffre périmé, une objection oubliée :
[ouvrez une issue](https://github.com/g-pliberal/education/issues).

## Licences

Le code est sous licence Apache 2.0 (voir `LICENSE`). Les textes du site sont
sous [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).
Les polices — Public Sans et Instrument Serif — sont sous OFL, avec leurs
licences dans `moteur/polices/`.
