#!/usr/bin/env python3
"""For task 1
"""
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
    return [nums async for nums in async_generator()]
