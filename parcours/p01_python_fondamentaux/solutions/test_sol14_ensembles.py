"""Tests des solutions 4.4. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol14_ensembles import (
    anagrammes,
    communs,
    doublons,
    est_pangramme,
    mot_valide,
    nb_differents,
    seulement_chez_a,
)


@pytest.mark.parametrize(("elements", "attendu"), [([1, 2, 2, 3, 1], 3), ([], 0), (["a", "A"], 2)])
def test_nb_differents(elements, attendu):
    assert nb_differents(elements) == attendu


def test_communs():
    assert communs(["Riz", "Sel"], ["Sel", "Huile", "Riz"]) == ["Riz", "Sel"]
    assert communs(["a"], ["b"]) == []


def test_seulement_chez_a():
    assert seulement_chez_a(["Riz", "Sel", "Sucre"], ["Sel"]) == ["Riz", "Sucre"]
    assert seulement_chez_a([], ["a"]) == []


@pytest.mark.parametrize(
    ("mot", "lettres", "attendu"),
    [("riz", "zirabc", True), ("rat", "riz", False), ("", "abc", True)],
)
def test_mot_valide(mot, lettres, attendu):
    assert mot_valide(mot, lettres) is attendu


def test_est_pangramme():
    assert est_pangramme("The quick brown fox jumps over the lazy dog") is True
    assert est_pangramme("Mbote na bino") is False


@pytest.mark.parametrize(
    ("elements", "attendu"), [([1, 2, 2, 3, 3, 3, 4], [2, 3]), ([1, 2], []), ([], [])]
)
def test_doublons(elements, attendu):
    assert doublons(elements) == attendu


@pytest.mark.parametrize(
    ("a", "b", "attendu"),
    [("Marie", "aimer", True), ("Roma", "Amor", True), ("abc", "abd", False), ("aab", "ab", False)],
)
def test_anagrammes(a, b, attendu):
    assert anagrammes(a, b) is attendu
