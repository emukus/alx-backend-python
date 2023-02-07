#!/usr/bin/env python3
"""Coroutines that imports async_comprehension and executes it four times"""

from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the execution time of async_comprehension"""
    t = perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - t
