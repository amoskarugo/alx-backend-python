#!/usr/bin/env python3
"""
module that implements a function that has a return type of any or none
"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not known


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function that returns the first element of a list
    :param lst:  of elements
    :return: first element or none if list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
