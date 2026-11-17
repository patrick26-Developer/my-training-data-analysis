"""Corrigés commentés : leçon 5.1."""


class Caisse:
    """Ex. 1 : recevoir la dépendance dans le constructeur."""

    def __init__(self, politique):
        self.politique = politique

    def total(self, montant):
        """Ex. 2 : déléguer puis vérifier le résultat du collaborateur."""
        remise = self.politique.calculer(montant)
        if not 0 <= remise <= montant:
            raise ValueError("Remise invalide.")
        return montant - remise


class RemiseFixe:
    """Ex. 3 : stratégie de remplacement sans héritage obligatoire."""

    def __init__(self, montant):
        if montant < 0:
            raise ValueError("Remise négative.")
        self.montant = montant

    def calculer(self, montant):
        return min(self.montant, montant)
