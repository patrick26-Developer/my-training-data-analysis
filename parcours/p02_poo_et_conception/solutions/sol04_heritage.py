"""Corrigés commentés : leçon 4.1."""


class SansRemise:
    """Ex. 1 : contrat commun pour le montant de remise."""

    def calculer(self, montant):
        return 0.0


class RemiseSeuil(SansRemise):
    """Ex. 2 : spécialisation qui conserve signature et contrat."""

    def calculer(self, montant):
        if montant > 10000:
            return montant * 5 / 100
        return 0.0


def total_net(montant, politique):
    """Ex. 3 : aucun test du type concret n'est nécessaire."""
    return montant - politique.calculer(montant)
