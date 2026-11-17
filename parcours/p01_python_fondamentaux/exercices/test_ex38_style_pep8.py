"""Tests de l'exercice 10.3. Ne modifie pas ce fichier."""

import inspect

import pytest
from ex38_style_pep8 import (
    est_constante,
    est_snake_case,
    indentation_correcte,
    lignes_trop_longues,
    noms_masquant_le_langage,
    prix_apres_remise,
    vers_pascal_case,
    vers_snake_case,
)


@pytest.mark.parametrize(
    ("texte", "attendu"),
    [
        ("CompteBancaire", "compte_bancaire"),
        ("prixTotal", "prix_total"),
        ("HTTPServer", "http_server"),
        ("simple", "simple"),
        ("DejaLa", "deja_la"),
    ],
)
def test_vers_snake_case(texte, attendu):
    assert vers_snake_case(texte) == attendu


@pytest.mark.parametrize(
    ("texte", "attendu"),
    [("compte_bancaire", "CompteBancaire"), ("prix", "Prix"), ("a_b_c", "ABC")],
)
def test_vers_pascal_case(texte, attendu):
    assert vers_pascal_case(texte) == attendu


@pytest.mark.parametrize(
    ("nom", "attendu"),
    [("prix_total", True), ("PrixTotal", False), ("prix2", True), ("2prix", False), ("a-b", False)],
)
def test_est_snake_case(nom, attendu):
    assert est_snake_case(nom) is attendu


@pytest.mark.parametrize(
    ("nom", "attendu"),
    [("TAUX_TVA", True), ("taux", False), ("Taux", False), ("MAX2", True), ("_X", False)],
)
def test_est_constante(nom, attendu):
    assert est_constante(nom) is attendu


def test_lignes_trop_longues():
    code = "court\n" + "x" * 101 + "\nmoyen\n" + "y" * 120
    assert lignes_trop_longues(code) == [2, 4]
    assert lignes_trop_longues(code, maximum=4) == [1, 2, 3, 4]
    assert lignes_trop_longues("abc", maximum=3) == []


def test_indentation_correcte():
    assert indentation_correcte("def f():\n    return 1\n") is True
    assert indentation_correcte("def f():\n  return 1\n") is False
    assert indentation_correcte("def f():\n\treturn 1\n") is False
    assert indentation_correcte("if x:\n    if y:\n        pass\n\n") is True
    assert indentation_correcte("") is True


def test_noms_masquant_le_langage():
    assert noms_masquant_le_langage("list = [1]\nsum = 0\nx = 2") == ["list", "sum"]
    assert noms_masquant_le_langage("a = 1\nb = 2") == []
    assert noms_masquant_le_langage("max = 1\nmax = 2") == ["max"]


def test_prix_apres_remise():
    assert prix_apres_remise(1000, 2, 10) == pytest.approx(1800.0)
    assert prix_apres_remise(500, 3, 0) == pytest.approx(1500.0)
    assert prix_apres_remise(100, 1, 100) == pytest.approx(0.0)
    noms = list(inspect.signature(prix_apres_remise).parameters)
    assert noms == ["prix_unitaire", "quantite", "remise_pourcent"]
