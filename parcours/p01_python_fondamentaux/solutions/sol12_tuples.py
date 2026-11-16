"""Solutions 4.2 — Les tuples."""


def echanger(couple: tuple) -> tuple:
    a, b = couple
    return b, a


def diviser(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b


def formater_date(date: tuple[int, int, int]) -> str:
    jour, mois, annee = date
    return f"{jour:02d}/{mois:02d}/{annee}"


def distance(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


def associer(produits: list[str], prix: list[float]) -> list[tuple[str, float]]:
    resultat = []
    for produit, p in zip(produits, prix, strict=True):
        resultat.append((produit, p))
    return resultat


def chiffre_affaires(ventes: list[tuple[str, int, float]]) -> float:
    total = 0
    for _produit, quantite, prix_unitaire in ventes:
        total += quantite * prix_unitaire
    return total


def resume(elements: list) -> tuple:
    premier, *milieu, dernier = elements
    return premier, dernier, len(milieu)
