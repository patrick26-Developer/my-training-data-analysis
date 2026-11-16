"""Tests de l'exercice 5.3. Ne modifie pas ce fichier."""

import inspect

import ex18_portee_et_recursivite as ex
import pytest


def test_tva_globale():
    assert ex.TVA == 18


def test_prix_ttc():
    assert ex.prix_ttc(1000) == pytest.approx(1180.0)


def test_incrementer():
    assert ex.incrementer(5) == 6
    assert ex.incrementer(5, pas=10) == 15


def test_ajouter_sans_modifier():
    original = ["Riz"]
    resultat = ex.ajouter_sans_modifier(original, "Sel")
    assert resultat == ["Riz", "Sel"]
    assert original == ["Riz"]


@pytest.mark.parametrize(("n", "attendu"), [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorielle(n, attendu):
    assert ex.factorielle(n) == attendu


def test_factorielle_est_recursive():
    assert "factorielle(" in inspect.getsource(ex.factorielle).split("\n", 1)[1]


@pytest.mark.parametrize(("n", "attendu"), [(0, 0), (1, 1), (10, 55), (100, 5050)])
def test_somme_recursive(n, attendu):
    assert ex.somme_recursive(n) == attendu


@pytest.mark.parametrize(("b", "e", "attendu"), [(2, 10, 1024), (5, 0, 1), (3, 3, 27), (7, 1, 7)])
def test_puissance(b, e, attendu):
    assert ex.puissance(b, e) == attendu


@pytest.mark.parametrize(("texte", "attendu"), [("Mbote", "etobM"), ("", ""), ("a", "a")])
def test_inverser(texte, attendu):
    assert ex.inverser(texte) == attendu


@pytest.mark.parametrize(
    ("n", "attendu"), [(0, 0), (1, 1), (2, 1), (10, 55), (90, 2880067194370816120)]
)
def test_fibonacci(n, attendu):
    assert ex.fibonacci(n) == attendu


@pytest.mark.parametrize(("a", "b", "attendu"), [(48, 18, 6), (17, 5, 1), (10, 0, 10), (0, 7, 7)])
def test_pgcd(a, b, attendu):
    assert ex.pgcd(a, b) == attendu
