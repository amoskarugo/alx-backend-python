#!/usr/bin/env python3
"""
a module that implements a basic coroutine
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument.
    waits for a random delay between 0 and max_delay and eventually returns it.
    :param max_delay: number of seconds to sleep
    :return: random number generated
    """
    random_num = random.uniform(0, max_delay + 1)
    await asyncio.sleep(random_num)

    return random_num
