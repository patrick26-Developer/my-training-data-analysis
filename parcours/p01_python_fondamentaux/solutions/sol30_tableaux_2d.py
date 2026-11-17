"""Solutions 8.3 — Tableaux à deux dimensions."""

Tableau = list[list]


def creer_grille(lignes: int, colonnes: int, valeur: object = 0) -> Tableau:
    return [[valeur] * colonnes for _ in range(lignes)]


def colonne(tableau: Tableau, j: int) -> list:
    return [ligne[j] for ligne in tableau]


def totaux_lignes(tableau: Tableau) -> list:
    return [sum(ligne) for ligne in tableau]


def totaux_colonnes(tableau: Tableau) -> list:
    return [sum(col) for col in zip(*tableau, strict=True)]


def transposer(tableau: Tableau) -> Tableau:
    return [list(col) for col in zip(*tableau, strict=True)]


def somme_matrices(a: Tableau, b: Tableau) -> Tableau:
    return [[x + y for x, y in zip(la, lb, strict=True)] for la, lb in zip(a, b, strict=True)]


def produit_matrices(a: Tableau, b: Tableau) -> Tableau:
    colonnes_b = list(zip(*b, strict=True))
    return [
        [sum(x * y for x, y in zip(ligne, col, strict=True)) for col in colonnes_b] for ligne in a
    ]


def identite(n: int) -> Tableau:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def determinant_2x2(m: Tableau) -> float:
    (a, b), (c, d) = m
    return a * d - b * c


def determinant_3x3(m: Tableau) -> float:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def diagonale_principale(m: Tableau) -> list:
    return [m[i][i] for i in range(len(m))]


def trace(m: Tableau) -> float:
    return sum(diagonale_principale(m))


def tourner_90(m: Tableau) -> Tableau:
    return [ligne[::-1] for ligne in transposer(m)]


def gagnant_morpion(grille: Tableau) -> str | None:
    lignes = [list(ligne) for ligne in grille]
    colonnes = [list(col) for col in zip(*grille, strict=True)]
    diagonales = [[grille[i][i] for i in range(3)], [grille[i][2 - i] for i in range(3)]]
    for alignement in lignes + colonnes + diagonales:
        if alignement[0] != " " and alignement.count(alignement[0]) == 3:
            return alignement[0]
    return None
