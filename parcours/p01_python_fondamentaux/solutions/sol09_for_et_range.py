"""Solutions 3.2 — for et range."""


def table_de_multiplication(n: int) -> str:
    lignes = []
    for i in range(1, 11):
        lignes.append(f"{n} x {i} = {n * i}")
    return "\n".join(lignes)


def somme_des_carres(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def compter_voyelles(texte: str) -> int:
    compteur = 0
    for lettre in texte.lower():
        if lettre in "aeiouy":
            compteur += 1
    return compteur


def compte_a_rebours(n: int) -> str:
    morceaux = []
    for i in range(n, 0, -1):
        morceaux.append(str(i))
    morceaux.append("Décollage !")
    return " ".join(morceaux)


def somme_des_pairs(n: int) -> int:
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total


def triangle(hauteur: int) -> str:
    lignes = []
    for i in range(1, hauteur + 1):
        lignes.append("*" * i)
    return "\n".join(lignes)


def est_premier(n: int) -> bool:
    if n < 2:
        return False
    for diviseur in range(2, n):
        if n % diviseur == 0:
            return False
    return True
