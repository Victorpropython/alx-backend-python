import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() ->>:
    start_time = time.time()
    end_time = time.time()
    elasped_time = end_time - start_time

    return [await asyncio.gather(measure_runtime())]
    return elasped_time