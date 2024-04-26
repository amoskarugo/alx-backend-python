#!/usr/bin/env python3
"""
Type Checking using mypy
"""
from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """

    :param lst: a tuple
    :param factor: integer to loop upto
    :return: a list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
