"""Solutions 5.4 — Les fonctions sont des valeurs."""

from collections.abc import Callable
from typing import Any


def appliquer(fonction: Callable[[Any], Any], valeurs: list) -> list:
    return [fonction(v) for v in valeurs]


def trier_par_prix(produits: list[tuple[str, float]]) -> list[tuple[str, float]]:
    return sorted(produits, key=lambda p: p[1])


def meilleur_eleve(eleves: list[dict]) -> str:
    return max(eleves, key=lambda e: e["note"])["nom"]


def trier_par_longueur(mots: list[str]) -> list[str]:
    return sorted(mots, key=lambda m: (len(m), m))


def multiplicateur(facteur: float) -> Callable[[float], float]:
    def multiplier(x: float) -> float:
        return x * facteur  # fermeture : facteur est mémorisé

    return multiplier


def calculer(a: float, operation: str, b: float) -> float | None:
    operations: dict[str, Callable[[float, float], float]] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if operation not in operations:
        return None
    if operation == "/" and b == 0:
        return None
    return operations[operation](a, b)


def filtrer(valeurs: list, condition: Callable[[Any], bool]) -> list:
    return [v for v in valeurs if condition(v)]


def composer(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def h(x: Any) -> Any:
        return f(g(x))

    return h
