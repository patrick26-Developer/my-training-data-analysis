"""Tests de l'exercice 10.4. Ne modifie pas ce fichier."""

import doctest

import ex39_documenter as module
import pytest
from ex39_documenter import carre, est_pair, fusionner_mots, initiales, prix_ttc

FONCTIONS = [carre, est_pair, initiales, prix_ttc, fusionner_mots]


def test_carre():
    assert carre(4) == 16
    assert carre(-3) == 9


def test_est_pair():
    assert est_pair(4) is True
    assert est_pair(7) is False


def test_initiales():
    assert initiales("Grâce Marie Nzoni") == "G.M.N."
    assert initiales("jean") == "J."


def test_prix_ttc():
    assert prix_ttc(1000) == pytest.approx(1180.0)
    assert prix_ttc(333, 5) == pytest.approx(349.65)


def test_fusionner_mots():
    assert fusionner_mots(["a", "b", "c"]) == "a-b-c"
    assert fusionner_mots([]) == ""


@pytest.mark.parametrize("fonction", FONCTIONS, ids=lambda f: f.__name__)
def test_docstring_presente(fonction):
    assert fonction.__doc__ and len(fonction.__doc__.strip()) >= 10


@pytest.mark.parametrize("fonction", FONCTIONS, ids=lambda f: f.__name__)
def test_exemples_doctest_presents_et_valides(fonction):
    tests = doctest.DocTestFinder().find(fonction, fonction.__name__, globs=vars(module))
    exemples = [e for t in tests for e in t.examples]
    assert exemples, f"{fonction.__name__} n'a aucun exemple doctest (>>> ...)"
    executeur = doctest.DocTestRunner(verbose=False)
    for t in tests:
        executeur.run(t)
    assert executeur.failures == 0, f"Un exemple doctest de {fonction.__name__} échoue"


def test_docstring_prix_ttc_documente_taux():
    assert "taux" in prix_ttc.__doc__


def test_docstring_du_module():
    assert module.__doc__ and "Mayele" in module.__doc__
