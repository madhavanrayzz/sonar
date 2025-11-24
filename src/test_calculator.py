# test_calculator.py
import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-3, 5) == -15
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)
