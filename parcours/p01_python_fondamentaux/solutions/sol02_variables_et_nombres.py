"""Solutions 1.2 — Variables et nombres."""

PARITE_FCFA_EURO = 655.957  # parité fixe : 1 euro = 655,957 FCFA


def total_facture(prix_unitaire: float, quantite: int) -> float:
    return prix_unitaire * quantite


def appliquer_remise(prix: float, pourcentage: float) -> float:
    montant_remise = prix * pourcentage / 100
    return prix - montant_remise


def fcfa_en_euro(montant_fcfa: float) -> float:
    return round(montant_fcfa / PARITE_FCFA_EURO, 2)


def partager(montant: int, personnes: int) -> tuple[int, int]:
    part = montant // personnes
    reste = montant % personnes
    return part, reste
    # Équivalent en une ligne : return divmod(montant, personnes)


def nom_du_type(valeur: object) -> str:
    return type(valeur).__name__


def stock_final(stock: int, vendus: int, livres: int) -> int:
    stock -= vendus
    stock += livres
    return stock
