"""Tests des solutions 1.3. Généré par outils/sync_tests_solutions.py."""

from sol03_le_texte import (
    code_ville,
    formater_prix,
    inverser,
    nettoyer_nom,
    presenter,
    telephone_valide,
    valeur_du_stock,
)


def test_nettoyer_nom():
    assert nettoyer_nom("  mAmA nzoni ") == "Mama Nzoni"
    assert nettoyer_nom("JEAN") == "Jean"


def test_presenter():
    assert presenter("Grâce", 25) == "Grâce a 25 ans"


def test_formater_prix():
    assert formater_prix(1234567.5) == "1,234,567.50 FCFA"
    assert formater_prix(500) == "500.00 FCFA"


def test_code_ville():
    assert code_ville("Brazzaville") == "BRA"
    assert code_ville("pointe-noire") == "POI"


def test_inverser():
    assert inverser("Mbote") == "etobM"
    assert inverser("") == ""


def test_valeur_du_stock():
    assert valeur_du_stock("Manioc;500;12") == 6000
    assert valeur_du_stock("Sel;100;0") == 0


def test_telephone_valide():
    assert telephone_valide("060123456") is True
    assert telephone_valide("06012345a") is False
    assert telephone_valide("06012345") is False
    assert telephone_valide("0601234567") is False
