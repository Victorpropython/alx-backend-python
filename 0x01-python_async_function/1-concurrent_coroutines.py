#!/usr/bin/env python3
import asyncio
import random

wait_random = __import__ ('0-basic_async_syntax')

async def wait_n(n, max_delay):
    """
    Asynchronous function to spawn n no of times,
    with specified max_delay.

    Args, n and max_delay. Where n is the integer 
    number of times and max_delay is the maximum 
    number of delay.
    """
    stalling = random.uniform(0, max_delay)

    await asyncio.sleep(stalling)

    #print(wait_n(range(n,max_delay)))

    return stalling#wait_n(n, max_delay)
