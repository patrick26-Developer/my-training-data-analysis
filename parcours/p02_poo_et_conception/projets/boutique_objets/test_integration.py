"""Tests des échanges disque, migration P01 et parcours console."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

import pytest

from boutique_objets import main, stockage
from boutique_objets.modele import Caisse, Produit, Stock, Vente
from parcours.p01_python_fondamentaux.projets.synthese_boutique import stock as ancien_stock
from parcours.p01_python_fondamentaux.projets.synthese_boutique import stockage as ancien_stockage
from parcours.p01_python_fondamentaux.projets.synthese_boutique import ventes as anciennes_ventes


@pytest.fixture
def caisse():
    magasin = Stock()
    magasin.ajouter(Produit("Riz", 800, 30))
    magasin.ajouter(Produit("Sucre", 500, 3))
    caisse = Caisse(magasin)
    caisse.vendre("Grâce", "Riz", 20, date(2026, 1, 15))
    caisse.vendre("Grâce", "Sucre", 1, date(2026, 1, 15))
    return caisse


def test_aller_retour_et_statistiques(tmp_path, caisse):
    chemin = tmp_path / "sous-dossier" / "boutique.json"
    stockage.sauvegarder(chemin, caisse)
    copie = stockage.charger(chemin)
    assert copie.stock.valeur() == caisse.stock.valeur()
    assert copie.stock.alertes() == ["Sucre"]
    assert copie.journal == caisse.journal
    assert copie.chiffre_affaires() == 15700
    assert copie.total_par_produit() == {"Riz": 15200, "Sucre": 500}
    assert copie.meilleur_client() == "Grâce"
    copie.vendre("Autre", "Riz", 1)
    assert len(copie.journal) == 3
    assert len(caisse.journal) == 2


def test_migration_p01(tmp_path):
    magasin, journal = {}, []
    ancien_stock.ajouter_produit(magasin, ancien_stock.creer_produit("Manioc", 500, 30))
    anciennes_ventes.enregistrer_vente(magasin, journal, "Grâce", "Manioc", 21)
    chemin = tmp_path / "boutique.json"
    ancien_stockage.sauvegarder(chemin, magasin, journal)
    caisse = stockage.charger(chemin)
    assert caisse.stock.trouver("manioc").quantite == 9
    assert [asdict(v) for v in caisse.journal] == journal
    stockage.sauvegarder(chemin, caisse)
    assert json.loads(chemin.read_text(encoding="utf-8"))["version"] == 1


def test_export_csv(tmp_path, caisse):
    chemin = tmp_path / "export" / "ventes.csv"
    assert stockage.exporter_journal_csv(chemin, caisse) == 2
    with chemin.open(encoding="utf-8", newline="") as fichier:
        lignes = list(csv.DictReader(fichier))
    assert lignes[0]["client"] == "Grâce"
    assert float(lignes[0]["total"]) == 15200
    assert lignes[1]["produit"] == "Sucre"


def test_fichier_absent(tmp_path):
    caisse = stockage.charger(tmp_path / "absent.json")
    assert caisse.stock.valeur() == 0
    assert caisse.journal == ()
    assert caisse.meilleur_client() is None
    assert caisse.total_par_produit() == {}


@pytest.mark.parametrize(
    "contenu",
    [
        "{",
        "[]",
        "{}",
        '{"version": 2, "stock": [], "journal": []}',
        '{"version": true, "stock": [], "journal": []}',
        '{"version": 1, "stock": [{"nom": "Riz", "prix": -1, "quantite": 3}], "journal": []}',
        '{"version": 1, "stock": [], "journal": [null]}',
    ],
)
def test_corruption_signalee_sans_ecrasement(tmp_path, contenu):
    chemin = tmp_path / "boutique.json"
    chemin.write_text(contenu, encoding="utf-8")
    with pytest.raises(ValueError, match="Sauvegarde invalide"):
        stockage.charger(chemin)
    assert chemin.read_text(encoding="utf-8") == contenu


def test_doublons_refuses(tmp_path):
    chemin = tmp_path / "boutique.json"
    chemin.write_text(
        json.dumps(
            {
                "version": 1,
                "stock": [
                    {"nom": "riz", "prix": 500, "quantite": 2},
                    {"nom": " RIZ ", "prix": 500, "quantite": 2},
                ],
                "journal": [],
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="dupliqué"):
        stockage.charger(chemin)


def test_echec_remplacement_preserve_sauvegarde(tmp_path, caisse, monkeypatch):
    chemin = tmp_path / "boutique.json"
    chemin.write_text("ancienne sauvegarde", encoding="utf-8")

    def echec(self, cible):
        raise PermissionError("Verrouillé")

    monkeypatch.setattr(Path, "replace", echec)
    with pytest.raises(PermissionError):
        stockage.sauvegarder(chemin, caisse)
    assert chemin.read_text(encoding="utf-8") == "ancienne sauvegarde"
    assert list(tmp_path.glob(".boutique-*.tmp")) == []


@pytest.mark.parametrize("prix", [float("nan"), float("inf"), -float("inf"), True, "500"])
def test_prix_non_numeriques_ou_non_finis(prix):
    with pytest.raises(ValueError):
        Produit("Riz", prix, 2)


@pytest.mark.parametrize(
    "champ,valeur",
    [
        ("total", -1),
        ("total", 501),
        ("remise", -1),
        ("prix", float("nan")),
        ("quantite", True),
        ("date", "2026-02-30"),
        ("client", ""),
    ],
)
def test_validation_vente(champ, valeur):
    donnees = {
        "date": "2026-01-15",
        "client": "Grâce",
        "produit": "Riz",
        "quantite": 1,
        "prix": 500,
        "remise": 0,
        "total": 500,
    }
    donnees[champ] = valeur
    with pytest.raises(ValueError):
        Vente(**donnees)


def test_journal_charge_rejette_dict():
    with pytest.raises(ValueError):
        Caisse(Stock(), journal=[{}])


def test_session_console(tmp_path, monkeypatch, capsys):
    chemin = tmp_path / "boutique.json"
    reponses = iter(
        [
            "1",
            "Riz",
            "erreur",
            "800",
            "3",
            "2",
            "Grâce",
            "Inconnu",
            "1",
            "2",
            "Grâce",
            "Riz",
            "4",
            "2",
            "Grâce",
            "Riz",
            "2",
            "3",
            "4",
            "5",
            "6",
            "?",
            "q",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    assert main.menu(chemin) == 0
    sortie = capsys.readouterr().out
    for texte in [
        "nombre valide",
        "Produit inconnu",
        "Stock insuffisant",
        "1600.00 FCFA",
        "1 vente(s) exportée(s)",
        "Choix inconnu",
        "Au revoir",
    ]:
        assert texte in sortie
    caisse = stockage.charger(chemin)
    assert caisse.stock.trouver("Riz").quantite == 1
    assert len(caisse.journal) == 1
    assert chemin.with_suffix(".csv").exists()


def test_console_necrase_pas_fichier_invalide(tmp_path, capsys):
    chemin = tmp_path / "boutique.json"
    chemin.write_text("{", encoding="utf-8")
    assert main.menu(chemin) == 1
    assert "Chargement impossible" in capsys.readouterr().out
    assert chemin.read_text(encoding="utf-8") == "{"


def test_console_echec_sauvegarde_permet_reessai(tmp_path, monkeypatch, capsys):
    reponses = iter(["q", "q"])
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    sauvegarder = main.sauvegarder
    appels = []

    def temporairement_indisponible(chemin, caisse):
        appels.append(chemin)
        if len(appels) == 1:
            raise PermissionError("Verrouillé")
        sauvegarder(chemin, caisse)

    monkeypatch.setattr(main, "sauvegarder", temporairement_indisponible)
    assert main.menu(tmp_path / "boutique.json") == 0
    assert len(appels) == 2
    assert "Opération refusée" in capsys.readouterr().out
