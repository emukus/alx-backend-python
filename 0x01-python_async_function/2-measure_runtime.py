#!/usr/bin/env python3
"""Takes arguments that measures the total execution time."""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n
    Returns: total time / n."""
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
