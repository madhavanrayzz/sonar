import pytest
from your_package.example import (
    add, subtract, is_even, greet, Calculator
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-2) is True


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet() == "Hello, World!"
    assert greet("") == "Hello, Anonymous!"
    assert greet(None) == "Hello, Anonymous!"


def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10


def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5


def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)
