"""Tests des solutions 7.4. Généré par outils/sync_tests_solutions.py."""

import subprocess
import sys

from sol27_ecrire_ses_modules import (
    creer_module,
    creer_package,
    executable_directement,
    importer_module,
    liste_des_fonctions,
)

CODE = """def double(x):
    return x * 2


def _prive():
    return 1


def triple(x):
    return x * 3


if __name__ == "__main__":
    print(double(21))
"""


def test_creer_module(tmp_path):
    chemin = creer_module(tmp_path, "calculs", CODE)
    assert chemin == tmp_path / "calculs.py"
    assert chemin.read_text(encoding="utf-8") == CODE


def test_creer_package(tmp_path):
    dossier = creer_package(tmp_path, "boutique", {"calculs": "X = 1\n", "stock": "Y = 2\n"})
    assert dossier == tmp_path / "boutique"
    assert (dossier / "__init__.py").read_text(encoding="utf-8") == ""
    assert (dossier / "calculs.py").read_text(encoding="utf-8") == "X = 1\n"
    assert (dossier / "stock.py").exists()


def test_executable_directement():
    assert executable_directement(CODE) is True
    assert executable_directement("def f():\n    pass\n") is False
    assert executable_directement('  if __name__ == "__main__":\n    pass') is True


def test_importer_module(tmp_path):
    creer_module(tmp_path, "calculs", CODE)
    module = importer_module(tmp_path, "calculs")
    assert module.double(4) == 8
    assert module.triple(4) == 12


def test_liste_des_fonctions(tmp_path):
    creer_module(tmp_path, "calculs", CODE)
    module = importer_module(tmp_path, "calculs")
    assert liste_des_fonctions(module) == ["double", "triple"]


def test_le_main_ne_s_execute_pas_a_l_import(tmp_path):
    chemin = creer_module(tmp_path, "calculs", CODE)
    importer_module(tmp_path, "calculs")  # ne doit rien afficher ni planter
    sortie = subprocess.run(
        [sys.executable, str(chemin)], capture_output=True, text=True, check=True
    ).stdout
    assert sortie.strip() == "42"
