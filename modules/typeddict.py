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


def get_area(shape: ShapeUnion):
    if shape["shape_type"] == ShapeType.CIRCLE:
        return pi * (shape["width"] / 2.0) ** 2
    return shape["width"] * shape["height"]


class Shape(ABC):
    """
    Abstract class for various polygon shapes, not for direct implementation
    """

    @abstractmethod
    def area(self) -> float:
        """
        abstract method for area of any shape
        """
        raise ValueError("not implemented")

    @abstractmethod
    def corner_count(self) -> int:
        """
        abstract method for corner count of any shape
        """
        raise ValueError("not implemented")


class Rectangle(Shape):
    """
    Rectangle shape
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Area of rectangle: base * height
        """
        return self.width * self.height

    def corner_count(self) -> int:
        """
        Most rectangles have four corners. This one has 4 as well.
        """
        return 4


class Circle(Shape):
    """
    circle shape
    """

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """
        The area of a circle: Currently depends on math library for pi
        """
        return pi * self.radius**2

    def corner_count(self) -> int:
        """
        I tried to find circles with corners, but I haven't found one yet
        """
        return 0


class Triangle(Shape):
    """
    Triangle Shape
    """

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        """
        Like most triangles, this is 1/2 * base * height
        """
        return 0.5 * self.base * self.height

    def corner_count(self) -> int:
        """
        Triangle have three corners, aren't you glad you know that?
        """
        return 3


def total_corner_weighted_areas_oop(shapes: List[Shape]) -> float:
    """
    get the sum total of corner weighted areas where the weighted area is 1 + (number of corners* area)
    """
    accum: int = 0.0
    for shape in shapes:
        accum += (1.0 / (1.0 + shape.corner_count())) * shape.area()
    return accum


def total_area(shapes: List[Shape]) -> float:
    """
    Returns the sum total area of all shapes in the list
    """
    sum_total: float = 0.0
    for i in range(len(shapes)):
        sum_total += shapes[i].area()
    return sum_total


def total_area_in_groups_of_4(shapes: List[Shape]) -> float:
    """
    Returns the sum total area of all shapes in the list.
    The iteration is batched in groups of 4
    """
    accum_0: float = 0.0
    accum_1: float = 0.0
    accum_2: float = 0.0
    accum_3: float = 0.0
    for i in range(0, len(shapes), 4):
        accum_0 += 0 if i >= len(shapes) else shapes[i].area()
        accum_1 += 0 if i + 1 >= len(shapes) else shapes[i + 1].area()
        accum_2 += 0 if i + 2 >= len(shapes) else shapes[i + 2].area()
        accum_3 += 0 if i + 3 >= len(shapes) else shapes[i + 3].area()
    return accum_0 + accum_1 + accum_2 + accum_3
