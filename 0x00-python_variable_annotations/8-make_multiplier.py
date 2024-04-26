#!/usr/bin/env python3
"""
module that implements Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    :param multiplier:
    :return: function
    """
    def multiply(m: float) -> float:
        """
        inner function
        :param m: multiplier
        :return:
        """
        return m * multiplier
    return multiply
