"""Tests des solutions 4.1. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol11_listes import (
    ajouter_si_absent,
    extremes,
    fin_inversee,
    moyenne,
    sans_doublons,
    somme_des_lignes,
    transposee,
    trier_decroissant,
)


def test_moyenne():
    assert moyenne([10, 15, 20]) == pytest.approx(15.0)
    assert moyenne([]) == 0.0
    assert moyenne([7]) == pytest.approx(7.0)


@pytest.mark.parametrize(
    ("nombres", "attendu"), [([4, 9, 2, 7], (2, 9)), ([5], (5, 5)), ([-3, -8, 0], (-8, 0))]
)
def test_extremes(nombres, attendu):
    assert extremes(nombres) == attendu


def test_trier_decroissant():
    original = [3, 1, 2]
    assert trier_decroissant(original) == [3, 2, 1]
    assert original == [3, 1, 2]  # l'originale n'est pas modifiée


def test_sans_doublons():
    assert sans_doublons([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert sans_doublons([]) == []
    assert sans_doublons(["a", "a"]) == ["a"]


def test_fin_inversee():
    assert fin_inversee([1, 2, 3, 4, 5], 2) == [5, 4, 3]
    assert fin_inversee([1, 2, 3], 0) == [3, 2, 1]
    assert fin_inversee([1, 2, 3], 3) == []


def test_ajouter_si_absent():
    stock = ["Manioc"]
    assert ajouter_si_absent(stock, "Riz") is True
    assert stock == ["Manioc", "Riz"]
    assert ajouter_si_absent(stock, "Riz") is False
    assert stock == ["Manioc", "Riz"]


def test_somme_des_lignes():
    assert somme_des_lignes([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert somme_des_lignes([]) == []


def test_transposee():
    assert transposee([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transposee([[1, 2]]) == [[1], [2]]
