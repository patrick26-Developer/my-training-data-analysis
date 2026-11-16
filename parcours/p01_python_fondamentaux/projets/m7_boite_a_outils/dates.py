"""Fonctions de dates réutilisables."""

from datetime import date


def age_en_annees(naissance: date, aujourdhui: date | None = None) -> int:
    """Âge en années complètes."""
    aujourdhui = aujourdhui or date.today()
    annees = aujourdhui.year - naissance.year
    if (aujourdhui.month, aujourdhui.day) < (naissance.month, naissance.day):
        annees -= 1
    return annees


def jours_restants(cible: date, aujourdhui: date | None = None) -> int:
    """Nombre de jours avant la date cible (négatif si elle est passée)."""
    aujourdhui = aujourdhui or date.today()
    return (cible - aujourdhui).days
