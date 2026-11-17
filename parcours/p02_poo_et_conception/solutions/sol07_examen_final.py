"""Corrigé de la partie code de l'examen P02."""

from dataclasses import dataclass


class Portefeuille:
    def __init__(self, solde):
        if solde < 0:
            raise ValueError("Solde négatif.")
        self._solde = solde

    @property
    def solde(self):
        return self._solde

    def debiter(self, montant):
        # Vérifier avant de modifier : un refus préserve le solde.
        if montant <= 0 or montant > self.solde:
            raise ValueError("Débit impossible.")
        self._solde -= montant


@dataclass(frozen=True)
class LigneTicket:
    produit: str
    prix: int
    quantite: int

    def total(self):
        return self.prix * self.quantite


class Livraison:
    def frais(self, distance):
        return 0


class LivraisonMoto(Livraison):
    def frais(self, distance):
        # L'enfant conserve la signature et l'unité du résultat du parent.
        return 500 + 100 * distance


class Commande:
    def __init__(self, livraison):
        self.livraison = livraison

    def total(self, sous_total, distance):
        # La dépendance reçue peut être une autre classe sans parent commun.
        frais = self.livraison.frais(distance)
        if frais < 0:
            raise ValueError("Frais négatifs.")
        return sous_total + frais
