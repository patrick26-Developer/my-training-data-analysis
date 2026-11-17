"""Solutions 8.1 — Maths et formules."""

import math


def aire_disque(rayon: float) -> float:
    return math.pi * rayon**2


def perimetre_disque(rayon: float) -> float:
    return 2 * math.pi * rayon


def volume_cylindre(rayon: float, hauteur: float) -> float:
    return math.pi * rayon**2 * hauteur


def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)  # ou math.hypot(a, b)


def capital_final(capital: float, taux_annuel: float, annees: float) -> float:
    return capital * (1 + taux_annuel / 100) ** annees


def mensualite(capital: float, taux_annuel: float, mois: int) -> float:
    i = taux_annuel / 100 / 12  # taux mensuel
    if i == 0:
        return capital / mois
    return capital * i / (1 - (1 + i) ** -mois)


def resoudre_second_degre(a: float, b: float, c: float) -> list[float]:
    delta = b**2 - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    racine = math.sqrt(delta)
    return sorted([(-b - racine) / (2 * a), (-b + racine) / (2 * a)])


def variation_pourcentage(ancien: float, nouveau: float) -> float:
    return round((nouveau - ancien) / ancien * 100, 2)


def sont_egaux(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=1e-9)


def combinaisons_loto(n: int, k: int) -> int:
    return math.comb(n, k)


def angle_en_radians(degres: float) -> float:
    return math.radians(degres)


def sinus_en_degres(degres: float) -> float:
    return math.sin(math.radians(degres))
