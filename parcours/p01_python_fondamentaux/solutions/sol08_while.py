"""Solutions 3.1 — La boucle while."""


def somme_jusqua(n: int) -> int:
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def factorielle(n: int) -> int:
    resultat = 1
    i = 2
    while i <= n:
        resultat *= i
        i += 1
    return resultat


def nombre_de_bits(n: int) -> int:
    bits = 0
    while n > 0:
        n //= 2
        bits += 1
    return bits


def annees_pour_atteindre(capital: float, objectif: float, taux: float) -> int:
    annees = 0
    while capital < objectif:
        capital *= 1 + taux / 100
        annees += 1
    return annees


def collatz(n: int) -> int:
    etapes = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        etapes += 1
    return etapes


def somme_des_chiffres(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def total_jusqua_fin(saisies: list[str]) -> float:
    total = 0.0
    i = 0
    while i < len(saisies) and saisies[i] != "fin":
        total += float(saisies[i])
        i += 1
    return total
