"""Solutions 10.3 — Style et conventions de nommage."""

import ast
import re

FONCTIONS_INTEGREES = {
    "list",
    "dict",
    "set",
    "str",
    "int",
    "sum",
    "max",
    "min",
    "len",
    "type",
    "id",
}


def vers_snake_case(texte: str) -> str:
    # Insère "_" entre une minuscule/chiffre et une majuscule, et avant la dernière majuscule d'un sigle.
    texte = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", texte)
    texte = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", texte)
    return texte.lower()


def vers_pascal_case(texte: str) -> str:
    return "".join(morceau.capitalize() for morceau in texte.split("_"))


def est_snake_case(nom: str) -> bool:
    return re.fullmatch(r"[a-z][a-z0-9_]*", nom) is not None


def est_constante(nom: str) -> bool:
    return re.fullmatch(r"[A-Z][A-Z0-9_]*", nom) is not None


def lignes_trop_longues(code: str, maximum: int = 100) -> list[int]:
    return [i for i, ligne in enumerate(code.splitlines(), start=1) if len(ligne) > maximum]


def indentation_correcte(code: str) -> bool:
    for ligne in code.splitlines():
        if not ligne.strip():
            continue
        debut = ligne[: len(ligne) - len(ligne.lstrip())]
        if "\t" in debut or len(debut) % 4 != 0:
            return False
    return True


def noms_masquant_le_langage(code: str) -> list[str]:
    noms = set()
    for noeud in ast.walk(ast.parse(code)):
        if isinstance(noeud, ast.Assign):
            for cible in noeud.targets:
                if isinstance(cible, ast.Name) and cible.id in FONCTIONS_INTEGREES:
                    noms.add(cible.id)
    return sorted(noms)


def prix_apres_remise(prix_unitaire: float, quantite: int, remise_pourcent: float) -> float:
    sous_total = prix_unitaire * quantite
    if remise_pourcent > 0:
        sous_total -= sous_total * remise_pourcent / 100
    return sous_total
