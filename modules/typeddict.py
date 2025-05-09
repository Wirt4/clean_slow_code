from abc import ABC, abstractmethod
from enum import Enum, auto
from math import pi
from typing import List, TypedDict


class ShapeType(Enum):
    CIRCLE = auto()
    RECTANGLE = auto()
    TRIANGLE = auto()
    SHAPE_COUNT = auto()


class ShapeUnion(TypedDict):
    shape_type: ShapeType
    width: float
    height: float


def get_area(shape: ShapeUnion) -> float:
    if shape["shape_type"] == ShapeType.CIRCLE:
        return shape["width"] * shape["height"] * pi * 0.25
    if shape["shape_type"] == ShapeType.RECTANGLE:
        return shape["width"] * shape["height"]
    if shape["shape_type"] == ShapeType.TRIANGLE:
        return shape["width"] * shape["height"] * 0.5
    raise ValueError("invalid shape type")


def total_area(shapes: List[ShapeUnion]) -> float:
    """
    Returns the sum total area of all shapes in the list
    """
    sum_total: float = 0.0
    for i in range(len(shapes)):
        sum_total += get_area(shapes[i])
    return sum_total


def total_area_in_groups_of_4(shapes: List[ShapeUnion]) -> float:
    """
    Returns the sum total area of all shapes in the list.
    The iteration is batched in groups of 4
    """
    accum_0: float = 0.0
    accum_1: float = 0.0
    accum_2: float = 0.0
    accum_3: float = 0.0
    for i in range(0, len(shapes), 4):
        accum_0 += 0 if i >= len(shapes) else get_area(shapes[i])
        accum_1 += 0 if i + 1 >= len(shapes) else get_area(shapes[i + 1])
        accum_2 += 0 if i + 2 >= len(shapes) else get_area(shapes[i + 2])
        accum_3 += 0 if i + 3 >= len(shapes) else get_area(shapes[i + 3])
    return accum_0 + accum_1 + accum_2 + accum_3
