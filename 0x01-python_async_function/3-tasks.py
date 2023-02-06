#!/usr/bin/env python3
"""Function that takes an int and returns a asyncio.Task"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Waits for random delay then returns asyncio.Task object"""
    task = create_task(wait_random(max_delay))
    return task
