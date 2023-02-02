#!/usr/bin/env python3
"""A type-annotated 'to_kv' function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k, and an int OR float v as arguments
    Returns: k and the square of v as a tuple"""

    return (k, v**2)
