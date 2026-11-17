"""Solutions 9.2 — matplotlib."""

from os import PathLike
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def courbe_ventes(mois: list[float], ventes: list[float]) -> Figure:
    fig, ax = plt.subplots()
    ax.plot(mois, ventes, marker="o")  # lève ValueError si les tailles diffèrent
    ax.set_title("Ventes")
    ax.set_xlabel("Mois")
    ax.set_ylabel("Ventes (FCFA)")
    return fig


def barres_stock(produits: list[str], quantites: list[float]) -> Figure:
    fig, ax = plt.subplots()
    ax.bar(produits, quantites)
    ax.set_title("Stock par produit")
    ax.set_ylabel("Quantité")
    return fig


def histogramme_notes(notes: list[float], classes: int = 5) -> Figure:
    fig, ax = plt.subplots()
    ax.hist(notes, bins=classes, edgecolor="black")
    ax.set_title("Répartition des notes")
    ax.set_xlabel("Note")
    return fig


def nuage_points(x: list[float], y: list[float]) -> Figure:
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel("Heures")
    ax.set_ylabel("Note")
    return fig


def camembert(parts: dict[str, float]) -> Figure:
    fig, ax = plt.subplots()
    ax.pie(list(parts.values()), labels=list(parts.keys()))
    ax.set_title("Répartition")
    return fig


def deux_courbes(x: list[float], y1: list[float], y2: list[float]) -> Figure:
    fig, ax = plt.subplots()
    ax.plot(x, y1, label="A")
    ax.plot(x, y2, label="B")
    ax.legend()
    ax.set_title("Comparaison")
    return fig


def figure_double(mois: list[float], ventes: list[float]) -> Figure:
    fig, (gauche, droite) = plt.subplots(1, 2, figsize=(10, 4))
    gauche.plot(mois, ventes)
    droite.bar(mois, ventes)
    fig.tight_layout()
    return fig


def enregistrer(fig: Figure, chemin: str | PathLike[str]) -> bool:
    fig.savefig(chemin, dpi=100)
    return Path(chemin).exists()
