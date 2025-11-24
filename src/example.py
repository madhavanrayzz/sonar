def add(a: int, b: int) -> int:
    """Return sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return difference of two numbers."""
    return a - b


def is_even(number: int) -> bool:
    """Check if number is even."""
    return number % 2 == 0


def greet(name: str = "World") -> str:
    """Return greeting message."""
    if not name:
        name = "Anonymous"
    return f"Hello, {name}!"


class Calculator:
    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
