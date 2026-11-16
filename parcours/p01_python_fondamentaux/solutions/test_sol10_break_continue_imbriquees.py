"""Tests des solutions 3.3. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol10_break_continue_imbriquees import (
    nombres_premiers,
    paires_de_somme,
    premier_carre_superieur,
    premier_mot,
    somme_sans_multiples_de_3,
    table_carree,
)


@pytest.mark.parametrize(("limite", "attendu"), [(50, 8), (0, 1), (100, 11), (1, 2)])
def test_premier_carre_superieur(limite, attendu):
    assert premier_carre_superieur(limite) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (2, 3), (10, 37), (30, 300)])
def test_somme_sans_multiples_de_3(n, attendu):
    assert somme_sans_multiples_de_3(n) == attendu


@pytest.mark.parametrize(
    ("texte", "attendu"), [("Mbote na yo", "Mbote"), ("Congo", "Congo"), (" a", ""), ("", "")]
)
def test_premier_mot(texte, attendu):
    assert premier_mot(texte) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(1, "1"), (3, "1 2 3\n2 4 6\n3 6 9"), (2, "1 2\n2 4")])
def test_table_carree(n, attendu):
    assert table_carree(n) == attendu


def test_nombres_premiers():
    assert nombres_premiers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert nombres_premiers(1) == []
    assert nombres_premiers(2) == [2]


def test_paires_de_somme():
    assert paires_de_somme(10, 5) == [(1, 4), (2, 3)]
    assert paires_de_somme(10, 3) == [(1, 2)]
    assert paires_de_somme(3, 100) == []
