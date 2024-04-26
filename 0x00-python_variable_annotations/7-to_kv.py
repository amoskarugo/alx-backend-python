#!/usr/bin/env python3
"""

"""
import math
from typing import Union, Tuple, Any


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple
    :param k: string
    :param v: float or int
    :return: tuple
    """
    return k, v ** 2
