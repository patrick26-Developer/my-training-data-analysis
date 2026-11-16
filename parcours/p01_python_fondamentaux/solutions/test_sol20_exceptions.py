"""Tests des solutions 6.1. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol20_exceptions import (
    StockInsuffisant,
    convertir_entier,
    diviser_sans_erreur,
    premier_entier_valide,
    retirer,
    somme_tolerante,
    valeur_ou_defaut,
    vendre,
)


@pytest.mark.parametrize(
    ("texte", "attendu"), [("42", 42), ("-7", -7), ("abc", None), ("", None), ("2.5", None)]
)
def test_convertir_entier(texte, attendu):
    assert convertir_entier(texte) == attendu


def test_diviser_sans_erreur():
    assert diviser_sans_erreur(10, 4) == pytest.approx(2.5)
    assert diviser_sans_erreur(1, 0) is None


def test_valeur_ou_defaut():
    assert valeur_ou_defaut({"a": 1}, "a", 0) == 1
    assert valeur_ou_defaut({"a": 1}, "b", 0) == 0


def test_retirer():
    assert retirer(1000, 300) == 700
    with pytest.raises(ValueError, match="Montant invalide"):
        retirer(1000, 0)
    with pytest.raises(ValueError, match="Solde insuffisant"):
        retirer(1000, 5000)


def test_premier_entier_valide():
    assert premier_entier_valide(["abc", "x1", "12", "7"]) == 12
    with pytest.raises(ValueError, match="Aucune saisie valide"):
        premier_entier_valide(["a", "b"])


def test_somme_tolerante():
    assert somme_tolerante(["10", "abc", "2.5", "5"]) == pytest.approx(17.5)
    assert somme_tolerante([]) == 0


def test_stock_insuffisant():
    assert issubclass(StockInsuffisant, Exception)
    assert vendre(10, 3) == 7
    with pytest.raises(StockInsuffisant):
        vendre(2, 5)
