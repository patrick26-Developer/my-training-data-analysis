"""Corrigés commentés : leçon 2.1."""


class Stock:
    """Ex. 1 : créer le dictionnaire dans chaque instance."""

    def __init__(self):
        self._quantites = {}

    def ajouter(self, nom, quantite):
        """Ex. 2 : valider avant toute mutation."""
        if type(quantite) is not int or quantite <= 0:
            raise ValueError("Quantité entière positive requise.")
        self._quantites[nom] = self.quantite(nom) + quantite

    def quantite(self, nom):
        return self._quantites.get(nom, 0)

    @property
    def produits(self):
        """Ex. 3 : exposer une copie, pas le dictionnaire interne."""
        return self._quantites.copy()
