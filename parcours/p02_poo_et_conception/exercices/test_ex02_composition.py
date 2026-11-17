import pytest
from ex02_composition import Stock


def test_cumul_et_independance():
    a, b = Stock(), Stock()
    a.ajouter("Riz", 2)
    a.ajouter("Riz", 3)
    assert a.quantite("Riz") == 5
    assert b.quantite("Riz") == 0


@pytest.mark.parametrize("q", [0, -1, 1.5, True])
def test_refus_sans_mutation(q):
    stock = Stock()
    stock.ajouter("Riz", 2)
    with pytest.raises(ValueError):
        stock.ajouter("Riz", q)
    assert stock.quantite("Riz") == 2


def test_copie():
    stock = Stock()
    stock.ajouter("Riz", 2)
    copie = stock.produits
    copie["Riz"] = 100
    assert stock.quantite("Riz") == 2
