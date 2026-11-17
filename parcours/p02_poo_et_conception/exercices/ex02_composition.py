"""Exercices 2.1 — compléter les NotImplementedError.

Tâche 1 — Stock() crée un dictionnaire propre à l'instance. quantite(nom)
retourne la quantité disponible, ou 0 pour un nom absent (comparaison exacte).
Tâche 2 — ajouter(nom, quantite) cumule une quantité entière strictement positive.
Refuser 0, nombres négatifs, fractions et booléens par ValueError, sans mutation.
Tâche 3 — produits est une propriété sans setter qui retourne une copie du
 dictionnaire des quantités. Modifier cette copie ne doit pas modifier le stock.
"""


class Stock:
    """Ex. 1 : créer le dictionnaire dans chaque instance."""

    def __init__(self):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError

    def ajouter(self, nom, quantite):
        """Ex. 2 : valider avant toute mutation."""
        raise NotImplementedError

    def quantite(self, nom):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError

    @property
    def produits(self):
        """Ex. 3 : exposer une copie, pas le dictionnaire interne."""
        raise NotImplementedError
