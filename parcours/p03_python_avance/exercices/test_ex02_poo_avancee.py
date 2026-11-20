"""Tests du contrat demandé dans les exercices 3.2."""

import pytest
from ex02_poo_avancee import Article, Catalogue, Paiement, PaiementSimulation


def test_prix_modifiable_et_nul() -> None:
    article = Article("Cahier", 1000)
    assert article.prix == 1000
    article.prix = 0
    assert article.prix == 0


def test_creation_invalide() -> None:
    with pytest.raises(ValueError):
        Article("Cahier", -1)


def test_modification_invalide_conserve_prix() -> None:
    article = Article("Cahier", 1000)
    with pytest.raises(ValueError):
        article.prix = -1
    assert article.prix == 1000


def test_contrat_abstrait() -> None:
    with pytest.raises(TypeError):
        Paiement()  # type: ignore[abstract]


@pytest.mark.parametrize("montant", [0, 1000, 5000])
def test_paiement_simule(montant: int) -> None:
    assert PaiementSimulation().payer(montant) == f"Simulation : {montant} FCFA"


def test_paiement_negatif() -> None:
    with pytest.raises(ValueError):
        PaiementSimulation().payer(-1)


def test_catalogue_vide() -> None:
    catalogue = Catalogue([])
    assert len(catalogue) == 0
    assert list(catalogue) == []
    with pytest.raises(IndexError):
        catalogue[0]


def test_catalogue_copie_conteneur_et_partage_articles() -> None:
    article = Article("Cahier", 1000)
    source = [article]
    catalogue = Catalogue(source)
    source.clear()
    assert len(catalogue) == 1
    assert catalogue[0] is article
    article.prix = 1500
    assert catalogue[0].prix == 1500


def test_iteration_repetable_et_indices() -> None:
    articles = [Article("Cahier", 1000), Article("Stylo", 500)]
    catalogue = Catalogue(a for a in articles)
    assert list(catalogue) == articles
    assert list(catalogue) == articles
    assert catalogue[-1] is articles[1]
    assert sum(a.prix for a in catalogue) == 1500
    with pytest.raises(IndexError):
        catalogue[2]
