from typing import List

from modules.oop import Shape, total_area, total_area_in_groups_of_4
from modules.random_shapes import random_shape_oop

shape_list_size: int = 100000


def make_list(shape_lambda):
    """
    makes a list from the shape generating function, and returns the list
    Note, there's duck-typing here so it can be used both for the OOP and struct versions
    """
    return [shape_lambda() for _ in range(shape_list_size)]


def run_oop() -> None:
    """
    Runs the batched and un-batched versions of total area
    """
    shape_list: List[Shape] = make_list(random_shape_oop)
    total_area(shape_list)
    total_area_in_groups_of_4(shape_list)


def run_struct() -> None:
    """
    Runs the batched and un-batched versions of total area
    """
    shape_list: List[Shape] = make_list(random_shape_oop)
    total_area(shape_list)
    total_area_in_groups_of_4(shape_list)
