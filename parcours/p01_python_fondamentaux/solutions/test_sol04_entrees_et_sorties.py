"""Tests des solutions 1.4. Copie des tests d'exercice appliquée aux solutions."""

import pytest
from sol04_entrees_et_sorties import (
    additionner_saisies,
    demander_prenom,
    recu,
    saluer_utilisateur,
    total_saisi,
)


def simuler_saisies(monkeypatch, *reponses):
    """Remplace input() : chaque appel renvoie la réponse suivante."""
    iterateur = iter(reponses)
    monkeypatch.setattr("builtins.input", lambda *_args: next(iterateur))


def test_demander_prenom(monkeypatch):
    simuler_saisies(monkeypatch, "  grâce mARIE ")
    assert demander_prenom() == "Grâce Marie"


def test_additionner_saisies(monkeypatch):
    simuler_saisies(monkeypatch, "2.5", "4")
    assert additionner_saisies() == pytest.approx(6.5)


def test_additionner_saisies_virgule(monkeypatch):
    simuler_saisies(monkeypatch, "2,5", "1,5")
    assert additionner_saisies() == pytest.approx(4.0)


def test_total_saisi(monkeypatch):
    simuler_saisies(monkeypatch, "2500", "3")
    assert total_saisi() == pytest.approx(7500.0)


def test_saluer_utilisateur(monkeypatch, capsys):
    simuler_saisies(monkeypatch, " jean ")
    saluer_utilisateur()
    assert capsys.readouterr().out == "Mbote, Jean !\n"


def test_recu():
    attendu = "Client   : Grâce\nQuantité : 3\nTotal    : 7,500 FCFA"
    assert recu("Grâce", 3, 7500) == attendu
