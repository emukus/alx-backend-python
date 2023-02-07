#!/usr/bin/env python3
"""A coroutine that takes no arguments."""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, each time asynchronously waits 1 sec,
    then yield a random int between 0 and 10."""
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
