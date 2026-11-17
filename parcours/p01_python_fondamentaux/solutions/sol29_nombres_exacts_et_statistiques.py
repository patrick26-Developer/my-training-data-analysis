"""Solutions 8.2 — Calculs exacts, hasard et statistiques."""

import random
import statistics
from collections.abc import Callable
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction


def total_exact(prix: list[str]) -> Decimal:
    total = Decimal("0")
    for p in prix:
        total += Decimal(p)
    return total


def ttc(prix_ht: str, taux: str) -> Decimal:
    montant = Decimal(prix_ht) * (1 + Decimal(taux))
    return montant.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def somme_fractions(fractions: list[tuple[int, int]]) -> Fraction:
    total = Fraction(0)
    for numerateur, denominateur in fractions:
        total += Fraction(numerateur, denominateur)
    return total


def lancer_des(n: int, graine: int) -> list[int]:
    random.seed(graine)
    return [random.randint(1, 6) for _ in range(n)]


def resume(notes: list[float]) -> dict[str, float]:
    return {
        "moyenne": round(statistics.mean(notes), 2),
        "mediane": statistics.median(notes),
        "mode": statistics.mode(notes),
        "ecart_type": round(statistics.pstdev(notes), 2),
    }


def valeurs_aberrantes(valeurs: list[float], k: float = 2) -> list[float]:
    moyenne = statistics.mean(valeurs)
    ecart_type = statistics.pstdev(valeurs)
    return [v for v in valeurs if abs(v - moyenne) > k * ecart_type]


def probabilite_estimee(evenement: Callable[[], bool], essais: int, graine: int) -> float:
    random.seed(graine)
    succes = sum(1 for _ in range(essais) if evenement())
    return succes / essais


def tirage_loto(graine: int) -> list[int]:
    random.seed(graine)
    return sorted(random.sample(range(1, 50), 6))
