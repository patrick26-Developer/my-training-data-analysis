"""Solutions 2.1 — Booléens et comparaisons."""


def est_majeur(age: int) -> bool:
    return age >= 18


def est_admis(note: float) -> bool:
    return 10 <= note <= 20


def est_weekend(jour: str) -> bool:
    return jour in ("samedi", "dimanche")


def doit_retirer(stock: int, perime: bool) -> bool:
    return stock == 0 or perime


def peut_emprunter(abonnement_actif: bool, livres_empruntes: int) -> bool:
    return abonnement_actif and livres_empruntes < 3


def est_vide(texte: str) -> bool:
    # strip() enlève les espaces ; un texte vide est « faux ».
    return not texte.strip()


def est_voyelle(lettre: str) -> bool:
    return lettre.lower() in "aeiouy"
