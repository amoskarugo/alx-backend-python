#!/usr/bin/env python3
"""
module containing a function to perform add operation on an iterable.
"""
from typing import List
lst: List[float]


def sum_list(my_list: lst) -> float:
    """
    function that receives a list of floats and adds all of them together.
    :param my_list: list containing float numbers.
    :return: sum of all the elements in the list.
    """
    return sum(my_list)
