#!/usr/bin/env python3
"""basics of async await"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    multiple coroutines
    :param n: number of times to run the task
    :param max_delay: wait time before execution
    :return: list of result of all tasks
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
