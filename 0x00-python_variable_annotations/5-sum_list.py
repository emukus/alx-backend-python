#!/usr/bin/env python3
"""A type-annotated 'sum_list' function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats as arguments
    Returns their sum as a float."""

    return sum(input_list)
