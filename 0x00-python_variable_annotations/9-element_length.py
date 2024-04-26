#!/usr/bin/env python3
"""
module that implements a function that performs complex
type annotation
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    :param lst: an iterable object
    :return: list of tuples
    """
    return [(i, len(i)) for i in lst]
