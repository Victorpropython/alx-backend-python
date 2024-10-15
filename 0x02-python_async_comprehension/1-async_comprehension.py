#!/usr/bin/rnv python3
import asyncio
import random
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


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
