"""Tests des solutions 1.2. Copie des tests d'exercice appliquée aux solutions."""

import pytest
from sol02_variables_et_nombres import (
    appliquer_remise,
    fcfa_en_euro,
    nom_du_type,
    partager,
    stock_final,
    total_facture,
)


def test_total_facture():
    assert total_facture(2500, 3) == 7500
    assert total_facture(100, 0) == 0


def test_appliquer_remise():
    assert appliquer_remise(20000, 15) == pytest.approx(17000.0)
    assert appliquer_remise(1000, 0) == pytest.approx(1000.0)
    assert appliquer_remise(1000, 100) == pytest.approx(0.0)


def test_fcfa_en_euro():
    assert fcfa_en_euro(65595.7) == 100.0
    assert fcfa_en_euro(1000) == 1.52


def test_partager():
    assert partager(10000, 3) == (3333, 1)
    assert partager(9000, 3) == (3000, 0)


def test_nom_du_type():
    assert nom_du_type(3) == "int"
    assert nom_du_type(3.5) == "float"
    assert nom_du_type("Manioc") == "str"
    assert nom_du_type(True) == "bool"


def test_stock_final():
    assert stock_final(100, 35, 20) == 85
    assert stock_final(10, 10, 0) == 0
