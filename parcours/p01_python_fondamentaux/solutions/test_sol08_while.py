"""Tests des solutions 3.1. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol08_while import (
    annees_pour_atteindre,
    collatz,
    factorielle,
    nombre_de_bits,
    somme_des_chiffres,
    somme_jusqua,
    total_jusqua_fin,
)


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (1, 1), (10, 55), (100, 5050)])
def test_somme_jusqua(n, attendu):
    assert somme_jusqua(n) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorielle(n, attendu):
    assert factorielle(n) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (1, 1), (8, 4), (255, 8), (256, 9)])
def test_nombre_de_bits(n, attendu):
    assert nombre_de_bits(n) == attendu


@pytest.mark.parametrize(
    ("capital", "objectif", "taux", "attendu"),
    [(1000, 2000, 10, 8), (1000, 1000, 5, 0), (500, 1000, 100, 1)],
)
def test_annees_pour_atteindre(capital, objectif, taux, attendu):
    assert annees_pour_atteindre(capital, objectif, taux) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(1, 0), (2, 1), (6, 8), (27, 111)])
def test_collatz(n, attendu):
    assert collatz(n) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (7, 7), (1234, 10), (999, 27)])
def test_somme_des_chiffres(n, attendu):
    assert somme_des_chiffres(n) == attendu


def test_total_jusqua_fin():
    assert total_jusqua_fin(["500", "250.5", "fin", "999"]) == pytest.approx(750.5)
    assert total_jusqua_fin(["fin"]) == 0
