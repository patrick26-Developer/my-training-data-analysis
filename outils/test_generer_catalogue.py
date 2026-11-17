"""Tests du générateur de catalogue : phases de lancement, prix bornés, même prix en trois devises."""

import importlib.util
from datetime import date
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "generer_catalogue", Path(__file__).resolve().parent / "generer_catalogue.py"
)
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)

LANCEMENT = {
    "gratuit_mois": 2,
    "gratuit_jours": 0,
    "telechargements_gratuits": True,
    "date_ouverture": "2026-12-01",
    "annonce_avant_jours": 15,
}


@pytest.mark.parametrize(
    ("jour", "phase"),
    [
        (date(2026, 11, 30), "avant_ouverture"),
        (date(2026, 12, 1), "lancement_gratuit"),
        (date(2027, 1, 31), "lancement_gratuit"),
        (date(2027, 2, 1), "premium"),
    ],
)
def test_phase_de_lancement(jour, phase):
    assert g.phase_de_lancement(LANCEMENT, jour)["phase_actuelle"] == phase


def test_dates_du_premium_et_de_l_annonce():
    resultat = g.phase_de_lancement(LANCEMENT, date(2026, 12, 2))
    assert resultat["date_debut_premium"] == "2027-02-01"
    assert resultat["date_annonce_premium"] == "2027-01-17"


def test_un_mois_et_demi():
    config = {**LANCEMENT, "gratuit_mois": 1, "gratuit_jours": 15}
    assert g.phase_de_lancement(config, date(2026, 12, 2))["date_debut_premium"] == "2027-01-16"


def test_date_ouverture_inconnue():
    config = {**LANCEMENT, "date_ouverture": ""}
    resultat = g.phase_de_lancement(config)
    assert resultat["phase_actuelle"] == "a_definir"
    assert resultat["date_debut_premium"] is None


def test_ajouter_mois_fin_de_mois():
    assert g.ajouter_mois(date(2026, 12, 31), 2) == date(2027, 2, 28)
    assert g.ajouter_mois(date(2026, 1, 31), 1) == date(2026, 2, 28)


@pytest.mark.parametrize(
    ("montant", "attendu"), [(300, 1000), (1000, 1000), (2500, 2500), (5000, 5000), (9000, 5000)]
)
def test_prix_borne_dans_la_fourchette(montant, attendu):
    assert g.borner(montant, 1000, 5000) == attendu


def test_meme_prix_en_trois_devises():
    general = {"parite_euro": 655.957, "usd_pour_1_eur": 1.10, "arrondi_devises": 0.5}
    prix = g.prix_multidevises(2000, general)
    assert prix == {"XAF": 2000, "EUR": 3.0, "USD": 3.5}
    # équivalence : le montant en EUR correspond bien à celui en XAF (à l'arrondi près)
    assert prix["EUR"] * general["parite_euro"] == pytest.approx(2000, abs=0.25 * 655.957)


def test_le_catalogue_respecte_la_fourchette():
    import json

    catalogue = json.loads(
        (Path(__file__).resolve().parent.parent / "catalogue" / "catalogue.json").read_text(
            encoding="utf-8"
        )
    )
    plancher = catalogue["fourchette_prix_xaf"]["plancher"]
    plafond = catalogue["fourchette_prix_xaf"]["plafond"]
    for parcours in catalogue["parcours"]:
        for tarif in parcours["prix"].values():
            assert plancher <= tarif["XAF"] <= plafond
