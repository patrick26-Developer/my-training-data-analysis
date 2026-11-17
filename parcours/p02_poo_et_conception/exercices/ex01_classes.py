"""Exercices 1.1 — compléter les NotImplementedError.

Tâche 1 — Produit(nom, prix, quantite) mémorise ces trois attributs, sans
validation demandée ici. Chaque instance conserve ses propres valeurs.
Tâche 2 — valeur() retourne prix * quantite, sans modifier l'objet.
Tâche 3 — etiquette() retourne exactement "<nom> : <prix> FCFA".
Exemple : Produit("Riz", 800, 3).etiquette() == "Riz : 800 FCFA".
"""


class Produit:
    """Ex. 1 : chaque instance conserve ses propres données."""

    def __init__(self, nom, prix, quantite):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError

    def valeur(self):
        """Ex. 2 : un calcul ne modifie pas la quantité."""
        raise NotImplementedError

    def etiquette(self):
        """Ex. 3 : utiliser les attributs de l'instance courante."""
        raise NotImplementedError
