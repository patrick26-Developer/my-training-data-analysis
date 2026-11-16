"""Fonctions de traitement de texte réutilisables."""


def nettoyer_nom(nom: str) -> str:
    """Retire les espaces superflus et met une majuscule à chaque mot."""
    return " ".join(nom.split()).title()


def est_palindrome(texte: str) -> bool:
    """Vrai si le texte se lit pareil dans les deux sens (lettres et chiffres seulement)."""
    nettoye = [c.lower() for c in texte if c.isalnum()]
    return nettoye == nettoye[::-1]
