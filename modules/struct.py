from typing import TypedDict, Union, Literal, List
import random
from math import pi

"""
Old-fashioned flat struct version
"""


class RectangleStruct(TypedDict):
    type: Literal["rectangle"]
    width: float
    height: float


class CircleStruct(TypedDict):
    type: Literal["circle"]
    radius: float


class TriangleStruct(TypedDict):
    type: Literal["triangle"]
    base: float
    height: float


ShapeStruct = Union[RectangleStruct, CircleStruct, TriangleStruct]


def area(shape: ShapeStruct) -> float:
    if shape["type"] == "rectangle":
        return shape["width"] * shape["height"]
    elif shape["type"] == "circle":
        return pi * shape["radius"] ** 2
    elif shape["type"] == "triangle":
        return 0.5 * shape["base"] * shape["height"]
    else:
        raise ValueError("Unknown shape")


def total_area_struct(shapes: List[ShapeStruct]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += area(shape)
    return accum
