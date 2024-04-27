#!/usr/bin/env python3
"""basic async comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generate a list of random numbers"""
    lst = [_ async for _ in async_generator()]
    return lst
