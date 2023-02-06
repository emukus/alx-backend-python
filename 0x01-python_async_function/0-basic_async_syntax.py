#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an int arguments and waits
for a random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay btwn 0 & max_delay, and returns that"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
