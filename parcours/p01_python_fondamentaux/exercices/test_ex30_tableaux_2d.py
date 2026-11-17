"""Tests de l'exercice 8.3. Ne modifie pas ce fichier."""

from ex30_tableaux_2d import (
    colonne,
    creer_grille,
    determinant_2x2,
    determinant_3x3,
    diagonale_principale,
    gagnant_morpion,
    identite,
    produit_matrices,
    somme_matrices,
    totaux_colonnes,
    totaux_lignes,
    tourner_90,
    trace,
    transposer,
)

M = [[120, 150, 130], [80, 95, 110], [200, 180, 210]]


def test_creer_grille():
    g = creer_grille(2, 3)
    assert g == [[0, 0, 0], [0, 0, 0]]
    g[0][0] = 9
    assert g[1][0] == 0  # lignes indépendantes
    assert creer_grille(1, 2, valeur="x") == [["x", "x"]]


def test_colonne():
    assert colonne(M, 1) == [150, 95, 180]


def test_totaux():
    assert totaux_lignes(M) == [400, 285, 590]
    assert totaux_colonnes(M) == [400, 425, 450]


def test_transposer():
    assert transposer([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transposer([[1, 2]]) == [[1], [2]]


def test_somme_matrices():
    assert somme_matrices([[1, 2], [3, 4]], [[10, 20], [30, 40]]) == [[11, 22], [33, 44]]


def test_produit_matrices():
    assert produit_matrices([[1, 2], [3, 4]], [[0, 1], [1, 0]]) == [[2, 1], [4, 3]]
    assert produit_matrices([[1, 2, 3]], [[1], [2], [3]]) == [[14]]
    a = [[2, 3], [4, 5]]
    assert produit_matrices(a, identite(2)) == a


def test_identite():
    assert identite(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_determinants():
    assert determinant_2x2([[1, 2], [3, 4]]) == -2
    assert determinant_3x3([[2, 0, 0], [0, 3, 0], [0, 0, 4]]) == 24
    assert determinant_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0


def test_diagonale_et_trace():
    assert diagonale_principale([[1, 2], [3, 4]]) == [1, 4]
    assert trace([[1, 2], [3, 4]]) == 5


def test_tourner_90():
    assert tourner_90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert tourner_90([[1, 2, 3]]) == [[1], [2], [3]]


def test_gagnant_morpion():
    assert gagnant_morpion([["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]) == "X"
    assert gagnant_morpion([["O", "X", " "], ["O", "X", " "], ["O", " ", "X"]]) == "O"
    assert gagnant_morpion([["X", "O", " "], ["O", "X", " "], [" ", " ", "X"]]) == "X"
    assert gagnant_morpion([[" "] * 3 for _ in range(3)]) is None
    assert gagnant_morpion([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]) is None
