"""Solutions 9.1 — La géométrie derrière turtle."""

import math

Point = tuple[float, float]


def angle_de_rotation(n: int) -> float:
    return 360 / n


def angle_interieur(n: int) -> float:
    return 180 - angle_de_rotation(n)


def sommets_polygone(n: int, rayon: float) -> list[Point]:
    points = []
    for k in range(n):
        angle = 2 * math.pi * k / n
        x = round(rayon * math.cos(angle), 6) + 0.0  # + 0.0 évite « -0.0 »
        y = round(rayon * math.sin(angle), 6) + 0.0
        points.append((x, y))
    return points


def perimetre_polygone(points: list[Point]) -> float:
    total = 0.0
    for i, depart in enumerate(points):
        arrivee = points[(i + 1) % len(points)]  # le dernier point rejoint le premier
        total += math.dist(depart, arrivee)
    return round(total, 6)


def longueur_cote(n: int, rayon: float) -> float:
    return round(2 * rayon * math.sin(math.pi / n), 6)


def chemin_carre(cote: float) -> list[tuple[str, float]]:
    chemin: list[tuple[str, float]] = []
    for _ in range(4):
        chemin.append(("forward", cote))
        chemin.append(("left", 90))
    return chemin


def position_finale(ordres: list[tuple[str, float]]) -> Point:
    x = y = 0.0
    cap = 0.0  # angle en degrés, 0 = Est
    for ordre, valeur in ordres:
        match ordre:
            case "forward":
                x += valeur * math.cos(math.radians(cap))
                y += valeur * math.sin(math.radians(cap))
            case "left":
                cap += valeur
            case "right":
                cap -= valeur
    return round(x, 6) + 0.0, round(y, 6) + 0.0


def aire_polygone(points: list[Point]) -> float:
    somme = 0.0
    for i, (x1, y1) in enumerate(points):
        x2, y2 = points[(i + 1) % len(points)]
        somme += x1 * y2 - x2 * y1
    return round(abs(somme) / 2, 6)
