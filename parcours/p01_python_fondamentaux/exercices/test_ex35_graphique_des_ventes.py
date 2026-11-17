"""Tests de l'exercice 9.4. Ne modifie pas ce fichier."""

import pytest
from ex35_graphique_des_ventes import (
    chiffre_affaires_par_mois,
    chiffre_affaires_par_produit,
    droite_de_tendance,
    evolution,
    lire_ventes,
    meilleur_produit,
    prevision,
    tableau_de_bord,
)

CSV = """mois,produit,quantite,prix_unitaire
2026-02,Riz,10,800
2026-01,Manioc,100,500
2026-01,Riz,5,800
2026-02,Manioc,60,500
"""

VENTES = [
    {"mois": "2026-02", "produit": "Riz", "quantite": 10, "prix": 800.0},
    {"mois": "2026-01", "produit": "Manioc", "quantite": 100, "prix": 500.0},
    {"mois": "2026-01", "produit": "Riz", "quantite": 5, "prix": 800.0},
    {"mois": "2026-02", "produit": "Manioc", "quantite": 60, "prix": 500.0},
]


def test_lire_ventes(tmp_path):
    chemin = tmp_path / "ventes.csv"
    chemin.write_text(CSV, encoding="utf-8")
    assert lire_ventes(chemin) == VENTES


def test_chiffre_affaires_par_mois():
    resultat = chiffre_affaires_par_mois(VENTES)
    assert resultat == {"2026-01": 54000.0, "2026-02": 38000.0}
    assert list(resultat) == ["2026-01", "2026-02"]  # trié


def test_chiffre_affaires_par_produit():
    assert chiffre_affaires_par_produit(VENTES) == {"Riz": 12000.0, "Manioc": 80000.0}


def test_meilleur_produit():
    assert meilleur_produit(VENTES) == "Manioc"


def test_evolution():
    assert evolution({"01": 100, "02": 150, "03": 120}) == [50.0, -20.0]
    assert evolution({"01": 0, "02": 50, "03": 100}) == [100.0]
    assert evolution({"01": 5}) == []


def test_droite_de_tendance():
    assert droite_de_tendance([1, 3, 5, 7]) == (2.0, 1.0)
    a, b = droite_de_tendance([10, 10, 10])
    assert (a, b) == (0.0, 10.0)


def test_prevision():
    assert prevision([1, 3, 5, 7]) == 9.0
    assert prevision([1, 3, 5, 7], mois_suivants=3) == 13.0


def test_tableau_de_bord():
    fig = tableau_de_bord(VENTES)
    assert len(fig.axes) == 2
    assert fig.axes[0].get_title() == "Chiffre d'affaires par mois"
    assert fig.axes[1].get_title() == "Chiffre d'affaires par produit"
    assert fig._suptitle.get_text() == "Boutique Mama Nzoni"
    assert list(fig.axes[0].lines[0].get_ydata()) == pytest.approx([54000.0, 38000.0])


def test_donnees_du_projet():
    from pathlib import Path

    chemin = Path(__file__).resolve().parents[1] / "projets" / "donnees" / "ventes.csv"
    ventes = lire_ventes(chemin)
    assert len(ventes) == 18
    assert meilleur_produit(ventes) == "Manioc"
