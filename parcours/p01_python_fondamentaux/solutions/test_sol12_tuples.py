"""Tests des solutions 4.2. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol12_tuples import (
    associer,
    chiffre_affaires,
    distance,
    diviser,
    echanger,
    formater_date,
    resume,
)


def test_echanger():
    assert echanger((1, 2)) == (2, 1)
    assert echanger(("a", "b")) == ("b", "a")


@pytest.mark.parametrize(("a", "b", "attendu"), [(17, 5, (3, 2)), (10, 2, (5, 0)), (3, 7, (0, 3))])
def test_diviser(a, b, attendu):
    assert diviser(a, b) == attendu


@pytest.mark.parametrize(
    ("date", "attendu"), [((5, 3, 2026), "05/03/2026"), ((16, 11, 2026), "16/11/2026")]
)
def test_formater_date(date, attendu):
    assert formater_date(date) == attendu


@pytest.mark.parametrize(
    ("p1", "p2", "attendu"), [((0, 0), (3, 4), 5.0), ((1, 1), (1, 1), 0.0), ((0, 0), (1, 1), 1.41)]
)
def test_distance(p1, p2, attendu):
    assert distance(p1, p2) == pytest.approx(attendu)


def test_associer():
    assert associer(["Riz", "Sel"], [800, 100]) == [("Riz", 800), ("Sel", 100)]
    assert associer([], []) == []


def test_chiffre_affaires():
    assert chiffre_affaires([("Riz", 2, 800), ("Sel", 5, 100)]) == 2100
    assert chiffre_affaires([]) == 0


def test_resume():
    assert resume([1, 2, 3, 4, 5]) == (1, 5, 3)
    assert resume([1, 2]) == (1, 2, 0)
