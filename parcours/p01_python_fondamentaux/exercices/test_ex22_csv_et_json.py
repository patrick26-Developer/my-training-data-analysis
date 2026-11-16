"""Tests de l'exercice 6.3. Ne modifie pas ce fichier."""

import json

from ex22_csv_et_json import (
    ajouter_produit_json,
    charger_json,
    compter_par_ville,
    csv_vers_json,
    ecrire_stock_csv,
    lire_stock_csv,
    sauvegarder_json,
    valeur_totale_csv,
)

PRODUITS = [
    {"nom": "Manioc", "prix": 500, "quantite": 12},
    {"nom": "Café, noir", "prix": 800, "quantite": 3},
]


def test_ecrire_stock_csv(tmp_path):
    chemin = tmp_path / "stock.csv"
    ecrire_stock_csv(chemin, PRODUITS)
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    assert lignes[0] == "nom,prix,quantite"
    assert lignes[1] == "Manioc,500,12"
    assert lignes[2] == '"Café, noir",800,3'  # la virgule est protégée par le module csv


def test_lire_stock_csv(tmp_path):
    chemin = tmp_path / "stock.csv"
    ecrire_stock_csv(chemin, PRODUITS)
    assert lire_stock_csv(chemin) == PRODUITS


def test_valeur_totale_csv(tmp_path):
    chemin = tmp_path / "stock.csv"
    ecrire_stock_csv(chemin, PRODUITS)
    assert valeur_totale_csv(chemin) == 8400


def test_sauvegarder_json(tmp_path):
    chemin = tmp_path / "d.json"
    sauvegarder_json(chemin, {"nom": "Grâce", "villes": ["Brazzaville"]})
    texte = chemin.read_text(encoding="utf-8")
    assert "Grâce" in texte  # accents conservés
    assert "\n" in texte  # indenté
    assert json.loads(texte) == {"nom": "Grâce", "villes": ["Brazzaville"]}


def test_charger_json(tmp_path):
    chemin = tmp_path / "d.json"
    assert charger_json(chemin, defaut=[]) == []
    chemin.write_text("pas du json", encoding="utf-8")
    assert charger_json(chemin, defaut={"x": 1}) == {"x": 1}
    chemin.write_text('{"a": 1}', encoding="utf-8")
    assert charger_json(chemin) == {"a": 1}


def test_compter_par_ville(tmp_path):
    chemin = tmp_path / "gens.csv"
    chemin.write_text(
        "nom,ville\nJean,Brazzaville\nMarie,Pointe-Noire\nPaul,Brazzaville\n", encoding="utf-8"
    )
    assert compter_par_ville(chemin) == {"Brazzaville": 2, "Pointe-Noire": 1}


def test_csv_vers_json(tmp_path):
    source = tmp_path / "a.csv"
    destination = tmp_path / "a.json"
    source.write_text("nom,age\nJean,30\nMarie,25\n", encoding="utf-8")
    csv_vers_json(source, destination)
    assert json.loads(destination.read_text(encoding="utf-8")) == [
        {"nom": "Jean", "age": "30"},
        {"nom": "Marie", "age": "25"},
    ]


def test_ajouter_produit_json(tmp_path):
    chemin = tmp_path / "p.json"
    assert ajouter_produit_json(chemin, {"nom": "Riz"}) == 1
    assert ajouter_produit_json(chemin, {"nom": "Sel"}) == 2
    assert json.loads(chemin.read_text(encoding="utf-8")) == [{"nom": "Riz"}, {"nom": "Sel"}]
