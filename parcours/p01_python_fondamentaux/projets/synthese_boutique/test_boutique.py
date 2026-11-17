"""Tests du projet de synthèse (inspire-toi de ce fichier pour tester TON projet)."""

import csv
import doctest
from datetime import date

import pytest

from synthese_boutique import affichage, stock, stockage, ventes


@pytest.fixture
def boutique():
    magasin: dict = {}
    stock.ajouter_produit(magasin, stock.creer_produit("manioc", 500, 100))
    stock.ajouter_produit(magasin, stock.creer_produit("Riz", 800, 3))
    return magasin


# ------------------------------------------------------------------ stock
def test_creer_produit_normalise_le_nom():
    assert stock.creer_produit("  sac  de riz ", 800, 3) == {
        "nom": "Sac De Riz",
        "prix": 800.0,
        "quantite": 3,
    }


@pytest.mark.parametrize(
    ("nom", "prix", "quantite"),
    [("", 100, 1), ("  ", 100, 1), ("x", 0, 1), ("x", -5, 1), ("x", 5, -1)],
)
def test_creer_produit_refuse_les_donnees_invalides(nom, prix, quantite):
    with pytest.raises(ValueError):
        stock.creer_produit(nom, prix, quantite)


def test_ajouter_un_produit_existant_cumule(boutique):
    stock.ajouter_produit(boutique, stock.creer_produit("MANIOC", 550, 20))
    assert boutique["manioc"]["quantite"] == 120
    assert boutique["manioc"]["prix"] == 550.0


def test_retirer_du_stock(boutique):
    stock.retirer_du_stock(boutique, "Manioc", 30)
    assert boutique["manioc"]["quantite"] == 70


def test_retirer_erreurs(boutique):
    with pytest.raises(stock.ProduitInconnuError):
        stock.retirer_du_stock(boutique, "Sucre", 1)
    with pytest.raises(stock.StockInsuffisantError):
        stock.retirer_du_stock(boutique, "Riz", 4)
    with pytest.raises(ValueError):
        stock.retirer_du_stock(boutique, "Riz", 0)
    assert boutique["riz"]["quantite"] == 3  # rien n'a été retiré


def test_valeur_et_alertes(boutique):
    assert stock.valeur_du_stock(boutique) == 100 * 500 + 3 * 800
    assert stock.produits_en_alerte(boutique, seuil=5) == ["Riz"]


# ------------------------------------------------------------------ ventes
def test_enregistrer_vente_sans_remise(boutique):
    journal: list[dict] = []
    vente = ventes.enregistrer_vente(
        boutique, journal, " grâce ", "riz", 2, jour=date(2026, 11, 16)
    )
    assert vente == {
        "date": "2026-11-16",
        "client": "Grâce",
        "produit": "Riz",
        "quantite": 2,
        "prix": 800.0,
        "remise": 0.0,
        "total": 1600.0,
    }
    assert journal == [vente]
    assert boutique["riz"]["quantite"] == 1


def test_remise_au_dessus_du_seuil(boutique):
    journal: list[dict] = []
    vente = ventes.enregistrer_vente(boutique, journal, "Jean", "Manioc", 30)  # 15 000 FCFA
    assert vente["remise"] == 750.0
    assert vente["total"] == 14250.0


def test_vente_impossible_ne_modifie_rien(boutique):
    journal: list[dict] = []
    with pytest.raises(stock.StockInsuffisantError):
        ventes.enregistrer_vente(boutique, journal, "Jean", "Riz", 10)
    assert journal == []
    assert boutique["riz"]["quantite"] == 3


def test_statistiques(boutique):
    journal: list[dict] = []
    ventes.enregistrer_vente(boutique, journal, "Jean", "Manioc", 10)  # 5 000
    ventes.enregistrer_vente(boutique, journal, "Marie", "Riz", 3)  # 2 400
    ventes.enregistrer_vente(boutique, journal, "Jean", "Manioc", 2)  # 1 000
    assert ventes.chiffre_d_affaires(journal) == 8400
    assert ventes.total_par_produit(journal) == {"Manioc": 6000, "Riz": 2400}
    assert ventes.meilleur_client(journal) == "Jean"
    assert ventes.meilleur_client([]) is None


def test_doctests_du_module_ventes():
    resultat = doctest.testmod(ventes)
    assert resultat.failed == 0
    assert resultat.attempted >= 2


# ------------------------------------------------------------------ stockage
def test_sauvegarde_et_rechargement(tmp_path, boutique):
    journal: list[dict] = []
    ventes.enregistrer_vente(boutique, journal, "Grâce", "Manioc", 5)
    chemin = tmp_path / "donnees" / "boutique.json"
    stockage.sauvegarder(chemin, boutique, journal)
    stock_recharge, journal_recharge = stockage.charger(chemin)
    assert stock_recharge == boutique
    assert journal_recharge == journal


def test_chargement_fichier_absent_ou_corrompu(tmp_path):
    assert stockage.charger(tmp_path / "absent.json") == ({}, [])
    corrompu = tmp_path / "corrompu.json"
    corrompu.write_text("{pas du json", encoding="utf-8")
    assert stockage.charger(corrompu) == ({}, [])


def test_export_csv(tmp_path, boutique):
    journal: list[dict] = []
    ventes.enregistrer_vente(boutique, journal, "Grâce", "Manioc", 5)
    chemin = tmp_path / "ventes.csv"
    assert stockage.exporter_journal_csv(chemin, journal) == 1
    with open(chemin, newline="", encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
    assert lignes[0]["client"] == "Grâce"
    assert float(lignes[0]["total"]) == 2500.0


# ------------------------------------------------------------------ affichage
def test_formater_recu(boutique):
    journal: list[dict] = []
    vente = ventes.enregistrer_vente(
        boutique, journal, "Grâce", "Manioc", 5, jour=date(2026, 11, 16)
    )
    recu = affichage.formater_recu(vente)
    assert "Grâce" in recu
    assert "2026-11-16" in recu
    assert "2,500" in recu
    assert all(len(ligne) <= 41 for ligne in recu.splitlines())


def test_formater_stock(boutique):
    texte = affichage.formater_stock(boutique)
    assert texte.splitlines()[1].startswith("Manioc")
    assert affichage.formater_stock({}) == "Stock vide."
