"""Exécuter les exemples de code réellement publiés dans les leçons.

Les exemples d'une leçon forment un tutoriel progressif : chacun peut utiliser les noms définis par les
précédents. On les exécute donc dans l'ordre, dans un même espace de noms, une leçon à la fois.
"""

import re
from pathlib import Path

import pytest

LECONS = Path(__file__).resolve().parents[1] / "lecons"
FICHIERS = sorted(LECONS.glob("*.md"))
EXTRAIT = re.compile(r"```python\n(.*?)```", re.S)


@pytest.mark.parametrize("chemin", FICHIERS, ids=[f.stem for f in FICHIERS])
def test_exemples_de_la_lecon(chemin):
    blocs = EXTRAIT.findall(chemin.read_text(encoding="utf-8"))
    assert blocs, f"{chemin.name} ne contient aucun exemple Python"
    espace = {"__name__": "__exemple__"}
    for numero, bloc in enumerate(blocs, 1):
        try:
            exec(compile(bloc, f"{chemin.stem}-bloc{numero}", "exec"), espace)
        except Exception as erreur:
            pytest.fail(f"{chemin.name}, exemple n°{numero} : {type(erreur).__name__}: {erreur}")
