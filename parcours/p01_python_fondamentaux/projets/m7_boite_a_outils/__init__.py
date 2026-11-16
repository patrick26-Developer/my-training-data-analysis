"""Boîte à outils : maths, textes et dates (mini-projet du module 7)."""

from .dates import age_en_annees, jours_restants
from .maths import moyenne, pgcd
from .textes import est_palindrome, nettoyer_nom

__all__ = ["age_en_annees", "est_palindrome", "jours_restants", "moyenne", "nettoyer_nom", "pgcd"]
