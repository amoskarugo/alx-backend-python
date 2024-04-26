#!/usr/bin/env python3
"""

"""
import math
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple
    :param k: string
    :param v: float or int
    :return: tuple
    """
    return k, math.pow(v, 2)
