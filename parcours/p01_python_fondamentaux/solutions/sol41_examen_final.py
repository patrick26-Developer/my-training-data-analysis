"""Corrigé de l'examen final P01 — Partie B."""

import csv
import re
from collections import Counter
from os import PathLike


def mention(note: float) -> str:
    """Retourne la mention d'une note sur 20.

    >>> mention(16)
    'Très bien'
    >>> mention(9.99)
    'Ajourné'

    Raises:
        ValueError: si la note n'est pas comprise entre 0 et 20.
    """
    if not 0 <= note <= 20:
        raise ValueError("La note doit être comprise entre 0 et 20.")
    if note >= 16:
        return "Très bien"
    if note >= 14:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
    return "Ajourné"


def mots_frequents(texte: str, n: int) -> list[tuple[str, int]]:
    """Retourne les n mots les plus fréquents avec leur nombre d'occurrences.

    >>> mots_frequents("a b a", 1)
    [('a', 2)]
    """
    propre = re.sub(r"[.,;:!?]", " ", texte.lower())
    compteur = Counter(propre.split())
    classement = sorted(compteur.items(), key=lambda couple: (-couple[1], couple[0]))
    return classement[:n]


def rendre_monnaie(montant: int, pieces: list[int]) -> dict[int, int]:
    """Retourne la monnaie à rendre avec l'algorithme glouton.

    >>> rendre_monnaie(1000, [500, 100])
    {500: 2}
    """
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif.")
    rendu: dict[int, int] = {}
    reste = montant
    for piece in sorted(pieces, reverse=True):
        nombre, reste = divmod(reste, piece)
        if nombre:
            rendu[piece] = nombre
    return rendu


def charger_notes(chemin: str | PathLike[str]) -> dict[str, float]:
    """Lit un CSV nom,note et retourne la moyenne par nom (lignes invalides ignorées).

    Un fichier absent donne un dictionnaire vide.
    """
    notes: dict[str, list[float]] = {}
    try:
        with open(chemin, newline="", encoding="utf-8") as f:
            for ligne in csv.DictReader(f):
                try:
                    valeur = float(ligne["note"])
                except (ValueError, KeyError, TypeError):
                    continue
                if 0 <= valeur <= 20 and ligne.get("nom"):
                    notes.setdefault(ligne["nom"], []).append(valeur)
    except FileNotFoundError:
        return {}
    return {nom: sum(valeurs) / len(valeurs) for nom, valeurs in notes.items()}


def est_equilibre(texte: str) -> bool:
    """Vrai si (), [] et {} sont correctement équilibrés et imbriqués.

    >>> est_equilibre("([]{})")
    True
    >>> est_equilibre("([)]")
    False
    """
    paires = {")": "(", "]": "[", "}": "{"}
    pile: list[str] = []
    for caractere in texte:
        if caractere in "([{":
            pile.append(caractere)
        elif caractere in paires:
            if not pile or pile.pop() != paires[caractere]:
                return False
    return not pile
