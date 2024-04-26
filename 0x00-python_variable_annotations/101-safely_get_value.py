#!/usr/bin/env python3
"""
module that contains a function that implements More involved type annotations
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[None, T]) -> Union[Any, T]:
    """

    :param dct: a dictionary
    :param key: key in dictionary
    :param default: generic type or any type
    :return: element in dictionary or the default value passed
    """
    if key in dct:
        return dct[key]
    else:
        return default
