"""Solutions 6.4 — pathlib."""

from os import PathLike
from pathlib import Path

Chemin = str | PathLike[str]


def extension(chemin: Chemin) -> str:
    return Path(chemin).suffix.lstrip(".").lower()


def changer_extension(chemin: Chemin, nouvelle: str) -> Path:
    return Path(chemin).with_suffix("." + nouvelle)


def creer_arborescence(racine: Chemin, noms: list[str]) -> int:
    racine = Path(racine)
    for nom in noms:
        (racine / nom).mkdir(parents=True, exist_ok=True)
    return sum(1 for element in racine.iterdir() if element.is_dir())


def lister_csv(dossier: Chemin) -> list[str]:
    return sorted(f.name for f in Path(dossier).glob("*.csv"))


def lister_python(dossier: Chemin) -> list[str]:
    return sorted(f.name for f in Path(dossier).rglob("*.py"))


def taille_totale(dossier: Chemin) -> int:
    total = 0
    for f in Path(dossier).rglob("*"):
        if f.is_file():
            total += f.stat().st_size
    return total


def ranger_par_extension(dossier: Chemin) -> dict[str, int]:
    dossier = Path(dossier)
    resultat: dict[str, int] = {}
    for fichier in list(dossier.iterdir()):  # list() : on déplace pendant le parcours
        if not fichier.is_file():
            continue
        nom_dossier = extension(fichier) or "sans_extension"
        cible = dossier / nom_dossier
        cible.mkdir(exist_ok=True)
        fichier.rename(cible / fichier.name)
        resultat[nom_dossier] = resultat.get(nom_dossier, 0) + 1
    return resultat


def dossier_du_script() -> Path:
    return Path(__file__).resolve().parent
