"""Tests de l'exercice 10.2 (tests de tes tests, par « mutation »). Ne modifie pas ce fichier.

Pour chaque fonction : une version correcte (tes tests doivent passer) et des versions
boguées, les « mutants » (tes tests doivent en détecter chacune).
"""

import pytest
from ex37_premiers_tests import (
    fizzbuzz,
    tests_pour_est_bissextile,
    tests_pour_est_pair,
    tests_pour_maximum,
    tests_pour_mention,
    tests_pour_prix_ttc,
    tests_pour_retirer,
    tests_pour_sans_doublons,
)


def verifier(tests_de_l_apprenant, correcte, mutants):
    """Les tests de l'apprenant passent avec `correcte` et échouent avec chaque mutant."""
    tests_de_l_apprenant(correcte)  # ne doit rien lever
    survivants = []
    for nom, mutant in mutants.items():
        try:
            tests_de_l_apprenant(mutant)
        except (Exception, pytest.fail.Exception):
            continue  # bug détecté (assert, pytest.raises en échec, ou plantage) : très bien
        survivants.append(nom)
    assert not survivants, f"Tes tests n'ont pas détecté ces bugs : {survivants}"


# --------------------------------------------------------------------------- est_pair
def test_est_pair():
    verifier(
        tests_pour_est_pair,
        lambda n: n % 2 == 0,
        {
            "toujours vrai": lambda n: True,
            "inversé": lambda n: n % 2 == 1,
            "zéro faux": lambda n: n != 0 and n % 2 == 0,
            "négatifs faux": lambda n: n > 0 and n % 2 == 0,
            "multiples de 4 seulement": lambda n: n % 4 == 0,
        },
    )


# --------------------------------------------------------------------------- maximum
def _maximum_correct(liste):
    return max(liste)


def test_maximum():
    def init_zero(liste):
        m = 0
        for x in liste:
            m = max(m, x)
        return m

    verifier(
        tests_pour_maximum,
        _maximum_correct,
        {
            "premier élément": lambda liste: liste[0],
            "dernier élément": lambda liste: liste[-1],
            "initialisé à zéro": init_zero,
            "minimum": lambda liste: min(liste),
            "ignore le dernier": lambda liste: max(liste[:-1]) if len(liste) > 1 else liste[0],
        },
    )


# --------------------------------------------------------------------------- prix_ttc
def test_prix_ttc():
    def correct(prix_ht, taux=18):
        return prix_ht * (1 + taux / 100)

    verifier(
        tests_pour_prix_ttc,
        correct,
        {
            "taux par défaut 20": lambda p, t=20: p * (1 + t / 100),
            "ignore le taux": lambda p, t=18: p * 1.18,
            "soustrait": lambda p, t=18: p * (1 - t / 100),
            "taux en fraction": lambda p, t=18: p * (1 + t),
            "n'ajoute rien": lambda p, t=18: p,
        },
    )


# --------------------------------------------------------------------------- mention
def test_mention():
    def correct(note):
        if note >= 16:
            return "Très bien"
        if note >= 14:
            return "Bien"
        if note >= 12:
            return "Assez bien"
        if note >= 10:
            return "Passable"
        return "Ajourné"

    def seuil(valeur, etiquette):
        def mutant(note):
            for s, nom in [(16, "Très bien"), (14, "Bien"), (12, "Assez bien"), (10, "Passable")]:
                borne = valeur if nom == etiquette else s
                if note > borne if nom == etiquette else note >= borne:
                    return nom
            return "Ajourné"

        return mutant

    mutants = {
        "> 16 au lieu de >= 16": seuil(16, "Très bien"),
        "> 14 au lieu de >= 14": seuil(14, "Bien"),
        "> 12 au lieu de >= 12": seuil(12, "Assez bien"),
        "> 10 au lieu de >= 10": seuil(10, "Passable"),
        "seuil 15": lambda n: "Très bien" if n >= 15 else correct(n),
        "tout ajourné": lambda n: "Ajourné",
    }
    verifier(tests_pour_mention, correct, mutants)


# --------------------------------------------------------------------------- retirer
def test_retirer():
    def correct(solde, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")
        if montant > solde:
            raise ValueError("Solde insuffisant")
        return solde - montant

    def sans_verif_negatif(solde, montant):
        if montant > solde:
            raise ValueError("Solde insuffisant")
        return solde - montant

    def zero_accepte(solde, montant):
        if montant < 0:
            raise ValueError("Montant invalide")
        if montant > solde:
            raise ValueError("Solde insuffisant")
        return solde - montant

    def egal_refuse(solde, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")
        if montant >= solde:
            raise ValueError("Solde insuffisant")
        return solde - montant

    def sans_verif_solde(solde, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")
        return solde - montant

    verifier(
        tests_pour_retirer,
        correct,
        {
            "montant négatif accepté": sans_verif_negatif,
            "montant zéro accepté": zero_accepte,
            "retrait total refusé": egal_refuse,
            "découvert autorisé": sans_verif_solde,
            "additionne": lambda s, m: s + m,
        },
    )


# --------------------------------------------------------------------------- sans_doublons
def test_sans_doublons():
    def correct(liste):
        resultat = []
        for e in liste:
            if e not in resultat:
                resultat.append(e)
        return resultat

    def mutant_set(liste):
        return list(set(liste))  # perd l'ordre

    def modifie_original(liste):
        i = 0
        while i < len(liste):
            if liste.index(liste[i]) != i:
                liste.pop(i)
            else:
                i += 1
        return liste

    def garde_dernier(liste):
        return list(dict.fromkeys(reversed(liste)))[::-1]

    verifier(
        tests_pour_sans_doublons,
        correct,
        {
            "ordre perdu (set)": lambda liste: sorted(set(liste), reverse=True),
            "ne fait rien": lambda liste: list(liste),
            "modifie l'original": modifie_original,
            "garde le dernier": garde_dernier,
            "vide tout": lambda liste: [],
            "set trié": lambda liste: (
                sorted(set(liste)) if liste != sorted(liste) else mutant_set(liste)
            ),
        },
    )


# --------------------------------------------------------------------------- est_bissextile
def test_est_bissextile():
    def correct(annee):
        return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)

    verifier(
        tests_pour_est_bissextile,
        correct,
        {
            "seulement /4": lambda a: a % 4 == 0,
            "oublie /400": lambda a: a % 4 == 0 and a % 100 != 0,
            "oublie /100": lambda a: a % 4 == 0 or a % 400 == 0,
            "toujours faux": lambda a: False,
            "/400 faux": lambda a: a % 4 == 0 and a % 100 != 0 and a % 400 != 0,
        },
    )


# --------------------------------------------------------------------------- fizzbuzz (TDD)
@pytest.mark.parametrize(
    ("n", "attendu"),
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (14, "14"),
    ],
)
def test_fizzbuzz(n, attendu):
    assert fizzbuzz(n) == attendu
