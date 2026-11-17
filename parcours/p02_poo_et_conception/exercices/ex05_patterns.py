"""Exercices 5.1 — compléter les NotImplementedError.

Tâche 1 — Caisse(politique) conserve l'objet reçu.
Tâche 2 — total(montant) retourne montant - politique.calculer(montant).
Lever ValueError si la remise n'est pas comprise entre 0 et montant.
Tâche 3 — RemiseFixe(montant) refuse un montant négatif par ValueError.
calculer(sous_total) retourne le plus petit de la remise fixe et du sous-total.
Les entrées sont des nombres finis positifs ou nuls, sauf tests explicites de refus.
"""


class Caisse:
    """Ex. 1 : recevoir la dépendance dans le constructeur."""

    def __init__(self, politique):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError

    def total(self, montant):
        """Ex. 2 : déléguer puis vérifier le résultat du collaborateur."""
        raise NotImplementedError


class RemiseFixe:
    """Ex. 3 : stratégie de remplacement sans héritage obligatoire."""

    def __init__(self, montant):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError

    def calculer(self, montant):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError
