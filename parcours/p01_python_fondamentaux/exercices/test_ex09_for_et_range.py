"""Tests de l'exercice 3.2. Ne modifie pas ce fichier."""

import pytest
from ex09_for_et_range import (
    compte_a_rebours,
    compter_voyelles,
    est_premier,
    somme_des_carres,
    somme_des_pairs,
    table_de_multiplication,
    triangle,
)


def test_table_de_multiplication():
    lignes = table_de_multiplication(7).split("\n")
    assert len(lignes) == 10
    assert lignes[0] == "7 x 1 = 7"
    assert lignes[2] == "7 x 3 = 21"
    assert lignes[9] == "7 x 10 = 70"


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (1, 1), (3, 14), (10, 385)])
def test_somme_des_carres(n, attendu):
    assert somme_des_carres(n) == attendu


@pytest.mark.parametrize(
    ("texte", "attendu"), [("Brazzaville", 4), ("", 0), ("RHYTHM", 1), ("AEIOUY", 6)]
)
def test_compter_voyelles(texte, attendu):
    assert compter_voyelles(texte) == attendu


@pytest.mark.parametrize(
    ("n", "attendu"), [(3, "3 2 1 Décollage !"), (1, "1 Décollage !"), (0, "Décollage !")]
)
def test_compte_a_rebours(n, attendu):
    assert compte_a_rebours(n) == attendu


@pytest.mark.parametrize(("n", "attendu"), [(1, 0), (2, 2), (10, 30), (100, 2550)])
def test_somme_des_pairs(n, attendu):
    assert somme_des_pairs(n) == attendu


@pytest.mark.parametrize(("hauteur", "attendu"), [(1, "*"), (3, "*\n**\n***"), (0, "")])
def test_triangle(hauteur, attendu):
    assert triangle(hauteur) == attendu


@pytest.mark.parametrize(
    ("n", "attendu"),
    [(0, False), (1, False), (2, True), (3, True), (4, False), (13, True), (91, False), (97, True)],
)
def test_est_premier(n, attendu):
    assert est_premier(n) is attendu
