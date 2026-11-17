"""Exercices 3.1 — compléter les NotImplementedError.

Tâche 1 — Vente est une dataclass gelée à trois champs : produit (str), prix
(float), quantite (int). Même classe et mêmes champs donnent des objets égaux.
Tâche 2 — total() retourne prix * quantite. Exemple : Vente("Riz", 800, 3) -> 2400.
Tâche 3 — creer_vente(produit) reçoit un dictionnaire avec nom, prix et quantite.
Retourner une Vente qui copie ses valeurs. Une modification ultérieure du
dictionnaire ne doit pas modifier la vente. Pas de validation des valeurs exigée ici.
"""

from dataclasses import dataclass


class Vente:
    """Ex. 1 : dataclass de valeurs simples, gelée."""

    produit: str
    prix: float
    quantite: int

    def total(self):
        """Ex. 2 : méthode ordinaire dans une dataclass."""
        raise NotImplementedError


def creer_vente(produit):
    """Ex. 3 : copier les valeurs du dictionnaire, pas sa référence."""
    raise NotImplementedError
