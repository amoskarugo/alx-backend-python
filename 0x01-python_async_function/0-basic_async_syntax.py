#!/usr/bin/env python3
"""
a module that implements a basic coroutine
"""

import random
import asyncio


async def wait_random(max_delay=10):
    """
    asynchronous coroutine that takes in an integer argument.
    waits for a random delay between 0 and max_delay and eventually returns it.
    :param max_delay: number of seconds to sleep
    :return: random number generated
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)

    return random_num
