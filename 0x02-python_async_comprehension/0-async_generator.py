#!/usr/bin/env python3
"""Task 0
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:

    """
    An Asynchronous program to take no arguments
    an loop 10 times. Waiting 10seconds before its yeild
    given a random number between 0 and 10
    Args:
    no args taken
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
