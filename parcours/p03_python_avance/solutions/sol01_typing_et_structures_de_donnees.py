"""Solution de l'exercice 1.1 — Typing avancé & structures de données."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Literal, NamedTuple, Protocol, TypedDict, overload


# ---------------------------------------------------------------------------
# 1. Dataclass immuable avec méthode
# ---------------------------------------------------------------------------
@dataclass(frozen=True, slots=True)
class Point3D:
    x: float
    y: float
    z: float = 0.0

    def distance_to(self, other: Point3D) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


# ---------------------------------------------------------------------------
# 2. NamedTuple
# ---------------------------------------------------------------------------
class RGB(NamedTuple):
    r: int
    g: int
    b: int


# ---------------------------------------------------------------------------
# 3. TypedDict
# ---------------------------------------------------------------------------
class UserPayload(TypedDict):
    id: int
    email: str
    is_active: bool


def make_user_payload(user_id: int, email: str, is_active: bool) -> UserPayload:
    return {"id": user_id, "email": email, "is_active": is_active}


# ---------------------------------------------------------------------------
# 4. Protocol + fonction générique
# ---------------------------------------------------------------------------
class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...


def plus_petit[T: Comparable](a: T, b: T) -> T:
    return a if a < b else b


# ---------------------------------------------------------------------------
# 5. Classe générique Stack[T]
# ---------------------------------------------------------------------------
class Stack[T]:
    """Pile générique LIFO."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items


# ---------------------------------------------------------------------------
# 6. @overload
# ---------------------------------------------------------------------------
@overload
def process(value: int) -> str: ...
@overload
def process(value: str) -> int: ...
def process(value: int | str) -> str | int:
    if isinstance(value, int):
        return str(value)
    return int(value)


# ---------------------------------------------------------------------------
# 7. Literal
# ---------------------------------------------------------------------------
def describe_mode(mode: Literal["read", "write", "append"]) -> str:
    return f"Mode d'ouverture du fichier : {mode}"
