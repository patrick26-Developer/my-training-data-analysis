"""Tests des solutions 8.4. Généré par outils/sync_tests_solutions.py."""

import random

import pytest
from sol31_algorithmes_classiques import (
    a_des_doublons,
    crible,
    deux_sommes,
    dichotomie,
    est_palindrome,
    fibonacci_liste,
    nombre_de_chiffres_binaires,
    recherche_lineaire,
    rendre_monnaie,
    tri_a_bulles,
    tri_insertion,
)


def test_recherche_lineaire():
    assert recherche_lineaire([4, 8, 15, 8], 8) == 1
    assert recherche_lineaire([4, 8], 99) == -1
    assert recherche_lineaire([], 1) == -1


@pytest.mark.parametrize("cible", [1, 3, 5, 7, 9, 11])
def test_dichotomie_trouve(cible):
    liste = [1, 3, 5, 7, 9, 11]
    assert liste[dichotomie(liste, cible)] == cible


def test_dichotomie_absent():
    assert dichotomie([1, 3, 5], 4) == -1
    assert dichotomie([], 4) == -1
    assert dichotomie([2], 2) == 0


def test_dichotomie_grande_liste():
    liste = list(range(0, 2_000_000, 2))
    assert dichotomie(liste, 1_999_998) == 999_999
    assert dichotomie(liste, 3) == -1


@pytest.mark.parametrize("tri", [tri_a_bulles, tri_insertion])
def test_tris(tri):
    original = [5, 2, 9, 1, 5, 6]
    assert tri(original) == [1, 2, 5, 5, 6, 9]
    assert original == [5, 2, 9, 1, 5, 6]
    assert tri([]) == []
    assert tri([1]) == [1]
    hasard = random.Random(1).sample(range(1000), 100)
    assert tri(hasard) == sorted(hasard)


def test_crible():
    assert crible(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert crible(1) == []
    assert crible(2) == [2]
    assert len(crible(10_000)) == 1229


def test_fibonacci_liste():
    assert fibonacci_liste(6) == [0, 1, 1, 2, 3, 5]
    assert fibonacci_liste(1) == [0]
    assert fibonacci_liste(0) == []


def test_est_palindrome():
    assert est_palindrome("Esope reste ici et se repose") is True
    assert est_palindrome("Bonjour") is False
    assert est_palindrome("") is True


def test_a_des_doublons():
    assert a_des_doublons([1, 2, 3, 1]) is True
    assert a_des_doublons([1, 2, 3]) is False
    assert a_des_doublons([]) is False


def test_deux_sommes():
    assert deux_sommes([2, 7, 11, 15], 9) == (0, 1)
    assert deux_sommes([3, 2, 4], 6) == (1, 2)
    assert deux_sommes([1, 2], 10) is None


def test_rendre_monnaie():
    assert rendre_monnaie(675, [500, 100, 50, 25]) == {500: 1, 100: 1, 50: 1, 25: 1}
    assert rendre_monnaie(1000, [500, 100]) == {500: 2}
    assert rendre_monnaie(0, [500]) == {}


@pytest.mark.parametrize(
    ("n", "attendu"), [(0, "0"), (1, "1"), (2, "10"), (10, "1010"), (255, "11111111")]
)
def test_binaire(n, attendu):
    assert nombre_de_chiffres_binaires(n) == attendu
