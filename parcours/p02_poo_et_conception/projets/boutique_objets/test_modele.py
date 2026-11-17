"""Comparaisons métier P01/P02 et garanties propres aux objets."""

from dataclasses import FrozenInstanceError, asdict
from datetime import date

import pytest

from boutique_objets.modele import Caisse, Produit, RemiseSeuil, SansRemise, Stock
from parcours.p01_python_fondamentaux.projets.synthese_boutique import stock, ventes


@pytest.mark.parametrize("quantite", [1, 20, 21, 30])
def test_parite_avec_p01(quantite):
    ancien = {}
    stock.ajouter_produit(ancien, stock.creer_produit("  sac  de riz ", 500, 50))
    nouveau = Stock()
    nouveau.ajouter(Produit("  sac  de riz ", 500, 50))
    journal = []
    jour = date(2026, 1, 15)
    attendu = ventes.enregistrer_vente(
        ancien, journal, "  mama  nzoni ", "sac de riz", quantite, jour
    )
    caisse = Caisse(nouveau)
    obtenu = caisse.vendre("  mama  nzoni ", "sac de riz", quantite, jour)
    assert asdict(obtenu) == attendu
    assert nouveau.valeur() == stock.valeur_du_stock(ancien)
    assert nouveau.alertes() == stock.produits_en_alerte(ancien)
    assert caisse.chiffre_affaires() == ventes.chiffre_d_affaires(journal)


def test_cumul_copie_et_stocks_independants():
    a, b = Stock(), Stock()
    produit = Produit("Riz", 500, 3)
    a.ajouter(produit)
    produit.retirer(1)
    a.ajouter(Produit("  RIZ ", 600, 2))
    assert a.trouver("riz").quantite == 5
    assert a.trouver("riz").prix == 600
    assert b.valeur() == 0
    assert a.alertes() == ["Riz"]
    with pytest.raises(KeyError):
        b.trouver("riz")


@pytest.mark.parametrize("quantite", [0, -1, 4, 1.5, True])
def test_vente_refusee_sans_mutation(quantite):
    magasin = Stock()
    magasin.ajouter(Produit("Riz", 500, 3))
    caisse = Caisse(magasin)
    with pytest.raises(ValueError):
        caisse.vendre("Client", "Riz", quantite)
    assert magasin.trouver("Riz").quantite == 3
    assert caisse.journal == ()


def test_instantane_et_journal_proteges():
    magasin = Stock()
    magasin.ajouter(Produit("Riz", 500, 3))
    caisse = Caisse(magasin, SansRemise())
    vente = caisse.vendre("", "Riz", 1)
    magasin.trouver("Riz").prix = 900
    assert vente.prix == 500
    assert vente.client == "Client"
    with pytest.raises(FrozenInstanceError):
        vente.total = 0
    assert caisse.journal == (vente,)


@pytest.mark.parametrize("resultat", [-1, 1001, None])
def test_strategie_invalide_sans_mutation(resultat):
    class Invalide:
        def calculer(self, montant):
            return resultat

    magasin = Stock()
    magasin.ajouter(Produit("Riz", 500, 3))
    caisse = Caisse(magasin, Invalide())
    with pytest.raises((ValueError, TypeError)):
        caisse.vendre("Client", "Riz", 2)
    assert magasin.trouver("Riz").quantite == 3
    assert caisse.journal == ()


def test_politique_qui_echoue():
    class Echec:
        def calculer(self, montant):
            raise RuntimeError("Service indisponible")

    magasin = Stock()
    magasin.ajouter(Produit("Riz", 500, 3))
    caisse = Caisse(magasin, Echec())
    with pytest.raises(RuntimeError):
        caisse.vendre("Client", "Riz", 1)
    assert magasin.trouver("Riz").quantite == 3
    assert caisse.journal == ()


@pytest.mark.parametrize(
    ("nom", "prix", "quantite"), [("", 500, 1), ("Riz", 0, 1), ("Riz", 500, -1), ("Riz", 500, 1.5)]
)
def test_produit_invalide(nom, prix, quantite):
    with pytest.raises(ValueError):
        Produit(nom, prix, quantite)


def test_prix_invalide_conserve_ancien():
    produit = Produit("Riz", 500, 3)
    with pytest.raises(ValueError):
        produit.prix = -5
    assert produit.prix == 500
    assert RemiseSeuil().calculer(10000) == 0
