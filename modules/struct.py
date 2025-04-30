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
    width: float
    height: float


class TriangleStruct(TypedDict):
    type: Literal["triangle"]
    height: float
    width: float


ShapeStruct = Union[RectangleStruct, CircleStruct, TriangleStruct]


def area(shape: ShapeStruct) -> float:
    if shape["type"] == "rectangle":
        return shape["width"] * shape["height"]
    elif shape["type"] == "circle":
        return pi * shape["radius"] ** 2
    elif shape["type"] == "triangle":
        return 0.5 * shape["width"] * shape["height"]
    else:
        raise ValueError("Unknown shape")


def corner_count(shape: ShapeStruct) -> float:
    if shape["type"] == "rectangle":
        return 4
    elif shape["type"] == "circle":
        return 0
    elif shape["type"] == "triangle":
        return 3
    else:
        raise ValueError("Unknown shape")


def total_area_struct(shapes: List[ShapeStruct]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += area(shape)
    return accum


coeffient_table = {"rectangle": 1.0, "triangle": 0.5, "circle": pi}


def get_area_union(shape: ShapeStruct):
    return coeffient_table[shape["type"]] * shape["width"] * shape["height"]


def total_corner_weighted_area_struct(shapes: List[ShapeStruct]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += get_area_union(shape)
