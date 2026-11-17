"""Tests de l'exercice 8.1. Ne modifie pas ce fichier."""

import math

import pytest
from ex28_maths_et_formules import (
    aire_disque,
    angle_en_radians,
    capital_final,
    combinaisons_loto,
    hypotenuse,
    mensualite,
    perimetre_disque,
    resoudre_second_degre,
    sinus_en_degres,
    sont_egaux,
    variation_pourcentage,
    volume_cylindre,
)


def test_disque():
    assert aire_disque(1) == pytest.approx(math.pi)
    assert aire_disque(2) == pytest.approx(4 * math.pi)
    assert perimetre_disque(1) == pytest.approx(2 * math.pi)


def test_volume_cylindre():
    assert volume_cylindre(1, 10) == pytest.approx(10 * math.pi)


def test_hypotenuse():
    assert hypotenuse(3, 4) == pytest.approx(5.0)
    assert hypotenuse(1, 1) == pytest.approx(math.sqrt(2))


def test_capital_final():
    assert capital_final(1000, 10, 2) == pytest.approx(1210.0)
    assert capital_final(1000, 0, 5) == pytest.approx(1000.0)


def test_mensualite():
    assert mensualite(2_000_000, 12, 24) == pytest.approx(94146.95, abs=0.5)
    assert mensualite(1200, 0, 12) == pytest.approx(100.0)


@pytest.mark.parametrize(
    ("a", "b", "c", "attendu"),
    [(1, -3, 2, [1.0, 2.0]), (1, 2, 1, [-1.0]), (1, 0, 1, []), (2, -8, 0, [0.0, 4.0])],
)
def test_resoudre_second_degre(a, b, c, attendu):
    assert resoudre_second_degre(a, b, c) == pytest.approx(attendu)


def test_variation_pourcentage():
    assert variation_pourcentage(500, 650) == 30.0
    assert variation_pourcentage(200, 150) == -25.0
    assert variation_pourcentage(3, 4) == 33.33


def test_sont_egaux():
    assert sont_egaux(0.1 + 0.2, 0.3) is True
    assert sont_egaux(1, 1.001) is False


def test_combinaisons_loto():
    assert combinaisons_loto(49, 6) == 13983816
    assert combinaisons_loto(5, 2) == 10


def test_angles():
    assert angle_en_radians(180) == pytest.approx(math.pi)
    assert sinus_en_degres(90) == pytest.approx(1.0)
    assert sinus_en_degres(30) == pytest.approx(0.5)
