"""Tests de l'exercice 5.4. Ne modifie pas ce fichier."""

import pytest
from ex19_fonctions_comme_valeurs import (
    appliquer,
    calculer,
    composer,
    filtrer,
    meilleur_eleve,
    multiplicateur,
    trier_par_longueur,
    trier_par_prix,
)


def test_appliquer():
    assert appliquer(len, ["a", "bb"]) == [1, 2]
    assert appliquer(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert appliquer(str.upper, []) == []


def test_trier_par_prix():
    produits = [("Riz", 800), ("Sel", 100), ("Manioc", 500)]
    assert trier_par_prix(produits) == [("Sel", 100), ("Manioc", 500), ("Riz", 800)]
    assert produits[0] == ("Riz", 800)  # l'originale n'est pas modifiée


def test_meilleur_eleve():
    eleves = [{"nom": "Jean", "note": 12}, {"nom": "Grâce", "note": 17}, {"nom": "Paul", "note": 9}]
    assert meilleur_eleve(eleves) == "Grâce"


def test_trier_par_longueur():
    assert trier_par_longueur(["sucre", "riz", "sel", "huile"]) == ["riz", "sel", "huile", "sucre"]


def test_multiplicateur():
    triple = multiplicateur(3)
    assert triple(5) == 15
    assert multiplicateur(10)(4) == 40
    assert callable(triple)


@pytest.mark.parametrize(
    ("a", "op", "b", "attendu"),
    [
        (6, "+", 2, 8),
        (6, "-", 2, 4),
        (6, "*", 2, 12),
        (6, "/", 2, 3),
        (6, "/", 0, None),
        (6, "^", 2, None),
    ],
)
def test_calculer(a, op, b, attendu):
    assert calculer(a, op, b) == attendu


def test_filtrer():
    assert filtrer([1, 2, 3, 4], lambda n: n % 2 == 0) == [2, 4]
    assert filtrer(["a", "", "b"], bool) == ["a", "b"]
    assert filtrer([], lambda x: True) == []


def test_composer():
    h = composer(str.upper, str.strip)
    assert h("  mbote ") == "MBOTE"
    assert composer(lambda x: x + 1, lambda x: x * 2)(5) == 11
