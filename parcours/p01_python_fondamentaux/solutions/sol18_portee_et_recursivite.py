"""Solutions 5.3 — Portée et récursivité."""

TVA = 18  # constante globale (MAJUSCULES)


def prix_ttc(prix_ht: float) -> float:
    return prix_ht * (1 + TVA / 100)  # lecture d'une globale : OK


def incrementer(compteur: int, pas: int = 1) -> int:
    return compteur + pas


def ajouter_sans_modifier(liste: list, element: object) -> list:
    return [*liste, element]  # nouvelle liste ; l'originale est intacte


def factorielle(n: int) -> int:
    if n <= 1:  # cas de base
        return 1
    return n * factorielle(n - 1)


def somme_recursive(n: int) -> int:
    if n <= 0:
        return 0
    return n + somme_recursive(n - 1)


def puissance(base: float, exposant: int) -> float:
    if exposant == 0:
        return 1
    return base * puissance(base, exposant - 1)


def inverser(texte: str) -> str:
    if len(texte) <= 1:
        return texte
    return inverser(texte[1:]) + texte[0]


def fibonacci(n: int) -> int:
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent


def pgcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return pgcd(b, a % b)
