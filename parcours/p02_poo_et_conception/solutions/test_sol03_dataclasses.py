from dataclasses import FrozenInstanceError

import pytest
from sol03_dataclasses import Vente, creer_vente


def test_egalite_total_et_representation():
    a = Vente("Riz", 800, 3)
    assert a == Vente("Riz", 800, 3)
    assert a != Vente("Riz", 900, 3)
    assert a.total() == 2400
    assert "Riz" in repr(a)


def test_instantane_gele():
    produit = {"nom": "Riz", "prix": 800, "quantite": 3}
    vente = creer_vente(produit)
    produit["prix"] = 900
    assert vente.prix == 800
    with pytest.raises(FrozenInstanceError):
        vente.prix = 1000
