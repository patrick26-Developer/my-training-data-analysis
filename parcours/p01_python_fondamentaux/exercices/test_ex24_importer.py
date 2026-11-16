"""Tests de l'exercice 7.1. Ne modifie pas ce fichier."""

import math

import pytest
from ex24_importer import (
    aire_cercle,
    arrondi_inferieur,
    arrondi_superieur,
    existe_module,
    mot_le_plus_frequent,
    nom_du_module_de,
    nombres_aleatoires,
    racine,
)


def test_racine():
    assert racine(16) == 4.0
    assert racine(2) == pytest.approx(math.sqrt(2))


def test_aire_cercle():
    assert aire_cercle(1) == 3.14
    assert aire_cercle(2) == 12.57


def test_arrondis():
    assert arrondi_superieur(2.1) == 3
    assert arrondi_inferieur(2.9) == 2
    assert arrondi_superieur(-2.1) == -2
    assert arrondi_inferieur(-2.1) == -3


def test_nombres_aleatoires():
    nombres = nombres_aleatoires(50, 1, 6)
    assert len(nombres) == 50
    assert all(1 <= n <= 6 for n in nombres)
    assert nombres_aleatoires(5, 1, 100, graine=42) == nombres_aleatoires(5, 1, 100, graine=42)


def test_mot_le_plus_frequent():
    assert mot_le_plus_frequent(["a", "b", "a", "c", "a", "b"]) == "a"
    assert mot_le_plus_frequent([]) is None


def test_existe_module():
    assert existe_module("math") is True
    assert existe_module("module_qui_n_existe_pas_xyz") is False


def test_nom_du_module_de():
    assert nom_du_module_de(math.sqrt) == "math"
    assert nom_du_module_de(len) == "builtins"
    assert nom_du_module_de(42) is None
