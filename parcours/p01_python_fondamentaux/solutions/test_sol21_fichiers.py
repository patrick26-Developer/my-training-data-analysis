"""Tests des solutions 6.2. Généré par outils/sync_tests_solutions.py."""

from sol21_fichiers import (
    ajouter_ligne,
    compter_lignes,
    compter_mots,
    copier_en_majuscules,
    derniere_ligne,
    ecrire_lignes,
    lire_lignes,
    valeur_du_stock,
)


def test_ecrire_puis_lire(tmp_path):
    chemin = tmp_path / "liste.txt"
    ecrire_lignes(chemin, ["Manioc", "Café crème", "Riz"])
    assert chemin.read_text(encoding="utf-8") == "Manioc\nCafé crème\nRiz\n"
    assert lire_lignes(chemin) == ["Manioc", "Café crème", "Riz"]


def test_ecrire_ecrase(tmp_path):
    chemin = tmp_path / "liste.txt"
    ecrire_lignes(chemin, ["a", "b"])
    ecrire_lignes(chemin, ["c"])
    assert lire_lignes(chemin) == ["c"]


def test_lire_lignes_ignore_vides_et_absent(tmp_path):
    chemin = tmp_path / "x.txt"
    assert lire_lignes(chemin) == []
    chemin.write_text("a\n\nb\n\n", encoding="utf-8")
    assert lire_lignes(chemin) == ["a", "b"]


def test_ajouter_ligne(tmp_path):
    chemin = tmp_path / "journal.txt"
    ajouter_ligne(chemin, "premiere")
    ajouter_ligne(chemin, "seconde")
    assert chemin.read_text(encoding="utf-8") == "premiere\nseconde\n"


def test_compter_lignes(tmp_path):
    chemin = tmp_path / "x.txt"
    assert compter_lignes(chemin) == 0
    chemin.write_text("a\n\nb\nc\n", encoding="utf-8")
    assert compter_lignes(chemin) == 3


def test_compter_mots(tmp_path):
    chemin = tmp_path / "x.txt"
    chemin.write_text("Mbote na bino\nTout le monde\n", encoding="utf-8")
    assert compter_mots(chemin) == 6


def test_valeur_du_stock(tmp_path):
    chemin = tmp_path / "stock.txt"
    chemin.write_text("Manioc;500;12\n\nRiz;800;3\n", encoding="utf-8")
    assert valeur_du_stock(chemin) == 8400


def test_copier_en_majuscules(tmp_path):
    source = tmp_path / "a.txt"
    destination = tmp_path / "b.txt"
    source.write_text("Mbote\nÉcole\n", encoding="utf-8")
    copier_en_majuscules(source, destination)
    assert destination.read_text(encoding="utf-8") == "MBOTE\nÉCOLE\n"


def test_derniere_ligne(tmp_path):
    chemin = tmp_path / "x.txt"
    assert derniere_ligne(chemin) is None
    chemin.write_text("", encoding="utf-8")
    assert derniere_ligne(chemin) is None
    chemin.write_text("a\nb\n\n", encoding="utf-8")
    assert derniere_ligne(chemin) == "b"
