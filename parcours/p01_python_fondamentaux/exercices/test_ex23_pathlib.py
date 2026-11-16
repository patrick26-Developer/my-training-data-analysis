"""Tests de l'exercice 6.4. Ne modifie pas ce fichier."""

from pathlib import Path

import pytest
from ex23_pathlib import (
    changer_extension,
    creer_arborescence,
    dossier_du_script,
    extension,
    lister_csv,
    lister_python,
    ranger_par_extension,
    taille_totale,
)


@pytest.mark.parametrize(
    ("chemin", "attendu"),
    [("rapport.PDF", "pdf"), ("Makefile", ""), ("a/b.tar.gz", "gz"), ("photo.jpeg", "jpeg")],
)
def test_extension(chemin, attendu):
    assert extension(chemin) == attendu


def test_changer_extension():
    assert changer_extension("a/b.txt", "md") == Path("a/b.md")
    assert changer_extension(Path("x.csv"), "json") == Path("x.json")


def test_creer_arborescence(tmp_path):
    assert creer_arborescence(tmp_path, ["a", "b"]) == 2
    assert creer_arborescence(tmp_path, ["a", "c"]) == 3  # "a" existe déjà : pas d'erreur
    assert (tmp_path / "c").is_dir()


def test_lister_csv(tmp_path):
    (tmp_path / "b.csv").write_text("x")
    (tmp_path / "a.csv").write_text("x")
    (tmp_path / "c.txt").write_text("x")
    (tmp_path / "sous").mkdir()
    (tmp_path / "sous" / "d.csv").write_text("x")
    assert lister_csv(tmp_path) == ["a.csv", "b.csv"]


def test_lister_python(tmp_path):
    (tmp_path / "z.py").write_text("x")
    (tmp_path / "sous").mkdir()
    (tmp_path / "sous" / "a.py").write_text("x")
    (tmp_path / "note.txt").write_text("x")
    assert lister_python(tmp_path) == ["a.py", "z.py"]


def test_taille_totale(tmp_path):
    (tmp_path / "a.txt").write_bytes(b"12345")
    (tmp_path / "sous").mkdir()
    (tmp_path / "sous" / "b.txt").write_bytes(b"123")
    assert taille_totale(tmp_path) == 8


def test_ranger_par_extension(tmp_path):
    (tmp_path / "a.txt").write_text("x")
    (tmp_path / "b.txt").write_text("x")
    (tmp_path / "c.csv").write_text("x")
    (tmp_path / "LISEZMOI").write_text("x")
    resultat = ranger_par_extension(tmp_path)
    assert resultat == {"txt": 2, "csv": 1, "sans_extension": 1}
    assert (tmp_path / "txt" / "a.txt").exists()
    assert (tmp_path / "csv" / "c.csv").exists()
    assert (tmp_path / "sans_extension" / "LISEZMOI").exists()
    assert not (tmp_path / "a.txt").exists()


def test_dossier_du_script():
    resultat = dossier_du_script()
    assert isinstance(resultat, Path)
    assert (resultat / "ex23_pathlib.py").exists() or (resultat / "sol23_pathlib.py").exists()
