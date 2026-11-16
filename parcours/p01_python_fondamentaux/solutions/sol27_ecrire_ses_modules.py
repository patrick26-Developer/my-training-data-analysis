"""Solutions 7.4 — Écrire ses modules."""

import importlib.util
import inspect
from os import PathLike
from pathlib import Path
from types import ModuleType

Chemin = str | PathLike[str]


def creer_module(dossier: Chemin, nom: str, code: str) -> Path:
    chemin = Path(dossier) / f"{nom}.py"
    chemin.write_text(code, encoding="utf-8")
    return chemin


def creer_package(dossier: Chemin, nom: str, modules: dict[str, str]) -> Path:
    racine = Path(dossier) / nom
    racine.mkdir(parents=True, exist_ok=True)
    (racine / "__init__.py").write_text("", encoding="utf-8")
    for nom_module, code in modules.items():
        creer_module(racine, nom_module, code)
    return racine


def executable_directement(code: str) -> bool:
    return any(ligne.strip() == 'if __name__ == "__main__":' for ligne in code.splitlines())


def importer_module(dossier: Chemin, nom: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(nom, Path(dossier) / f"{nom}.py")
    if spec is None or spec.loader is None:
        raise ImportError(f"Impossible d'importer {nom}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def liste_des_fonctions(module: ModuleType) -> list[str]:
    return sorted(
        nom
        for nom, valeur in vars(module).items()
        if inspect.isfunction(valeur) and not nom.startswith("_")
    )
