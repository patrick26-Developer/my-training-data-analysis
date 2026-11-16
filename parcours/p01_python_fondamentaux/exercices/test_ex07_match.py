"""Tests de l'exercice 2.3. Ne modifie pas ce fichier."""

import pytest
from ex07_match import (
    action_menu,
    calculer,
    jours_du_mois,
    operateur,
    statut_commande,
    type_de_jour,
)


@pytest.mark.parametrize(
    ("choix", "attendu"),
    [
        ("1", "ajouter"),
        ("2", "supprimer"),
        ("3", "afficher"),
        ("q", "quitter"),
        ("Q", "quitter"),
        ("x", "inconnu"),
    ],
)
def test_action_menu(choix, attendu):
    assert action_menu(choix) == attendu


@pytest.mark.parametrize(
    ("jour", "attendu"),
    [
        ("lundi", "semaine"),
        ("vendredi", "semaine"),
        ("samedi", "week-end"),
        ("dimanche", "week-end"),
        ("jeudi2", "inconnu"),
    ],
)
def test_type_de_jour(jour, attendu):
    assert type_de_jour(jour) == attendu


@pytest.mark.parametrize(
    ("mois", "attendu"),
    [(1, 31), (2, 28), (4, 30), (8, 31), (11, 30), (12, 31), (0, 0), (13, 0)],
)
def test_jours_du_mois(mois, attendu):
    assert jours_du_mois(mois) == attendu


@pytest.mark.parametrize(
    ("indicatif", "attendu"),
    [("04", "MTN"), ("05", "Airtel"), ("06", "Airtel"), ("07", "Inconnu")],
)
def test_operateur(indicatif, attendu):
    assert operateur(indicatif) == attendu


@pytest.mark.parametrize(
    ("a", "op", "b", "attendu"),
    [
        (6, "+", 2, 8),
        (6, "-", 2, 4),
        (6, "*", 2, 12),
        (6, "/", 2, 3),
        (6, "/", 0, None),
        (6, "%", 2, None),
    ],
)
def test_calculer(a, op, b, attendu):
    assert calculer(a, op, b) == attendu


@pytest.mark.parametrize(
    ("quantite", "attendu"),
    [(0, "vide"), (-2, "invalide"), (1, "normale"), (9, "normale"), (10, "grosse"), (80, "grosse")],
)
def test_statut_commande(quantite, attendu):
    assert statut_commande(quantite) == attendu
