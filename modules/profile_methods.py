from modules.oop import total_area
from modules.random_shapes import random_shape_oop

shape_list_size: int = 100000


def make_list(shape_lambda):
    return [shape_lambda() for _ in range(shape_list_size)]


def run_oop() -> None:
    total_area(make_list(random_shape_oop))
