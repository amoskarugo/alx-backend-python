#!/usr/bin/env python3
"""async comprehension basics"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float]:
    """function to yield random numbers"""
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
