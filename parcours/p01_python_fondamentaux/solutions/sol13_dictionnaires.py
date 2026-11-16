"""Solutions 4.3 — Les dictionnaires."""


def prix_du_produit(catalogue: dict[str, float], produit: str) -> float:
    return catalogue.get(produit, 0)


def compter_lettres(texte: str) -> dict[str, int]:
    compteur: dict[str, int] = {}
    for lettre in texte:
        compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur


def valeur_du_stock(stock: dict[str, tuple[float, int]]) -> float:
    total = 0
    for prix, quantite in stock.values():
        total += prix * quantite
    return total


def plus_cher(catalogue: dict[str, float]) -> str | None:
    gagnant = None
    meilleur_prix = None
    for produit, prix in catalogue.items():
        if meilleur_prix is None or prix > meilleur_prix:
            gagnant = produit
            meilleur_prix = prix
    return gagnant


def total_par_jour(ventes: list[tuple[str, float]]) -> dict[str, float]:
    totaux: dict[str, float] = {}
    for jour, montant in ventes:
        totaux[jour] = totaux.get(jour, 0) + montant
    return totaux


def inverser(dico: dict) -> dict:
    resultat = {}
    for cle, valeur in dico.items():
        resultat[valeur] = cle
    return resultat


def admis(eleves: list[dict]) -> list[str]:
    noms = []
    for eleve in eleves:
        if eleve["note"] >= 10:
            noms.append(eleve["nom"])
    return noms


def fusionner_stocks(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    resultat = dict(a)  # copie : on ne modifie pas l'original
    for produit, quantite in b.items():
        resultat[produit] = resultat.get(produit, 0) + quantite
    return resultat
