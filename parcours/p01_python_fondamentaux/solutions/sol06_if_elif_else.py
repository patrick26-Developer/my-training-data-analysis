"""Solutions 2.2 — if, elif, else."""


def parite(nombre: int) -> str:
    if nombre % 2 == 0:
        return "pair"
    return "impair"


def mention(note: float) -> str:
    # Du plus restrictif au plus large : l'ordre est essentiel.
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    return "Ajourné"


def taux_remise(quantite: int) -> int:
    if quantite >= 50:
        return 10
    if quantite >= 10:
        return 5
    return 0


def prix_ticket(age: int) -> int:
    if age < 12:
        return 100
    if age < 65:
        return 200
    return 0


def plus_grand(a: float, b: float, c: float) -> float:
    plus = a
    if b > plus:
        plus = b
    if c > plus:
        plus = c
    return plus


def est_bissextile(annee: int) -> bool:
    if annee % 400 == 0:
        return True
    if annee % 100 == 0:
        return False
    return annee % 4 == 0


def type_triangle(a: float, b: float, c: float) -> str:
    if a == b == c:
        return "equilateral"
    if a in (b, c) or b == c:
        return "isocele"
    return "scalene"
