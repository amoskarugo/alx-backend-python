#!/usr/bin/env python3
"""
module containing a function to perform add operation on an iterable.
"""
from typing import List, Union


def sum_mixed_list(my_list: List[Union[int, float]]) -> float:
    """
    function that receives a list of floats
    and integers and adds all of them together.
    :param my_list: list containing float and int numbers.
    :return: sum of all the elements in the list.
    """
    return sum(my_list)
