"""Solutions 3.3 — break, continue et boucles imbriquées."""


def premier_carre_superieur(limite: int) -> int:
    n = 1
    while True:
        if n * n > limite:
            break
        n += 1
    return n


def somme_sans_multiples_de_3(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        total += i
    return total


def premier_mot(texte: str) -> str:
    mot = ""
    for lettre in texte:
        if lettre == " ":
            break
        mot += lettre
    return mot


def table_carree(n: int) -> str:
    rangees = []
    for ligne in range(1, n + 1):
        valeurs = []
        for colonne in range(1, n + 1):
            valeurs.append(str(ligne * colonne))
        rangees.append(" ".join(valeurs))
    return "\n".join(rangees)


def nombres_premiers(n: int) -> list[int]:
    premiers = []
    for candidat in range(2, n + 1):
        for diviseur in range(2, candidat):
            if candidat % diviseur == 0:
                break
        else:  # aucun break : aucun diviseur trouvé
            premiers.append(candidat)
    return premiers


def paires_de_somme(n: int, cible: int) -> list[tuple[int, int]]:
    paires = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if a + b == cible:
                paires.append((a, b))
    return paires
