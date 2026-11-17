"""Solutions 10.4 — Documenter son code (Mayele Python Académie)."""


def carre(x: float) -> float:
    """Retourne le carré de x.

    >>> carre(4)
    16
    >>> carre(-3)
    9
    """
    return x * x


def est_pair(n: int) -> bool:
    """Retourne True si n est pair.

    >>> est_pair(4)
    True
    >>> est_pair(7)
    False
    """
    return n % 2 == 0


def initiales(nom_complet: str) -> str:
    """Retourne les initiales d'un nom complet, chacune suivie d'un point.

    >>> initiales("Grâce Marie Nzoni")
    'G.M.N.'
    >>> initiales("jean")
    'J.'
    """
    return "".join(mot[0].upper() + "." for mot in nom_complet.split())


def prix_ttc(prix_ht: float, taux: float = 18) -> float:
    """Retourne le prix TTC arrondi à 2 décimales.

    Args:
        prix_ht: prix hors taxe en FCFA.
        taux: taux de TVA en pourcentage (18 par défaut).

    Returns:
        Le prix toutes taxes comprises.

    >>> prix_ttc(1000)
    1180.0
    >>> prix_ttc(333, 5)
    349.65
    """
    return round(prix_ht * (1 + taux / 100), 2)


def fusionner_mots(mots: list[str]) -> str:
    """Colle les mots avec un tiret.

    >>> fusionner_mots(["a", "b", "c"])
    'a-b-c'
    >>> fusionner_mots([])
    ''
    """
    return "-".join(mots)
