"""Tests des solutions 1.1. Généré par outils/sync_tests_solutions.py."""

from sol01_premiers_pas import (
    afficher_adresse,
    afficher_produit,
    carte_de_visite,
    message_bienvenue,
    salutation,
)


def test_message_bienvenue():
    assert message_bienvenue() == "Bienvenue à Mayele Python Académie !"


def test_salutation():
    assert salutation("Grâce") == "Mbote, Grâce !"
    assert salutation("Jean") == "Mbote, Jean !"


def test_afficher_produit(capsys):
    afficher_produit()
    assert capsys.readouterr().out == "Manioc : 500 FCFA\n"


def test_afficher_adresse(capsys):
    afficher_adresse()
    assert capsys.readouterr().out == "Boutique Mama Nzoni\nBrazzaville\n"


def test_carte_de_visite():
    assert carte_de_visite("Mama Nzoni", "Pointe-Noire") == "Mama Nzoni\nPointe-Noire"
