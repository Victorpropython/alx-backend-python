#!/usr/bin/env python3
"""Function to measure the total time of execution for wait_n(n, max_delay)
And return total_time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Funtion to calculate the total time elasped
    """
    start_time = time.time()  # The start time
    asyncio.run(wait_n(n, max_delay))  # calling wait_n function
    return (time.time() - start_time) / n
