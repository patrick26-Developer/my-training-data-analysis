"""Solutions 4.1 — Les listes."""


def moyenne(nombres: list[float]) -> float:
    if not nombres:
        return 0.0
    return sum(nombres) / len(nombres)


def extremes(nombres: list[float]) -> tuple[float, float]:
    plus_petit = nombres[0]
    plus_grand = nombres[0]
    for n in nombres:
        if n < plus_petit:
            plus_petit = n
        if n > plus_grand:
            plus_grand = n
    return plus_petit, plus_grand


def trier_decroissant(nombres: list[float]) -> list[float]:
    return sorted(nombres, reverse=True)  # sorted ne modifie pas l'originale


def sans_doublons(elements: list) -> list:
    resultat = []
    for e in elements:
        if e not in resultat:
            resultat.append(e)
    return resultat


def fin_inversee(elements: list, debut: int) -> list:
    return elements[debut:][::-1]


def ajouter_si_absent(stock: list[str], produit: str) -> bool:
    if produit in stock:
        return False
    stock.append(produit)
    return True


def somme_des_lignes(matrice: list[list[float]]) -> list[float]:
    sommes = []
    for ligne in matrice:
        sommes.append(sum(ligne))
    return sommes


def transposee(matrice: list[list[float]]) -> list[list[float]]:
    resultat = []
    for colonne in range(len(matrice[0])):
        nouvelle_ligne = []
        for ligne in matrice:
            nouvelle_ligne.append(ligne[colonne])
        resultat.append(nouvelle_ligne)
    return resultat
