#!/usr/bin/env python3
"""Solving for task 4
"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    Asynchronous function to spawn n no of times,
    with specified max_delay.

    Args, n and max_delay. Where n is the integer
    number of times and max_delay is the maximum
    number of delay.
    Creating an identical with wait_n but this time
    using task_wait_random
    """
    # Executing  awaitable tasks
    tasks = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n))))
    # Returning the tasks
    return sorted(tasks)
