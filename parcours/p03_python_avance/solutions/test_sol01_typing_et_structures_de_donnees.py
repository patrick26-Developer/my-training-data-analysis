"""Tests des solutions 1.1. Généré par outils/sync_tests_solutions.py : il valide ex01_*.py."""

import dataclasses

import pytest
from sol01_typing_et_structures_de_donnees import (
    RGB,
    Point3D,
    Stack,
    describe_mode,
    make_user_payload,
    plus_petit,
    process,
)


class TestPoint3D:
    def test_distance_to(self) -> None:
        a = Point3D(0.0, 0.0, 0.0)
        b = Point3D(3.0, 4.0, 0.0)
        assert a.distance_to(b) == pytest.approx(5.0)

    def test_is_frozen(self) -> None:
        p = Point3D(1.0, 2.0, 3.0)
        with pytest.raises(dataclasses.FrozenInstanceError):
            p.x = 99.0  # type: ignore[misc]

    def test_has_slots_no_dict(self) -> None:
        p = Point3D(1.0, 2.0, 3.0)
        assert not hasattr(p, "__dict__")


class TestRGB:
    def test_is_named_tuple_with_fields(self) -> None:
        color = RGB(255, 0, 127)
        assert color.r == 255
        assert color.g == 0
        assert color.b == 127
        r, g, b = color  # déballage type tuple
        assert (r, g, b) == (255, 0, 127)


class TestUserPayload:
    def test_make_user_payload(self) -> None:
        payload = make_user_payload(1, "a@example.com", True)
        assert payload == {"id": 1, "email": "a@example.com", "is_active": True}


class TestPlusPetit:
    def test_int(self) -> None:
        assert plus_petit(3, 5) == 3

    def test_str(self) -> None:
        assert plus_petit("banane", "abricot") == "abricot"


class TestStack:
    def test_push_pop_lifo_order(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_is_empty(self) -> None:
        stack: Stack[str] = Stack()
        assert stack.is_empty() is True
        stack.push("x")
        assert stack.is_empty() is False

    def test_pop_empty_raises(self) -> None:
        stack: Stack[int] = Stack()
        with pytest.raises(IndexError):
            stack.pop()


class TestProcess:
    def test_int_to_str(self) -> None:
        assert process(42) == "42"

    def test_str_to_int(self) -> None:
        assert process("42") == 42


class TestDescribeMode:
    def test_returns_message(self) -> None:
        assert "read" in describe_mode("read")
