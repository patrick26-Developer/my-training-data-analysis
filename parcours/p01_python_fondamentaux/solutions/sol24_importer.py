"""Solutions 7.1 — Importer des modules."""

import importlib.util
import math
import random
from collections import Counter
from collections.abc import Callable


def racine(n: float) -> float:
    return math.sqrt(n)


def aire_cercle(rayon: float) -> float:
    return round(math.pi * rayon**2, 2)


def arrondi_superieur(x: float) -> int:
    return math.ceil(x)


def arrondi_inferieur(x: float) -> int:
    return math.floor(x)


def nombres_aleatoires(n: int, minimum: int, maximum: int, graine: int | None = None) -> list[int]:
    if graine is not None:
        random.seed(graine)
    return [random.randint(minimum, maximum) for _ in range(n)]


def mot_le_plus_frequent(mots: list[str]) -> str | None:
    if not mots:
        return None
    return Counter(mots).most_common(1)[0][0]


def existe_module(nom: str) -> bool:
    if not nom:
        return False
    try:
        return importlib.util.find_spec(nom) is not None
    except (ImportError, ValueError):
        return False


def nom_du_module_de(fonction: Callable | object) -> str | None:
    return getattr(fonction, "__module__", None)
