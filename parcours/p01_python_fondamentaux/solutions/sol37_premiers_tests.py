"""Solutions 10.2 — Des tests qui détectent les bugs."""

import pytest


def tests_pour_est_pair(est_pair):
    assert est_pair(2) is True
    assert est_pair(0) is True  # cas limite : zéro est pair
    assert est_pair(1) is False
    assert est_pair(7) is False
    assert est_pair(-4) is True  # négatif pair (et pas multiple de 4 seulement : -6)
    assert est_pair(-3) is False
    assert est_pair(6) is True  # pair mais pas multiple de 4


def tests_pour_maximum(maximum):
    assert maximum([3, 9, 2]) == 9  # au milieu
    assert maximum([9, 3, 2]) == 9  # au début
    assert maximum([2, 3, 9]) == 9  # à la fin
    assert maximum([-5, -2, -9]) == -2  # tous négatifs (piège de l'initialisation à 0)
    assert maximum([7]) == 7  # un seul élément
    assert maximum([4, 4, 4]) == 4  # tous égaux


def tests_pour_prix_ttc(prix_ttc):
    assert prix_ttc(1000) == pytest.approx(1180.0)  # taux par défaut : 18 %
    assert prix_ttc(1000, 5) == pytest.approx(1050.0)  # taux explicite
    assert prix_ttc(1000, 0) == pytest.approx(1000.0)  # taux nul
    assert prix_ttc(0) == pytest.approx(0.0)  # prix nul
    assert prix_ttc(200, 50) == pytest.approx(300.0)


def tests_pour_mention(mention):
    assert mention(20) == "Très bien"
    assert mention(16) == "Très bien"  # limites : on teste CHAQUE seuil et juste en dessous
    assert mention(15.99) == "Bien"
    assert mention(14) == "Bien"
    assert mention(13.99) == "Assez bien"
    assert mention(12) == "Assez bien"
    assert mention(11.99) == "Passable"
    assert mention(10) == "Passable"
    assert mention(9.99) == "Ajourné"
    assert mention(0) == "Ajourné"
    assert mention(15) == "Bien"


def tests_pour_retirer(retirer):
    assert retirer(1000, 300) == 700  # cas normal
    assert retirer(1000, 1000) == 0  # limite : retrait total autorisé
    assert retirer(1000, 1) == 999
    with pytest.raises(ValueError):  # montant nul
        retirer(1000, 0)
    with pytest.raises(ValueError):  # montant négatif
        retirer(1000, -50)
    with pytest.raises(ValueError):  # solde insuffisant
        retirer(1000, 1001)


def tests_pour_sans_doublons(sans_doublons):
    assert sans_doublons([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert sans_doublons([3, 1, 3, 2, 1]) == [3, 1, 2]  # ordre de PREMIÈRE apparition
    assert sans_doublons([]) == []
    assert sans_doublons([5]) == [5]
    assert sans_doublons(["b", "a", "b"]) == ["b", "a"]
    original = [2, 2, 1]
    sans_doublons(original)
    assert original == [2, 2, 1]  # l'original n'est pas modifié
    assert sans_doublons([1, 2, 3]) == [1, 2, 3]
    assert sans_doublons([9, 8, 9, 8, 7]) == [9, 8, 7]


def tests_pour_est_bissextile(est_bissextile):
    assert est_bissextile(2024) is True  # divisible par 4
    assert est_bissextile(2023) is False  # non divisible par 4
    assert est_bissextile(1900) is False  # siècle non divisible par 400
    assert est_bissextile(2000) is True  # divisible par 400
    assert est_bissextile(2100) is False
    assert est_bissextile(1600) is True
    assert est_bissextile(2026) is False
    assert est_bissextile(2028) is True


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
