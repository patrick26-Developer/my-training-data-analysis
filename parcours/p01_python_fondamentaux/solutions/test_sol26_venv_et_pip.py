"""Tests des solutions 7.3. Généré par outils/sync_tests_solutions.py."""

import pytest
from sol26_venv_et_pip import (
    ajouter_dependance,
    commande_creation_venv,
    gitignore_contient_venv,
    lire_requirements,
    nom_du_paquet,
    non_figes,
    versions_figees,
)

CONTENU = """# dépendances
requests==2.32.5

pandas>=2.0
numpy
  fastapi[standard]==0.128.0
"""


@pytest.mark.parametrize(
    ("ligne", "attendu"),
    [
        ("requests==2.32.5", "requests"),
        ("pandas>=2.0", "pandas"),
        ("numpy", "numpy"),
        ("fastapi[standard]==0.1", "fastapi"),
        ("black~=24.1", "black"),
        ("urllib3!=1.0", "urllib3"),
        ("django<6", "django"),
    ],
)
def test_nom_du_paquet(ligne, attendu):
    assert nom_du_paquet(ligne) == attendu


def test_lire_requirements(tmp_path):
    chemin = tmp_path / "requirements.txt"
    chemin.write_text(CONTENU, encoding="utf-8")
    assert lire_requirements(chemin) == [
        "requests==2.32.5",
        "pandas>=2.0",
        "numpy",
        "fastapi[standard]==0.128.0",
    ]


def test_versions_figees(tmp_path):
    chemin = tmp_path / "requirements.txt"
    chemin.write_text(CONTENU, encoding="utf-8")
    assert versions_figees(chemin) == {"requests": "2.32.5", "fastapi": "0.128.0"}


def test_non_figes(tmp_path):
    chemin = tmp_path / "requirements.txt"
    chemin.write_text(CONTENU, encoding="utf-8")
    assert non_figes(chemin) == ["numpy", "pandas"]


def test_ajouter_dependance(tmp_path):
    chemin = tmp_path / "requirements.txt"
    assert ajouter_dependance(chemin, "requests==2.32.5") is True
    assert ajouter_dependance(chemin, "requests==9.9.9") is False
    assert ajouter_dependance(chemin, "numpy") is True
    assert lire_requirements(chemin) == ["requests==2.32.5", "numpy"]


def test_commande_creation_venv():
    assert commande_creation_venv() == "python -m venv venv"
    assert commande_creation_venv(".venv") == "python -m venv .venv"


def test_gitignore_contient_venv(tmp_path):
    chemin = tmp_path / ".gitignore"
    assert gitignore_contient_venv(chemin) is False
    chemin.write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
    assert gitignore_contient_venv(chemin) is False
    chemin.write_text("__pycache__/\nvenv/\n", encoding="utf-8")
    assert gitignore_contient_venv(chemin) is True
    chemin.write_text(".venv\n", encoding="utf-8")
    assert gitignore_contient_venv(chemin) is True
