import pytest
from ex04_heritage import RemiseSeuil, SansRemise, total_net


@pytest.mark.parametrize(("montant", "attendu"), [(0, 0), (10000, 10000), (20000, 19000)])
def test_politiques(montant, attendu):
    assert total_net(montant, SansRemise()) == montant
    assert total_net(montant, RemiseSeuil()) == attendu
    assert isinstance(RemiseSeuil(), SansRemise)


def test_polymorphisme_sans_parent():
    class AutreRemise:
        def calculer(self, montant):
            return 100

    assert total_net(500, AutreRemise()) == 400
