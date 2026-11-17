"""Tests de l'examen final (partie B). Ne modifie pas ce fichier."""

import pytest
from ex41_examen_final import (
    charger_notes,
    est_equilibre,
    mention,
    mots_frequents,
    rendre_monnaie,
)

FONCTIONS = [mention, mots_frequents, rendre_monnaie, charger_notes, est_equilibre]


# ---------------------------------------------------------------- problème 1
@pytest.mark.parametrize(
    ("note", "attendu"),
    [
        (20, "Très bien"),
        (16, "Très bien"),
        (15.99, "Bien"),
        (14, "Bien"),
        (13.5, "Assez bien"),
        (12, "Assez bien"),
        (10, "Passable"),
        (9.99, "Ajourné"),
        (0, "Ajourné"),
    ],
)
def test_mention(note, attendu):
    assert mention(note) == attendu


@pytest.mark.parametrize("note", [-0.1, 20.1, -5, 100])
def test_mention_invalide(note):
    with pytest.raises(ValueError):
        mention(note)


# ---------------------------------------------------------------- problème 2
def test_mots_frequents():
    texte = "Le riz, le manioc ! Le riz et le sel; manioc? riz."
    assert mots_frequents(texte, 2) == [("le", 4), ("riz", 3)]
    assert mots_frequents(texte, 3)[2] == ("manioc", 2)


def test_mots_frequents_egalite_ordre_alphabetique():
    assert mots_frequents("b a c a b c", 3) == [("a", 2), ("b", 2), ("c", 2)]


def test_mots_frequents_cas_limites():
    assert mots_frequents("", 3) == []
    assert mots_frequents("un deux", 5) == [("deux", 1), ("un", 1)]
    assert mots_frequents("Riz riz RIZ", 1) == [("riz", 3)]


# ---------------------------------------------------------------- problème 3
def test_rendre_monnaie():
    assert rendre_monnaie(675, [25, 500, 100, 50]) == {500: 1, 100: 1, 50: 1, 25: 1}
    assert rendre_monnaie(1000, [500, 100]) == {500: 2}
    assert rendre_monnaie(0, [500]) == {}
    assert rendre_monnaie(30, [10, 5]) == {10: 3}


def test_rendre_monnaie_negatif():
    with pytest.raises(ValueError):
        rendre_monnaie(-1, [10])


# ---------------------------------------------------------------- problème 4
def test_charger_notes(tmp_path):
    chemin = tmp_path / "notes.csv"
    chemin.write_text(
        "nom,note\nJean,12\nMarie,16\nJean,14\nPaul,abc\nMarie,21\nLuc,-1\nPaul,10\n",
        encoding="utf-8",
    )
    assert charger_notes(chemin) == {"Jean": 13.0, "Marie": 16.0, "Paul": 10.0}


def test_charger_notes_absent_ou_vide(tmp_path):
    assert charger_notes(tmp_path / "absent.csv") == {}
    vide = tmp_path / "vide.csv"
    vide.write_text("nom,note\n", encoding="utf-8")
    assert charger_notes(vide) == {}


def test_charger_notes_decimales(tmp_path):
    chemin = tmp_path / "n.csv"
    chemin.write_text("nom,note\nA,12.5\nA,13.5\n", encoding="utf-8")
    assert charger_notes(chemin) == {"A": 13.0}


# ---------------------------------------------------------------- problème 5
@pytest.mark.parametrize(
    ("texte", "attendu"),
    [
        ("", True),
        ("()", True),
        ("([]{})", True),
        ("f(x[1]) + {a: (b)}", True),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("((())", False),
        ("{[}", False),
        ("]", False),
    ],
)
def test_est_equilibre(texte, attendu):
    assert est_equilibre(texte) is attendu


# ---------------------------------------------------------------- problème 6 (partiel)
@pytest.mark.parametrize("fonction", FONCTIONS, ids=lambda f: f.__name__)
def test_docstrings(fonction):
    assert fonction.__doc__ and len(fonction.__doc__.strip()) >= 15
