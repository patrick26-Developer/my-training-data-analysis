"""Solutions 7.2 — La bibliothèque standard."""

import secrets
import statistics
import string
from collections import defaultdict
from datetime import date, datetime, timedelta
from itertools import combinations


def age(naissance: date, aujourdhui: date) -> int:
    annees = aujourdhui.year - naissance.year
    # Si l'anniversaire n'est pas encore passé cette année, on retire un an.
    if (aujourdhui.month, aujourdhui.day) < (naissance.month, naissance.day):
        annees -= 1
    return annees


def jours_avant(date_cible: date, aujourdhui: date) -> int:
    return (date_cible - aujourdhui).days


def formater_date_fr(texte_iso: str) -> str:
    return datetime.strptime(texte_iso, "%Y-%m-%d").strftime("%d/%m/%Y")


def ajouter_jours(texte_iso: str, n: int) -> str:
    depart = datetime.strptime(texte_iso, "%Y-%m-%d").date()
    return (depart + timedelta(days=n)).isoformat()


def resume_statistique(notes: list[float]) -> dict[str, float]:
    return {
        "moyenne": round(statistics.mean(notes), 2),
        "mediane": statistics.median(notes),
        "min": min(notes),
        "max": max(notes),
    }


def regrouper_par_initiale(mots: list[str]) -> dict[str, list[str]]:
    groupes: defaultdict[str, list[str]] = defaultdict(list)
    for mot in mots:
        groupes[mot[0].lower()].append(mot)
    return dict(groupes)


def toutes_les_paires(elements: list) -> list[tuple]:
    return list(combinations(elements, 2))


def mot_de_passe(longueur: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(longueur))
