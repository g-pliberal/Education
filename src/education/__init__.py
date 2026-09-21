"""Le site « École » du Parti libéral français.

Le site est fait de pages statiques : aucun script ne tourne chez le lecteur,
rien n'est envoyé nulle part. `scripts/construire_site.py` les écrit à partir
de trois modules — les chiffres (`donnees`), le gabarit (`gabarit`), le texte
(`pages`).
"""

__all__ = ["donnees", "gabarit", "pages"]
