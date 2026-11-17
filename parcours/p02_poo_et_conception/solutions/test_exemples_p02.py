"""Exécuter les exemples autonomes réellement publiés dans les leçons."""

import re
from pathlib import Path

import pytest

LECONS = Path(__file__).resolve().parents[1] / "lecons"
EXEMPLES = [
    (f"{chemin.stem}-{numero}", bloc)
    for chemin in sorted(LECONS.glob("*.md"))
    for numero, bloc in enumerate(
        re.findall(r"```python\n(.*?)```", chemin.read_text(encoding="utf-8"), re.S), 1
    )
]


@pytest.mark.parametrize(("nom", "bloc"), EXEMPLES, ids=[nom for nom, _ in EXEMPLES])
def test_exemple(nom, bloc):
    exec(compile(bloc, nom, "exec"), {"__name__": "__exemple__"})
