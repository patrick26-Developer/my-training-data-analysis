"""Partie code : 20 tests indépendants, chacun vaut 3 points."""

from dataclasses import FrozenInstanceError, is_dataclass

import pytest
from sol07_examen_final import Commande, LigneTicket, Livraison, LivraisonMoto, Portefeuille


# Problème 1 : 15 points.
def test_p1_initialisation():
    assert Portefeuille(1000).solde == 1000
    assert Portefeuille(0).solde == 0


def test_p1_debit():
    p = Portefeuille(1000)
    p.debiter(300)
    p.debiter(700)
    assert p.solde == 0


def test_p1_solde_negatif():
    with pytest.raises(ValueError):
        Portefeuille(-1)


def test_p1_refus_sans_mutation():
    p = Portefeuille(100)
    for montant in (0, -1, 101):
        with pytest.raises(ValueError):
            p.debiter(montant)
        assert p.solde == 100


def test_p1_lecture_seule_et_independance():
    a, b = Portefeuille(100), Portefeuille(100)
    a.debiter(50)
    assert b.solde == 100
    with pytest.raises(AttributeError):
        a.solde = -100


# Problème 2 : 15 points.
def test_p2_dataclass():
    assert is_dataclass(LigneTicket)
    assert LigneTicket("Riz", 500, 2).produit == "Riz"


def test_p2_egalite():
    assert LigneTicket("Riz", 500, 2) == LigneTicket("Riz", 500, 2)
    assert LigneTicket("Riz", 500, 2) != LigneTicket("Riz", 600, 2)


def test_p2_total():
    assert LigneTicket("Riz", 500, 2).total() == 1000
    assert LigneTicket("Sucre", 700, 3).total() == 2100


def test_p2_gele():
    with pytest.raises(FrozenInstanceError):
        LigneTicket("Riz", 500, 2).prix = 600


def test_p2_representation():
    texte = repr(LigneTicket("Riz", 500, 2))
    assert "LigneTicket" in texte and "Riz" in texte


# Problème 3 : 15 points.
def test_p3_gratuit():
    assert Livraison().frais(0) == 0
    assert Livraison().frais(20) == 0


def test_p3_heritage():
    assert issubclass(LivraisonMoto, Livraison)


def test_p3_moto_zero():
    assert LivraisonMoto().frais(0) == 500


def test_p3_moto_distance():
    assert LivraisonMoto().frais(7) == 1200


def test_p3_polymorphisme():
    assert [p.frais(2) for p in (Livraison(), LivraisonMoto())] == [0, 700]


# Problème 4 : 15 points.
def test_p4_gratuit():
    assert Commande(Livraison()).total(1000, 3) == 1000


def test_p4_moto():
    assert Commande(LivraisonMoto()).total(1000, 3) == 1800


def test_p4_injection():
    class Transport:
        def frais(self, distance):
            return 42 * distance

    assert Commande(Transport()).total(1000, 2) == 1084


def test_p4_appel_avec_distance():
    distances = []

    class Espion:
        def frais(self, distance):
            distances.append(distance)
            return 0

    assert Commande(Espion()).total(500, 4) == 500
    assert distances == [4]


def test_p4_frais_negatifs():
    class Invalide:
        def frais(self, distance):
            return -1

    with pytest.raises(ValueError):
        Commande(Invalide()).total(1000, 1)
