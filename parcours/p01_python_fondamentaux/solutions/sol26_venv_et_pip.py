"""Solutions 7.3 — venv et pip."""

import re
from os import PathLike
from pathlib import Path

Chemin = str | PathLike[str]


def nom_du_paquet(ligne: str) -> str:
    # On garde les lettres, chiffres, "-", "_" et "." du début de la ligne.
    correspondance = re.match(r"[A-Za-z0-9_.\-]+", ligne.strip())
    return correspondance.group(0) if correspondance else ""


def lire_requirements(chemin: Chemin) -> list[str]:
    lignes = []
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if ligne and not ligne.startswith("#"):
            lignes.append(ligne)
    return lignes


def versions_figees(chemin: Chemin) -> dict[str, str]:
    figees = {}
    for ligne in lire_requirements(chemin):
        if "==" in ligne:
            _, version = ligne.split("==", 1)
            figees[nom_du_paquet(ligne)] = version
    return figees


def non_figes(chemin: Chemin) -> list[str]:
    return sorted(nom_du_paquet(ligne) for ligne in lire_requirements(chemin) if "==" not in ligne)


def ajouter_dependance(chemin: Chemin, ligne: str) -> bool:
    chemin = Path(chemin)
    existants = lire_requirements(chemin) if chemin.exists() else []
    noms = {nom_du_paquet(e).lower() for e in existants}
    if nom_du_paquet(ligne).lower() in noms:
        return False
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return True


def commande_creation_venv(nom: str = "venv") -> str:
    return f"python -m venv {nom}"


def gitignore_contient_venv(chemin: Chemin) -> bool:
    chemin = Path(chemin)
    if not chemin.exists():
        return False
    lignes = {ligne.strip() for ligne in chemin.read_text(encoding="utf-8").splitlines()}
    return bool(lignes & {"venv/", ".venv/", "venv", ".venv"})
