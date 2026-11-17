"""Solutions 9.3 — Représenter une fonction mathématique."""

import math
from collections.abc import Callable

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

Fonction = Callable[[float], float]


def linspace(debut: float, fin: float, n: int) -> list[float]:
    if n == 1:
        return [debut]
    pas = (fin - debut) / (n - 1)
    return [debut + i * pas for i in range(n)]


def table_de_valeurs(f: Fonction, debut: float, fin: float, n: int) -> list[tuple[float, float]]:
    return [(x, f(x)) for x in linspace(debut, fin, n)]


def tracer_fonction(f: Fonction, debut: float, fin: float, titre: str, n: int = 100) -> Figure:
    xs = linspace(debut, fin, n)
    fig, ax = plt.subplots()
    ax.plot(xs, [f(x) for x in xs])
    ax.set_title(titre)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    return fig


def zero_par_dichotomie(f: Fonction, a: float, b: float, precision: float = 1e-9) -> float:
    if f(a) * f(b) > 0:
        raise ValueError("Zéro non encadré")
    while b - a > precision:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2


def integrale(f: Fonction, a: float, b: float, n: int = 1000) -> float:
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def derivee(f: Fonction, x: float, h: float = 1e-6) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def minimum(f: Fonction, debut: float, fin: float, n: int = 1000) -> tuple[float, float]:
    return min(table_de_valeurs(f, debut, fin, n), key=lambda couple: couple[1])


def point_mort(prix: float, cout_variable: float, cout_fixe: float) -> int | None:
    if prix <= cout_variable:
        return None
    marge = prix - cout_variable  # gain par unité vendue
    return math.ceil(cout_fixe / marge)


def tracer_cercle(rayon: float) -> Figure:
    angles = linspace(0, 2 * math.pi, 100)
    fig, ax = plt.subplots()
    ax.plot([rayon * math.cos(t) for t in angles], [rayon * math.sin(t) for t in angles])
    ax.set_aspect("equal")
    return fig


def comparer_fonctions(
    fonctions: dict[str, Fonction], debut: float, fin: float, n: int = 100
) -> Figure:
    xs = linspace(debut, fin, n)
    fig, ax = plt.subplots()
    for nom, f in fonctions.items():
        ax.plot(xs, [f(x) for x in xs], label=nom)
    ax.legend()
    return fig
