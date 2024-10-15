#!/usr/bin/env python3
import asyncio
import random
from heapq import heappush, heappop
from typing import List

# importing wait_random
# from basic_async_syntax import wait_random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    Asynchronous function to spawn n no of times,
    with specified max_delay.

    Args, n and max_delay. Where n is the integer
    number of times and max_delay is the maximum
    number of delay.
    """
    # Creating a list
    delay = []

    # Creating a list for awaitable tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Run all taks concurrently and get result
    delay = await asyncio.gather(*tasks)

    # Returning the delays
    return sorted(delay)
