"""Tests de l'exercice 9.2. Ne modifie pas ce fichier."""

import pytest
from ex33_matplotlib import (
    barres_stock,
    camembert,
    courbe_ventes,
    deux_courbes,
    enregistrer,
    figure_double,
    histogramme_notes,
    nuage_points,
)

MOIS = [1, 2, 3, 4]
VENTES = [120, 150, 130, 180]


def test_courbe_ventes():
    fig = courbe_ventes(MOIS, VENTES)
    ax = fig.axes[0]
    assert ax.get_title() == "Ventes"
    assert ax.get_xlabel() == "Mois"
    assert ax.get_ylabel() == "Ventes (FCFA)"
    ligne = ax.lines[0]
    assert list(ligne.get_xdata()) == MOIS
    assert list(ligne.get_ydata()) == VENTES
    assert ligne.get_marker() == "o"


def test_barres_stock():
    fig = barres_stock(["Manioc", "Riz", "Sel"], [40, 25, 60])
    ax = fig.axes[0]
    assert ax.get_title() == "Stock par produit"
    assert ax.get_ylabel() == "Quantité"
    assert [r.get_height() for r in ax.patches] == [40, 25, 60]
    assert [t.get_text() for t in ax.get_xticklabels()] == ["Manioc", "Riz", "Sel"]


def test_histogramme_notes():
    notes = [8, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 18]
    fig = histogramme_notes(notes, classes=4)
    ax = fig.axes[0]
    assert ax.get_title() == "Répartition des notes"
    assert ax.get_xlabel() == "Note"
    assert len(ax.patches) == 4
    assert sum(r.get_height() for r in ax.patches) == len(notes)


def test_nuage_points():
    fig = nuage_points([1, 2, 3], [8, 12, 15])
    ax = fig.axes[0]
    assert ax.get_xlabel() == "Heures"
    assert ax.get_ylabel() == "Note"
    assert len(ax.collections[0].get_offsets()) == 3


def test_camembert():
    fig = camembert({"Manioc": 50, "Riz": 30, "Autres": 20})
    ax = fig.axes[0]
    assert ax.get_title() == "Répartition"
    assert [t.get_text() for t in ax.texts[:3]] == ["Manioc", "Riz", "Autres"]
    assert len(ax.patches) == 3


def test_deux_courbes():
    fig = deux_courbes([1, 2, 3], [1, 2, 3], [3, 2, 1])
    ax = fig.axes[0]
    assert ax.get_title() == "Comparaison"
    assert len(ax.lines) == 2
    assert [t.get_text() for t in ax.get_legend().get_texts()] == ["A", "B"]


def test_figure_double():
    fig = figure_double(MOIS, VENTES)
    assert len(fig.axes) == 2
    assert len(fig.axes[0].lines) == 1
    assert len(fig.axes[1].patches) == len(MOIS)


def test_enregistrer(tmp_path):
    fig = courbe_ventes(MOIS, VENTES)
    chemin = tmp_path / "ventes.png"
    assert enregistrer(fig, chemin) is True
    assert chemin.stat().st_size > 0


def test_longueurs_incoherentes():
    with pytest.raises(ValueError):
        courbe_ventes([1, 2, 3], [1, 2])
