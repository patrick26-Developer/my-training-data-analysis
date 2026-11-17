"""Tests des solutions 9.3. Généré par outils/sync_tests_solutions.py."""

import math

import pytest
from sol34_fonctions_mathematiques import (
    comparer_fonctions,
    derivee,
    integrale,
    linspace,
    minimum,
    point_mort,
    table_de_valeurs,
    tracer_cercle,
    tracer_fonction,
    zero_par_dichotomie,
)


def test_linspace():
    assert linspace(0, 1, 5) == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])
    assert linspace(2, 2, 1) == [2]
    assert linspace(-1, 1, 3) == pytest.approx([-1.0, 0.0, 1.0])
    assert len(linspace(0, 10, 101)) == 101


def test_table_de_valeurs():
    table = table_de_valeurs(lambda x: x**2, -1, 1, 3)
    assert [x for x, _ in table] == pytest.approx([-1.0, 0.0, 1.0])
    assert [y for _, y in table] == pytest.approx([1.0, 0.0, 1.0])


def test_tracer_fonction():
    fig = tracer_fonction(lambda x: x**2, -3, 3, "Parabole", n=50)
    ax = fig.axes[0]
    assert ax.get_title() == "Parabole"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "f(x)"
    assert len(ax.lines[0].get_xdata()) == 50
    assert min(ax.lines[0].get_ydata()) == pytest.approx(0, abs=0.01)


def test_zero_par_dichotomie():
    assert zero_par_dichotomie(lambda x: x**2 - 2, 0, 2) == pytest.approx(math.sqrt(2), abs=1e-6)
    assert zero_par_dichotomie(lambda x: x - 3, 0, 10) == pytest.approx(3.0, abs=1e-6)
    with pytest.raises(ValueError, match="Zéro non encadré"):
        zero_par_dichotomie(lambda x: x**2 + 1, -1, 1)


def test_integrale():
    assert integrale(lambda x: x**2, 0, 3) == pytest.approx(9.0, abs=1e-3)
    assert integrale(lambda x: 2, 0, 5) == pytest.approx(10.0)
    assert integrale(math.sin, 0, math.pi) == pytest.approx(2.0, abs=1e-4)


def test_derivee():
    assert derivee(lambda x: x**2, 3) == pytest.approx(6.0, abs=1e-4)
    assert derivee(math.sin, 0) == pytest.approx(1.0, abs=1e-4)


def test_minimum():
    x, y = minimum(lambda x: (x - 2) ** 2 + 1, -5, 5)
    assert x == pytest.approx(2.0, abs=0.02)
    assert y == pytest.approx(1.0, abs=0.01)


@pytest.mark.parametrize(
    ("prix", "cv", "cf", "attendu"),
    [(1500, 700, 20000, 25), (100, 100, 10, None), (100, 150, 10, None), (10, 5, 0, 0)],
)
def test_point_mort(prix, cv, cf, attendu):
    assert point_mort(prix, cv, cf) == attendu


def test_tracer_cercle():
    fig = tracer_cercle(2)
    ax = fig.axes[0]
    xs = ax.lines[0].get_xdata()
    ys = ax.lines[0].get_ydata()
    assert len(xs) == 100
    assert all(math.isclose(math.hypot(x, y), 2, abs_tol=1e-9) for x, y in zip(xs, ys, strict=True))
    assert ax.get_aspect() in (1.0, "equal")


def test_comparer_fonctions():
    fig = comparer_fonctions({"sin": math.sin, "cos": math.cos}, 0, 6.28, n=60)
    ax = fig.axes[0]
    assert len(ax.lines) == 2
    assert [t.get_text() for t in ax.get_legend().get_texts()] == ["sin", "cos"]
