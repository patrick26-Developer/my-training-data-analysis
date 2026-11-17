"""Configuration pytest commune au parcours P01.

- Force le moteur graphique « Agg » de matplotlib (sans fenêtre) pour les tests.
- Ferme toutes les figures après chaque test.
"""

import os

os.environ.setdefault("MPLBACKEND", "Agg")

import pytest


@pytest.fixture(autouse=True)
def _fermer_les_figures():
    yield
    try:
        import matplotlib.pyplot as plt

        plt.close("all")
    except ImportError:  # matplotlib non installé : rien à fermer
        pass
