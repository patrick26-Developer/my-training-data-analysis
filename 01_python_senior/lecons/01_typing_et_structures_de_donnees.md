# 1.1 — Typing avancé & structures de données

## Pourquoi typer son code Python

Python reste dynamiquement typé à l'exécution, mais le typage statique (vérifié par `mypy`)
est un standard professionnel : il documente l'intention, détecte des bugs avant l'exécution,
et rend le code navigable par les IDE. En entreprise, un code senior est **typé, vérifié en CI,
et `mypy --strict` passe sans erreur**.

Dans ce projet, `pyproject.toml` configure déjà `mypy` en mode `strict`.

---

## 1. `dataclasses` — structures de données avec comportement

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point3D:
    x: float
    y: float
    z: float = 0.0

    def distance_to(self, other: "Point3D") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
```

- `frozen=True` → immuable (utile pour la sécurité des threads, le hachage, éviter les bugs d'état partagé).
- `slots=True` → pas de `__dict__`, moins de mémoire, accès attribut plus rapide, erreur si on
  tente d'ajouter un attribut non déclaré.
- `field(default_factory=list)` → évite le piège classique du mutable par défaut partagé entre instances.
- `__post_init__` → validation après construction (une dataclass n'a pas de constructeur custom simple sinon).

**Quand l'utiliser** : dès qu'une classe sert principalement à porter des données, avec ou sans
quelques méthodes utilitaires.

## 2. `NamedTuple` vs `dataclass` vs `TypedDict`

| Besoin | Outil |
|---|---|
| Objet immuable, léger, comportement comme un tuple (déballage, index) | `NamedTuple` |
| Objet avec méthodes, mutabilité optionnelle, héritage | `dataclass` |
| Représenter la forme d'un `dict` existant (ex. JSON reçu d'une API) | `TypedDict` |

```python
from typing import NamedTuple, TypedDict

class RGB(NamedTuple):
    r: int
    g: int
    b: int

class UserPayload(TypedDict):
    id: int
    email: str
    is_active: bool
```

`TypedDict` ne crée **pas** de nouvelle classe à l'exécution — c'est un `dict` normal, la structure
n'existe que pour `mypy`. Utile pour typer des données externes (API, JSON) sans réécrire toute la
donnée sous forme d'objets.

## 3. `Protocol` — le typage structurel (duck typing typé)

```python
from typing import Protocol

class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...

def plus_petit[T: Comparable](a: T, b: T) -> T:
    return a if a < b else b
```

Un `Protocol` définit une **interface implicite** : n'importe quel objet qui possède les bonnes
méthodes/attributs est accepté, sans héritage explicite requis. C'est l'équivalent typé du
"duck typing" pythonique (`if it walks like a duck and quacks like a duck...`).

## 4. Génériques (`Generic`, `TypeVar`, syntaxe Python 3.12+)

Depuis Python 3.12, la syntaxe générique est intégrée au langage (plus besoin de `TypeVar` explicite
dans les cas simples) :

```python
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return not self._items
```

Un `Stack[int]` et un `Stack[str]` sont deux usages du même code, mais `mypy` vérifie qu'on ne
mélange pas les types à l'intérieur.

## 5. `Literal`, `Final`, `@overload`

```python
from typing import Literal, Final, overload

MAX_RETRIES: Final = 3

def set_mode(mode: Literal["read", "write", "append"]) -> None: ...

@overload
def process(value: int) -> str: ...
@overload
def process(value: str) -> int: ...
def process(value: int | str) -> str | int:
    if isinstance(value, int):
        return str(value)
    return int(value)
```

- `Literal` restreint les valeurs acceptées à un ensemble fini (utile pour des modes/statuts).
- `Final` indique qu'une variable/constante ne doit pas être réassignée.
- `@overload` documente précisément, pour `mypy`, plusieurs signatures possibles d'une même fonction
  selon le type d'entrée — la vraie implémentation vient après, sans décorateur.

---

## À retenir pour un niveau senior

- Le typage n'est pas de la bureaucratie : il remplace une partie de la documentation et de la
  validation manuelle.
- Choisir la structure la plus **simple** qui documente correctement l'intention
  (`NamedTuple`/`TypedDict` avant `dataclass`, `dataclass` avant classe classique).
- `Protocol` > héritage quand on veut juste vérifier une capacité (méthode/attribut), pas une relation
  "est un".
- `frozen=True` et `slots=True` doivent être le réflexe par défaut sur une dataclass, sauf besoin
  contraire explicite.
