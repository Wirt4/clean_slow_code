from typing import List

from modules import oop, typeddict
from modules.random_shapes import random_shape_oop

shape_list_size: int = 100000


def make_list(shape_lambda):
    """
    makes a list from the shape generating function, and returns the list
    Note, there's duck-typing here so it can be used both for the OOP and typeddict versions
    """
    return [shape_lambda() for _ in range(shape_list_size)]


def run_oop() -> None:
    """
    Runs the batched and un-batched versions of total area
    """
    shape_list: List[oop.Shape] = make_list(random_shape_oop)
    oop.total_area(shape_list)
    oop.total_area_in_groups_of_4(shape_list)


def run_typeddict() -> None:
    """
    Runs the batched and un-batched versions of total area
    """
    shape_list: List[typeddict.Shape] = make_list(random_shape_oop)
    typeddict.total_area(shape_list)
    typeddict.total_area_in_groups_of_4(shape_list)
