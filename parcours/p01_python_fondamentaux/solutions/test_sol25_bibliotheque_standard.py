"""Tests des solutions 7.2. Généré par outils/sync_tests_solutions.py."""

import string
from datetime import date

import pytest
from sol25_bibliotheque_standard import (
    age,
    ajouter_jours,
    formater_date_fr,
    jours_avant,
    mot_de_passe,
    regrouper_par_initiale,
    resume_statistique,
    toutes_les_paires,
)


@pytest.mark.parametrize(
    ("naissance", "aujourdhui", "attendu"),
    [
        (date(2000, 5, 20), date(2026, 5, 19), 25),
        (date(2000, 5, 20), date(2026, 5, 20), 26),
        (date(2000, 5, 20), date(2026, 12, 31), 26),
        (date(2000, 2, 29), date(2001, 2, 28), 0),
    ],
)
def test_age(naissance, aujourdhui, attendu):
    assert age(naissance, aujourdhui) == attendu


def test_jours_avant():
    assert jours_avant(date(2026, 12, 25), date(2026, 12, 20)) == 5
    assert jours_avant(date(2026, 1, 1), date(2026, 1, 3)) == -2
    assert jours_avant(date(2026, 1, 1), date(2026, 1, 1)) == 0


def test_formater_date_fr():
    assert formater_date_fr("2026-12-25") == "25/12/2026"
    assert formater_date_fr("2026-01-05") == "05/01/2026"


def test_ajouter_jours():
    assert ajouter_jours("2026-12-30", 5) == "2027-01-04"
    assert ajouter_jours("2024-02-28", 1) == "2024-02-29"


def test_resume_statistique():
    assert resume_statistique([12, 15, 9, 18, 15]) == {
        "moyenne": 13.8,
        "mediane": 15,
        "min": 9,
        "max": 18,
    }


def test_regrouper_par_initiale():
    resultat = regrouper_par_initiale(["Riz", "rat", "Sel", "sucre", "Huile"])
    assert resultat == {"r": ["Riz", "rat"], "s": ["Sel", "sucre"], "h": ["Huile"]}


def test_toutes_les_paires():
    assert toutes_les_paires(["A", "B", "C"]) == [("A", "B"), ("A", "C"), ("B", "C")]
    assert toutes_les_paires(["A"]) == []


def test_mot_de_passe():
    mdp = mot_de_passe(16)
    assert len(mdp) == 16
    autorises = set(string.ascii_letters + string.digits)
    assert set(mdp) <= autorises
    assert mot_de_passe(16) != mot_de_passe(16)  # (probabilité d'égalité négligeable)
