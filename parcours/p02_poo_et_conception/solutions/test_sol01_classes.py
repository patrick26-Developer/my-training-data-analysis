from sol01_classes import Produit


def test_instances_independantes():
    a, b = Produit("Riz", 800, 3), Produit("Sucre", 500, 2)
    a.quantite = 1
    assert b.quantite == 2
    assert a.nom == "Riz"


def test_valeur_et_etiquette():
    p = Produit("Riz", 800, 3)
    assert p.valeur() == 2400
    assert p.etiquette() == "Riz : 800 FCFA"
    assert p.quantite == 3
