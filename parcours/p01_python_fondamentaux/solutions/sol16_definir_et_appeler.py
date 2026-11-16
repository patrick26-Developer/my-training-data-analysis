"""Solutions 5.1 — Définir et appeler une fonction."""


def aire_rectangle(longueur: float, largeur: float) -> float:
    return longueur * largeur


def prix_ttc(prix_ht: float, taux: float) -> float:
    return prix_ht * (1 + taux / 100)


def celsius_en_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def est_pair(n: int) -> bool:
    return n % 2 == 0


def stats(nombres: list[float]) -> tuple[float, float, float]:
    return min(nombres), max(nombres), sum(nombres) / len(nombres)


def salutation(nom: str, heure: int) -> str:
    if heure < 18:
        return f"Bonjour, {nom} !"
    return f"Bonsoir, {nom} !"


def total_panier(prix: list[float], taux: float) -> int:
    total = 0.0
    for p in prix:
        total += prix_ttc(p, taux)  # on réutilise la fonction précédente
    return round(total)


def moyenne_ponderee(notes: list[float], coefficients: list[float]) -> float:
    """Retourne la moyenne des notes pondérée par les coefficients.

    notes         : liste de notes
    coefficients  : liste de coefficients de même taille
    """
    total = 0.0
    for note, coef in zip(notes, coefficients, strict=True):
        total += note * coef
    return total / sum(coefficients)
