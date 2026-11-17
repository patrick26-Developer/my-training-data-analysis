import pytest
from ex05_patterns import Caisse, RemiseFixe


def test_injection():
    assert Caisse(RemiseFixe(100)).total(500) == 400
    assert Caisse(RemiseFixe(100)).total(50) == 0


@pytest.mark.parametrize("remise", [-1, 501])
def test_mauvaise_strategie(remise):
    class PolitiqueInvalide:
        def calculer(self, montant):
            return remise

    with pytest.raises(ValueError):
        Caisse(PolitiqueInvalide()).total(500)


def test_remise_negative():
    with pytest.raises(ValueError):
        RemiseFixe(-1)
