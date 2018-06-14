"""useful methods to convert temperatures"""


def c2f(celsius: float) -> float:
    """convert from celsius to fahrenheit"""
    return 9 * celsius / 5 + 32


def f2c(fahrenheit: float) -> float:
    """convert from fahrenheit to celsius"""
    return (fahrenheit - 32) * 5 / 9
