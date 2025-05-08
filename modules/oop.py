from abc import ABC, abstractmethod
from math import pi
from typing import List

"""
Object-Oriented, Clean Version
"""


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
    sum_total = 0.0
    for shape in shapes:
        sum_total += shape.area()
    return sum_total
