"""Tests de l'exercice 2.1. Ne modifie pas ce fichier."""

import pytest
from ex05_booleens_et_comparaisons import (
    doit_retirer,
    est_admis,
    est_majeur,
    est_vide,
    est_voyelle,
    est_weekend,
    peut_emprunter,
)


@pytest.mark.parametrize(("age", "attendu"), [(17, False), (18, True), (40, True), (0, False)])
def test_est_majeur(age, attendu):
    assert est_majeur(age) is attendu


@pytest.mark.parametrize(
    ("note", "attendu"), [(9.99, False), (10, True), (20, True), (20.5, False), (-1, False)]
)
def test_est_admis(note, attendu):
    assert est_admis(note) is attendu


@pytest.mark.parametrize(
    ("jour", "attendu"),
    [("samedi", True), ("dimanche", True), ("lundi", False), ("", False)],
)
def test_est_weekend(jour, attendu):
    assert est_weekend(jour) is attendu


@pytest.mark.parametrize(
    ("stock", "perime", "attendu"),
    [(0, False, True), (5, True, True), (5, False, False), (0, True, True)],
)
def test_doit_retirer(stock, perime, attendu):
    assert doit_retirer(stock, perime) is attendu


@pytest.mark.parametrize(
    ("actif", "livres", "attendu"),
    [(True, 0, True), (True, 2, True), (True, 3, False), (False, 0, False)],
)
def test_peut_emprunter(actif, livres, attendu):
    assert peut_emprunter(actif, livres) is attendu


@pytest.mark.parametrize(
    ("texte", "attendu"), [("", True), ("   ", True), (" a ", False), ("abc", False)]
)
def test_est_vide(texte, attendu):
    assert est_vide(texte) is attendu


@pytest.mark.parametrize(
    ("lettre", "attendu"), [("a", True), ("E", True), ("y", True), ("b", False), ("Z", False)]
)
def test_est_voyelle(lettre, attendu):
    assert est_voyelle(lettre) is attendu
