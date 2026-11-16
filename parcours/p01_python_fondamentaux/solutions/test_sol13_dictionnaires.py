"""Tests des solutions 4.3. Généré par outils/sync_tests_solutions.py."""

from sol13_dictionnaires import (
    admis,
    compter_lettres,
    fusionner_stocks,
    inverser,
    plus_cher,
    prix_du_produit,
    total_par_jour,
    valeur_du_stock,
)


def test_prix_du_produit():
    catalogue = {"Riz": 800, "Sel": 100}
    assert prix_du_produit(catalogue, "Riz") == 800
    assert prix_du_produit(catalogue, "Sucre") == 0


def test_compter_lettres():
    assert compter_lettres("banane") == {"b": 1, "a": 2, "n": 2, "e": 1}
    assert compter_lettres("") == {}


def test_valeur_du_stock():
    assert valeur_du_stock({"Riz": (800, 3), "Sel": (100, 10)}) == 3400
    assert valeur_du_stock({}) == 0


def test_plus_cher():
    assert plus_cher({"Riz": 800, "Sel": 100, "Huile": 1500}) == "Huile"
    assert plus_cher({}) is None


def test_total_par_jour():
    ventes = [("lundi", 500), ("mardi", 300), ("lundi", 200)]
    assert total_par_jour(ventes) == {"lundi": 700, "mardi": 300}
    assert total_par_jour([]) == {}


def test_inverser():
    assert inverser({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_admis():
    eleves = [
        {"nom": "Grâce", "note": 14},
        {"nom": "Jean", "note": 8},
        {"nom": "Marie", "note": 10},
    ]
    assert admis(eleves) == ["Grâce", "Marie"]
    assert admis([]) == []


def test_fusionner_stocks():
    a = {"Riz": 2, "Sel": 1}
    b = {"Riz": 3, "Sucre": 4}
    assert fusionner_stocks(a, b) == {"Riz": 5, "Sel": 1, "Sucre": 4}
    assert a == {"Riz": 2, "Sel": 1}  # les originaux ne sont pas modifiés
