#!/usr/bin/env python3
"""A type-annotated 'make_multiplier' function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float as an argument
    Returns: a function that multiplies a float by multiplier"""
    def f(n: float) -> float:
        """Multiplies a float by multiplier"""
        return float(n * multiplier)

    return f
