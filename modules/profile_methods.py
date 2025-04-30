from modules.random_shapes import random_shape_oop, random_shape_struct
from modules.oop import total_area_oop, Shape
from modules.struct import total_area_struct, ShapeStruct

shape_list_size: int = 100000


def make_list(shape_lambda):
    return [shape_lambda() for _ in range(shape_list_size)]


def run_oop() -> None:
    total_area_oop(make_list(random_shape_oop))


def run_struct() -> None:
    total_area_struct(make_list(random_shape_struct))
