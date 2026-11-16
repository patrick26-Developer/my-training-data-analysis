"""Solutions 4.5 — Les compréhensions."""


def carres(n: int) -> list[int]:
    return [i * i for i in range(1, n + 1)]


def prix_ttc(prix: list[float], seuil: float) -> list[int]:
    return [round(p * 1.18) for p in prix if p > seuil]


def longueurs(mots: list[str]) -> list[int]:
    return [len(m) for m in mots]


def commencant_par(mots: list[str], lettre: str) -> list[str]:
    return [m for m in mots if m.lower().startswith(lettre.lower())]


def dico_longueurs(mots: list[str]) -> dict[str, int]:
    return {m: len(m) for m in mots}


def sans_negatifs(nombres: list[float]) -> list[float]:
    return [n if n >= 0 else 0 for n in nombres]


def aplatir(listes: list[list]) -> list:
    return [x for sous_liste in listes for x in sous_liste]


def tous_positifs(nombres: list[float]) -> bool:
    return all(n > 0 for n in nombres)


def grille(n: int, m: int) -> list[list[int]]:
    return [[0] * m for _ in range(n)]
