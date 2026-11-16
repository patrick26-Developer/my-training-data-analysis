"""Fonctions mathématiques réutilisables."""


def moyenne(nombres: list[float]) -> float:
    """Moyenne arithmétique ; 0.0 pour une liste vide."""
    return sum(nombres) / len(nombres) if nombres else 0.0


def pgcd(a: int, b: int) -> int:
    """Plus grand commun diviseur (algorithme d'Euclide)."""
    while b:
        a, b = b, a % b
    return a
