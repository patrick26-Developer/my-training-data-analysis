"""Tests des solutions 10.1. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol36_deboguer import (
    ajouter_produit,
    compter_voyelles,
    est_pair,
    est_premier,
    fusionner,
    maximum,
    moyenne,
    nombre_de_jours_du_mois,
    premier_mot,
    remise,
    somme_jusqua,
    trier_decroissant,
)


def test_bug1_somme_jusqua():
    assert somme_jusqua(10) == 55
    assert somme_jusqua(1) == 1
    assert somme_jusqua(0) == 0


def test_bug2_moyenne():
    assert moyenne([10, 20]) == pytest.approx(15.0)
    assert moyenne([]) == 0.0


@pytest.mark.parametrize(
    ("n", "attendu"), [(0, True), (1, False), (2, True), (7, False), (-4, True)]
)
def test_bug3_est_pair(n, attendu):
    assert est_pair(n) is attendu


def test_bug4_trier_decroissant():
    original = [3, 1, 2]
    assert trier_decroissant(original) == [3, 2, 1]
    assert original == [3, 1, 2]


def test_bug5_ajouter_produit():
    assert ajouter_produit("Riz") == ["Riz"]
    assert ajouter_produit("Sel") == ["Sel"]
    panier = ["Riz"]
    assert ajouter_produit("Sel", panier) == ["Riz", "Sel"]


def test_bug6_compter_voyelles():
    assert compter_voyelles("Brazzaville") == 4
    assert compter_voyelles("AEIOUY") == 6
    assert compter_voyelles("") == 0


def test_bug7_remise():
    assert remise(1000, 10) == pytest.approx(900.0)
    assert remise(200, 50) == pytest.approx(100.0)


def test_bug8_premier_mot():
    assert premier_mot("Mbote na yo") == "Mbote"
    assert premier_mot("Congo") == "Congo"
    assert premier_mot("") == ""


def test_bug9_maximum():
    assert maximum([3, 9, 2]) == 9
    assert maximum([-5, -2, -9]) == -2
    assert maximum([-1]) == -1


@pytest.mark.parametrize(
    ("n", "attendu"),
    [
        (0, False),
        (1, False),
        (2, True),
        (9, False),
        (15, False),
        (17, True),
        (25, False),
        (97, True),
    ],
)
def test_bug10_est_premier(n, attendu):
    assert est_premier(n) is attendu


def test_bug11_fusionner():
    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 30}
    assert fusionner(a, b) == {"x": 1, "y": 20, "z": 30}
    assert a == {"x": 1, "y": 2}  # l'original ne doit pas changer


@pytest.mark.parametrize(
    ("mois", "annee", "attendu"),
    [
        (1, 2026, 31),
        (4, 2026, 30),
        (2, 2026, 28),
        (2, 2024, 29),
        (2, 1900, 28),
        (2, 2000, 29),
        (12, 2026, 31),
    ],
)
def test_bug12_jours_du_mois(mois, annee, attendu):
    assert nombre_de_jours_du_mois(mois, annee) == attendu
