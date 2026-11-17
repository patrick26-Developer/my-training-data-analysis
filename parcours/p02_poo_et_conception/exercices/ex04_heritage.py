"""Exercices 4.1 — compléter les NotImplementedError.

Tâche 1 — SansRemise.calculer(montant) retourne 0.0.
Tâche 2 — RemiseSeuil hérite de SansRemise. calculer retourne 5 % du montant
strictement au-dessus de 10000, sinon 0.0. Exemple : 20000 -> 1000 ; 10000 -> 0.
Tâche 3 — total_net(montant, politique) soustrait politique.calculer(montant).
Ne pas tester la classe de politique. Les montants sont positifs ou nuls et les
politiques respectent leur contrat dans cet exercice.
"""


class SansRemise:
    """Ex. 1 : contrat commun pour le montant de remise."""

    def calculer(self, montant):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError


class RemiseSeuil(SansRemise):
    """Ex. 2 : spécialisation qui conserve signature et contrat."""

    def calculer(self, montant):
        """Complète cette opération selon la leçon et les tests."""
        raise NotImplementedError


def total_net(montant, politique):
    """Ex. 3 : aucun test du type concret n'est nécessaire."""
    raise NotImplementedError
