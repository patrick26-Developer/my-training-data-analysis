"""Solutions 10.1 — Déboguer : les 12 bugs, expliqués."""


def somme_jusqua(n: int) -> int:
    """Bug : range(1, n) s'arrête à n - 1. Correction : range(1, n + 1)."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def moyenne(notes: list[float]) -> float:
    """Bug : division par zéro sur une liste vide. Correction : cas particulier."""
    if not notes:
        return 0.0
    return sum(notes) / len(notes)


def est_pair(n: int) -> bool:
    """Bug : la condition était inversée (n % 2 == 1 teste l'impair)."""
    return n % 2 == 0


def trier_decroissant(nombres: list[float]) -> list[float]:
    """Bug : `resultat = nombres` n'est pas une copie. Correction : sorted()."""
    return sorted(nombres, reverse=True)


def ajouter_produit(produit: str, panier: list[str] | None = None) -> list[str]:
    """Bug : argument par défaut modifiable partagé. Correction : None."""
    if panier is None:
        panier = []
    panier.append(produit)
    return panier


def compter_voyelles(texte: str) -> int:
    """Bug : les majuscules n'étaient pas comptées. Correction : texte.lower()."""
    compteur = 0
    for lettre in texte.lower():
        if lettre in "aeiouy":
            compteur += 1
    return compteur


def remise(prix: float, pourcentage: float) -> float:
    """Bug : on soustrayait le pourcentage lui-même. Correction : prix * pourcentage / 100."""
    return prix - prix * pourcentage / 100


def premier_mot(phrase: str) -> str:
    """Bug : mots[1] au lieu de mots[0] (et plante pour un seul mot). Correction : mots[0]."""
    mots = phrase.split(" ")
    return mots[0]


def maximum(nombres: list[float]) -> float:
    """Bug : initialiser à 0 échoue pour des nombres négatifs. Correction : nombres[0]."""
    plus_grand = nombres[0]
    for n in nombres:
        if n > plus_grand:
            plus_grand = n
    return plus_grand


def est_premier(n: int) -> bool:
    """Bug : le `else: return True` arrête la boucle au premier diviseur testé."""
    if n < 2:
        return False
    for diviseur in range(2, n):
        if n % diviseur == 0:
            return False
    return True  # le return True est APRÈS la boucle


def fusionner(a: dict, b: dict) -> dict:
    """Bug : `resultat = a` modifie l'original. Correction : copie avec dict(a)."""
    resultat = dict(a)
    for cle, valeur in b.items():
        resultat[cle] = valeur
    return resultat


def nombre_de_jours_du_mois(mois: int, annee: int) -> int:
    """Bug : règle des années bissextiles incomplète (1900 n'est pas bissextile, 2000 l'est)."""
    if mois == 2:
        bissextile = annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)
        return 29 if bissextile else 28
    if mois in (4, 6, 9, 11):
        return 30
    return 31
