"""Solutions 1.3 — Le texte."""


def nettoyer_nom(nom: str) -> str:
    # strip() enlève les espaces des bords, title() met une majuscule à chaque mot.
    return nom.strip().title()


def presenter(nom: str, age: int) -> str:
    return f"{nom} a {age} ans"


def formater_prix(montant: float) -> str:
    # ',' = séparateur de milliers ; '.2f' = deux décimales.
    return f"{montant:,.2f} FCFA"


def code_ville(ville: str) -> str:
    return ville[:3].upper()


def inverser(texte: str) -> str:
    return texte[::-1]


def valeur_du_stock(ligne: str) -> int:
    _produit, prix, quantite = ligne.split(";")
    return int(prix) * int(quantite)


def telephone_valide(texte: str) -> bool:
    return len(texte) == 9 and texte.isdigit()
