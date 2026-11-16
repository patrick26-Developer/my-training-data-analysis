"""Solutions 6.1 — Les exceptions."""


def convertir_entier(texte: str) -> int | None:
    try:
        return int(texte)
    except ValueError:
        return None


def diviser_sans_erreur(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


def valeur_ou_defaut(dico: dict, cle: object, defaut: object) -> object:
    try:
        return dico[cle]
    except KeyError:
        return defaut


def retirer(solde: float, montant: float) -> float:
    if montant <= 0:
        raise ValueError("Montant invalide")
    if montant > solde:
        raise ValueError("Solde insuffisant")
    return solde - montant


def premier_entier_valide(saisies: list[str]) -> int:
    for texte in saisies:
        try:
            return int(texte)
        except ValueError:
            continue
    raise ValueError("Aucune saisie valide")


def somme_tolerante(textes: list[str]) -> float:
    total = 0.0
    for texte in textes:
        try:
            total += float(texte)
        except ValueError:
            pass  # texte ignoré volontairement
    return total


class StockInsuffisant(Exception):
    """Levée quand on veut vendre plus que le stock disponible."""


def vendre(stock: int, quantite: int) -> int:
    if stock < quantite:
        raise StockInsuffisant(f"Stock {stock} < demande {quantite}")
    return stock - quantite
