"""Solutions 8.4 — Algorithmes classiques."""


def recherche_lineaire(liste: list, cible: object) -> int:
    for i, valeur in enumerate(liste):
        if valeur == cible:
            return i
    return -1


def dichotomie(liste_triee: list, cible: object) -> int:
    bas, haut = 0, len(liste_triee) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if liste_triee[milieu] == cible:
            return milieu
        if liste_triee[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1


def tri_a_bulles(liste: list) -> list:
    liste = list(liste)
    n = len(liste)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange = True
        if not echange:  # déjà trié : on s'arrête
            break
    return liste


def tri_insertion(liste: list) -> list:
    liste = list(liste)
    for i in range(1, len(liste)):
        valeur = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > valeur:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = valeur
    return liste


def crible(n: int) -> list[int]:
    if n < 2:
        return []
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False
    for i in range(2, int(n**0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, n + 1, i):
                est_premier[multiple] = False
    return [i for i, p in enumerate(est_premier) if p]


def fibonacci_liste(n: int) -> list[int]:
    termes = []
    a, b = 0, 1
    for _ in range(n):
        termes.append(a)
        a, b = b, a + b
    return termes


def est_palindrome(texte: str) -> bool:
    propre = [c.lower() for c in texte if c.isalnum()]
    return propre == propre[::-1]


def a_des_doublons(liste: list) -> bool:
    return len(set(liste)) != len(liste)


def deux_sommes(nombres: list[int], cible: int) -> tuple[int, int] | None:
    vus: dict[int, int] = {}  # valeur -> indice
    for j, valeur in enumerate(nombres):
        complement = cible - valeur
        if complement in vus:
            return vus[complement], j
        vus[valeur] = j
    return None


def rendre_monnaie(montant: int, pieces: list[int]) -> dict[int, int]:
    rendu: dict[int, int] = {}
    reste = montant
    for piece in sorted(pieces, reverse=True):
        nombre, reste = divmod(reste, piece)
        if nombre:
            rendu[piece] = nombre
    return rendu


def nombre_de_chiffres_binaires(n: int) -> str:
    if n == 0:
        return "0"
    chiffres = []
    while n > 0:
        chiffres.append(str(n % 2))
        n //= 2
    return "".join(reversed(chiffres))
