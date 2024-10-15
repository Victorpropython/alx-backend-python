#!/usr/bin/rnv python3
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """
    Asyncgronous function to collect 10 random number
    using list async type.
    Args:
    No arguments but rather it returns 10 random numbers
    collected for async_generator.
    """
    # using an async comprehension to collect 10 random number
    return [data async for data in async_generator()]
