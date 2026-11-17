"""Tests des solutions 9.1. Généré par outils/sync_tests_solutions.py."""

import math

import pytest
from sol32_turtle import (
    aire_polygone,
    angle_de_rotation,
    angle_interieur,
    chemin_carre,
    longueur_cote,
    perimetre_polygone,
    position_finale,
    sommets_polygone,
)


@pytest.mark.parametrize(("n", "attendu"), [(3, 120.0), (4, 90.0), (6, 60.0), (360, 1.0)])
def test_angle_de_rotation(n, attendu):
    assert angle_de_rotation(n) == pytest.approx(attendu)


@pytest.mark.parametrize(("n", "attendu"), [(3, 60.0), (4, 90.0), (6, 120.0)])
def test_angle_interieur(n, attendu):
    assert angle_interieur(n) == pytest.approx(attendu)


def test_sommets_polygone():
    carre = sommets_polygone(4, 1)
    attendus = [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)]
    assert len(carre) == 4
    for (x, y), (ex, ey) in zip(carre, attendus, strict=True):
        assert x == pytest.approx(ex, abs=1e-6)
        assert y == pytest.approx(ey, abs=1e-6)
    hexagone = sommets_polygone(6, 10)
    assert len(hexagone) == 6
    assert all(math.isclose(math.hypot(x, y), 10, abs_tol=1e-5) for x, y in hexagone)
    assert hexagone[0] == (10.0, 0.0)


def test_perimetre_polygone():
    assert perimetre_polygone([(0, 0), (4, 0), (4, 3), (0, 3)]) == 14.0
    assert perimetre_polygone([(0, 0), (3, 0), (0, 4)]) == 12.0


def test_longueur_cote():
    assert longueur_cote(6, 10) == pytest.approx(10.0)  # hexagone : côté = rayon
    assert longueur_cote(4, 1) == pytest.approx(math.sqrt(2), abs=1e-6)


def test_chemin_carre():
    chemin = chemin_carre(50)
    assert len(chemin) == 8
    assert chemin[:2] == [("forward", 50), ("left", 90)]
    assert chemin.count(("forward", 50)) == 4


def test_position_finale():
    assert position_finale(chemin_carre(50)) == (0.0, 0.0)
    assert position_finale([("forward", 10)]) == (10.0, 0.0)
    assert position_finale([("left", 90), ("forward", 10)]) == (0.0, 10.0)
    assert position_finale([("right", 90), ("forward", 10)]) == (0.0, -10.0)
    assert position_finale([]) == (0.0, 0.0)


def test_aire_polygone():
    assert aire_polygone([(0, 0), (4, 0), (4, 3), (0, 3)]) == 12.0
    assert aire_polygone([(0, 0), (4, 0), (0, 3)]) == 6.0
    assert aire_polygone(sommets_polygone(4, 1)) == pytest.approx(2.0)
