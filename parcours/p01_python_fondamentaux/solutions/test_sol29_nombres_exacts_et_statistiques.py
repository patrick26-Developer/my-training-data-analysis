"""Tests des solutions 8.2. Généré par outils/sync_tests_solutions.py."""

import random
from decimal import Decimal
from fractions import Fraction

import pytest
from sol29_nombres_exacts_et_statistiques import (
    lancer_des,
    probabilite_estimee,
    resume,
    somme_fractions,
    tirage_loto,
    total_exact,
    ttc,
    valeurs_aberrantes,
)


def test_total_exact():
    assert total_exact(["0.10", "0.20"]) == Decimal("0.30")
    assert total_exact([]) == Decimal("0")
    assert isinstance(total_exact(["1"]), Decimal)


def test_ttc():
    assert ttc("1999.99", "0.18") == Decimal("2359.99")
    assert ttc("100", "0.18") == Decimal("118.00")


def test_somme_fractions():
    assert somme_fractions([(1, 3), (1, 6)]) == Fraction(1, 2)
    assert somme_fractions([]) == Fraction(0)


def test_lancer_des():
    lancers = lancer_des(20, graine=3)
    assert len(lancers) == 20
    assert all(1 <= x <= 6 for x in lancers)
    assert lancers == lancer_des(20, graine=3)


def test_resume():
    assert resume([12, 15, 9, 18, 15, 11]) == {
        "moyenne": 13.33,
        "mediane": 13.5,
        "mode": 15,
        "ecart_type": 2.98,
    }


def test_valeurs_aberrantes():
    donnees = [10, 11, 9, 10, 12, 10, 11, 9, 10, 100]
    assert valeurs_aberrantes(donnees, k=2) == [100]
    assert valeurs_aberrantes([5, 5, 5, 5]) == []


def test_probabilite_estimee():
    def pile():
        return random.random() < 0.5

    p = probabilite_estimee(pile, 20_000, graine=1)
    assert p == pytest.approx(0.5, abs=0.02)
    assert p == probabilite_estimee(pile, 20_000, graine=1)


def test_tirage_loto():
    tirage = tirage_loto(graine=5)
    assert tirage == sorted(tirage)
    assert len(set(tirage)) == 6
    assert all(1 <= n <= 49 for n in tirage)
    assert tirage == tirage_loto(graine=5)
