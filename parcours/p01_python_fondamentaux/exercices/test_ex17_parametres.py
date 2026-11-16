"""Tests de l'exercice 5.2. Ne modifie pas ce fichier."""

import pytest
from ex17_parametres import (
    additionner,
    ajouter_produit,
    fiche,
    formater_prix,
    moyenne,
    plus_grand,
    prix_ttc,
    remise,
)


def test_prix_ttc():
    assert prix_ttc(1000) == pytest.approx(1180.0)
    assert prix_ttc(1000, 5) == pytest.approx(1050.0)
    assert prix_ttc(1000, taux=0) == pytest.approx(1000.0)


def test_remise():
    assert remise(1000) == pytest.approx(1000.0)
    assert remise(1000, 10) == pytest.approx(900.0)
    assert remise(prix=200, pourcentage=50) == pytest.approx(100.0)


def test_additionner():
    assert additionner() == 0
    assert additionner(1, 2) == 3
    assert additionner(1, 2, 3, 4, 5) == 15


def test_moyenne():
    assert moyenne(10, 20) == pytest.approx(15.0)
    assert moyenne() == 0.0
    assert moyenne(7) == pytest.approx(7.0)


def test_plus_grand():
    assert plus_grand(3, 9, 4) == 9
    assert plus_grand(5) == 5
    assert plus_grand(-1, -5) == -1


def test_fiche():
    assert fiche(nom="Grâce", age=25) == "nom=Grâce | age=25"
    assert fiche() == ""


def test_formater_prix():
    assert formater_prix(1234567) == "1,234,567 FCFA"
    assert formater_prix(1234.5, devise="EUR", decimales=2) == "1,234.50 EUR"
    with pytest.raises(TypeError):
        formater_prix(1000, "EUR")  # type: ignore[misc]


def test_ajouter_produit_pas_de_defaut_partage():
    assert ajouter_produit("Riz") == ["Riz"]
    assert ajouter_produit("Sel") == ["Sel"]  # nouvelle liste à chaque appel
    panier = ["Riz"]
    assert ajouter_produit("Sel", panier) is panier
    assert panier == ["Riz", "Sel"]
