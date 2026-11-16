"""Solutions 5.2 — Paramètres."""


def prix_ttc(prix_ht: float, taux: float = 18) -> float:
    return prix_ht * (1 + taux / 100)


def remise(prix: float, pourcentage: float = 0) -> float:
    return prix - prix * pourcentage / 100


def additionner(*nombres: float) -> float:
    return sum(nombres)


def moyenne(*notes: float) -> float:
    if not notes:
        return 0.0
    return sum(notes) / len(notes)


def plus_grand(premier: float, *autres: float) -> float:
    gagnant = premier
    for n in autres:
        if n > gagnant:
            gagnant = n
    return gagnant


def fiche(**infos: object) -> str:
    return " | ".join(f"{cle}={valeur}" for cle, valeur in infos.items())


def formater_prix(montant: float, *, devise: str = "FCFA", decimales: int = 0) -> str:
    return f"{montant:,.{decimales}f} {devise}"


def ajouter_produit(produit: str, panier: list[str] | None = None) -> list[str]:
    if panier is None:
        panier = []  # nouvelle liste à chaque appel
    panier.append(produit)
    return panier
