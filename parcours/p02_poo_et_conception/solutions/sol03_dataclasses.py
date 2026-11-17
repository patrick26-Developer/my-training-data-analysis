"""Corrigés commentés : leçon 3.1."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Vente:
    """Ex. 1 : dataclass de valeurs simples, gelée."""

    produit: str
    prix: float
    quantite: int

    def total(self):
        """Ex. 2 : méthode ordinaire dans une dataclass."""
        return self.prix * self.quantite


def creer_vente(produit):
    """Ex. 3 : copier les valeurs du dictionnaire, pas sa référence."""
    return Vente(produit["nom"], produit["prix"], produit["quantite"])
