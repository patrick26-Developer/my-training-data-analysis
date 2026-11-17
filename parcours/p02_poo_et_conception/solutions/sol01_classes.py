"""Corrigés commentés : leçon 1.1."""


class Produit:
    """Ex. 1 : chaque instance conserve ses propres données."""

    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def valeur(self):
        """Ex. 2 : un calcul ne modifie pas la quantité."""
        return self.prix * self.quantite

    def etiquette(self):
        """Ex. 3 : utiliser les attributs de l'instance courante."""
        return f"{self.nom} : {self.prix} FCFA"
