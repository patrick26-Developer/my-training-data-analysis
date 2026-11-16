"""Tests des solutions 4.5. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol15_comprehensions import (
    aplatir,
    carres,
    commencant_par,
    dico_longueurs,
    grille,
    longueurs,
    prix_ttc,
    sans_negatifs,
    tous_positifs,
)


@pytest.mark.parametrize(("n", "attendu"), [(4, [1, 4, 9, 16]), (0, []), (1, [1])])
def test_carres(n, attendu):
    assert carres(n) == attendu


def test_prix_ttc():
    assert prix_ttc([300, 750, 1200], 500) == [885, 1416]
    assert prix_ttc([100], 500) == []


def test_longueurs():
    assert longueurs(["riz", "sucre"]) == [3, 5]
    assert longueurs([]) == []


def test_commencant_par():
    assert commencant_par(["Riz", "rat", "Sel"], "r") == ["Riz", "rat"]
    assert commencant_par(["Riz"], "x") == []


def test_dico_longueurs():
    assert dico_longueurs(["riz", "sucre"]) == {"riz": 3, "sucre": 5}


def test_sans_negatifs():
    assert sans_negatifs([3, -1, 4, -5]) == [3, 0, 4, 0]
    assert sans_negatifs([]) == []


def test_aplatir():
    assert aplatir([[1, 2], [3], []]) == [1, 2, 3]
    assert aplatir([]) == []


def test_tous_positifs():
    assert tous_positifs([1, 2, 3]) is True
    assert tous_positifs([1, 0, 3]) is False
    assert tous_positifs([]) is True


def test_grille():
    g = grille(2, 3)
    assert g == [[0, 0, 0], [0, 0, 0]]
    g[0][0] = 9
    assert g[1][0] == 0  # les lignes sont indépendantes
