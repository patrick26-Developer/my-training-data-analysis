"""Examen P02 : contrats et barème dans ../examen_final.md.

Compléter les méthodes sans consulter solutions/.
"""

from dataclasses import dataclass


class Portefeuille:
    def __init__(self, solde):
        raise NotImplementedError

    @property
    def solde(self):
        raise NotImplementedError

    def debiter(self, montant):
        raise NotImplementedError


class LigneTicket:
    produit: str
    prix: int
    quantite: int

    def total(self):
        raise NotImplementedError


class Livraison:
    def frais(self, distance):
        raise NotImplementedError


class LivraisonMoto:
    def frais(self, distance):
        raise NotImplementedError


class Commande:
    def __init__(self, livraison):
        raise NotImplementedError

    def total(self, sous_total, distance):
        raise NotImplementedError
