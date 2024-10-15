#!/usr/bin/env python3
"""Task 2
"""
import asyncio
import time
from typing import List
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    An async function to check for time used in
    executin four parrallel task
    """
    start_time = time.time()
    end_time = time.time()
    elasped_time = end_time - start_time

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return elasped_time
