"""Tests des solutions 2.2. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol06_if_elif_else import (
    est_bissextile,
    mention,
    parite,
    plus_grand,
    prix_ticket,
    taux_remise,
    type_triangle,
)


@pytest.mark.parametrize(
    ("n", "attendu"), [(0, "pair"), (7, "impair"), (10, "pair"), (-3, "impair")]
)
def test_parite(n, attendu):
    assert parite(n) == attendu


@pytest.mark.parametrize(
    ("note", "attendu"),
    [
        (20, "Très bien"),
        (16, "Très bien"),
        (15.5, "Bien"),
        (12, "Assez bien"),
        (10, "Passable"),
        (9.9, "Ajourné"),
        (0, "Ajourné"),
    ],
)
def test_mention(note, attendu):
    assert mention(note) == attendu


@pytest.mark.parametrize(
    ("quantite", "attendu"), [(1, 0), (9, 0), (10, 5), (49, 5), (50, 10), (500, 10)]
)
def test_taux_remise(quantite, attendu):
    assert taux_remise(quantite) == attendu


@pytest.mark.parametrize(
    ("age", "attendu"), [(5, 100), (11, 100), (12, 200), (64, 200), (65, 0), (90, 0)]
)
def test_prix_ticket(age, attendu):
    assert prix_ticket(age) == attendu


@pytest.mark.parametrize(
    ("a", "b", "c", "attendu"),
    [(1, 2, 3, 3), (3, 2, 1, 3), (2, 9, 4, 9), (5, 5, 5, 5), (-1, -5, -3, -1)],
)
def test_plus_grand(a, b, c, attendu):
    assert plus_grand(a, b, c) == attendu


@pytest.mark.parametrize(
    ("annee", "attendu"),
    [(2000, True), (1900, False), (2024, True), (2023, False), (2100, False)],
)
def test_est_bissextile(annee, attendu):
    assert est_bissextile(annee) is attendu


@pytest.mark.parametrize(
    ("a", "b", "c", "attendu"),
    [
        (3, 3, 3, "equilateral"),
        (3, 3, 4, "isocele"),
        (4, 3, 3, "isocele"),
        (3, 4, 3, "isocele"),
        (3, 4, 5, "scalene"),
    ],
)
def test_type_triangle(a, b, c, attendu):
    assert type_triangle(a, b, c) == attendu
