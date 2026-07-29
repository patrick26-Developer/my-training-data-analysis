"""Exercice 1.1 — Typing avancé & structures de données.

Complete chaque TODO. Lance les tests avec :
    python -m pytest 01_python_senior/exercices/test_ex01_typing_et_structures_de_donnees.py -v

Ne modifie pas les signatures (noms, paramètres, types de retour) : les tests s'appuient dessus.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, NamedTuple, Protocol, TypedDict, overload


# ---------------------------------------------------------------------------
# 1. Dataclass immuable avec méthode
# ---------------------------------------------------------------------------
# TODO : transforme Point3D en dataclass immuable (frozen) et optimisée mémoire (slots).
# Ajoute une méthode distance_to(other) -> float qui calcule la distance euclidienne 3D.
class Point3D:
    x: float
    y: float
    z: float = 0.0

    def distance_to(self, other: Point3D) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------------------
# 2. NamedTuple
# ---------------------------------------------------------------------------
# TODO : définis RGB comme un NamedTuple avec trois champs entiers r, g, b (0-255 non validé ici).
class RGB:
    pass


# ---------------------------------------------------------------------------
# 3. TypedDict
# ---------------------------------------------------------------------------
# TODO : définis UserPayload comme un TypedDict avec les clés :
#   id: int, email: str, is_active: bool
class UserPayload:
    pass


def make_user_payload(user_id: int, email: str, is_active: bool) -> UserPayload:
    """Construit un UserPayload à partir des champs donnés."""
    # TODO : implémente en retournant un dict conforme à UserPayload.
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 4. Protocol + fonction générique
# ---------------------------------------------------------------------------
class Comparable(Protocol):
    """TODO : déclare la méthode requise (__lt__) pour qu'un objet soit 'Comparable'."""


def plus_petit[T: Comparable](a: T, b: T) -> T:
    """Retourne le plus petit des deux éléments comparables."""
    # TODO : implémente en utilisant l'opérateur < (pas min()).
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 5. Classe générique Stack[T]
# ---------------------------------------------------------------------------
class Stack[T]:
    """Pile générique LIFO."""

    def __init__(self) -> None:
        # TODO : initialise le stockage interne (liste typée).
        raise NotImplementedError

    def push(self, item: T) -> None:
        raise NotImplementedError

    def pop(self) -> T:
        """Retire et retourne le dernier élément. Lève IndexError si la pile est vide."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------------
# 6. @overload
# ---------------------------------------------------------------------------
# TODO : ajoute les deux décorateurs @overload manquants au-dessus de l'implémentation,
# pour documenter que process(int) -> str et process(str) -> int.
def process(value: int | str) -> str | int:
    if isinstance(value, int):
        return str(value)
    return int(value)


# ---------------------------------------------------------------------------
# 7. Literal
# ---------------------------------------------------------------------------
# TODO : type le paramètre mode avec Literal["read", "write", "append"] au lieu de str.
def describe_mode(mode: str) -> str:
    return f"Mode d'ouverture du fichier : {mode}"
