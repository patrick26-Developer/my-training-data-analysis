"""Tests de l'exercice 5.1. Ne modifie pas ce fichier."""

import pytest
from ex16_definir_et_appeler import (
    aire_rectangle,
    celsius_en_fahrenheit,
    est_pair,
    moyenne_ponderee,
    prix_ttc,
    salutation,
    stats,
    total_panier,
)


def test_aire_rectangle():
    assert aire_rectangle(4, 5) == 20
    assert aire_rectangle(2.5, 2) == pytest.approx(5.0)


def test_prix_ttc():
    assert prix_ttc(1000, 18) == pytest.approx(1180.0)
    assert prix_ttc(500, 0) == pytest.approx(500.0)


@pytest.mark.parametrize(("c", "f"), [(0, 32), (100, 212), (-40, -40), (37, 98.6)])
def test_celsius_en_fahrenheit(c, f):
    assert celsius_en_fahrenheit(c) == pytest.approx(f)


@pytest.mark.parametrize(("n", "attendu"), [(0, True), (3, False), (10, True), (-4, True)])
def test_est_pair(n, attendu):
    assert est_pair(n) is attendu


def test_stats():
    assert stats([4, 9, 2]) == (2, 9, 5.0)
    assert stats([7]) == (7, 7, 7.0)


@pytest.mark.parametrize(
    ("nom", "heure", "attendu"),
    [
        ("Grâce", 9, "Bonjour, Grâce !"),
        ("Jean", 17, "Bonjour, Jean !"),
        ("Jean", 18, "Bonsoir, Jean !"),
    ],
)
def test_salutation(nom, heure, attendu):
    assert salutation(nom, heure) == attendu


def test_total_panier():
    assert total_panier([1000, 500], 18) == 1770
    assert total_panier([], 18) == 0


def test_moyenne_ponderee():
    assert moyenne_ponderee([12, 15], [2, 3]) == pytest.approx(13.8)
    assert moyenne_ponderee([10], [1]) == pytest.approx(10.0)
    assert moyenne_ponderee.__doc__  # une docstring est attendue
