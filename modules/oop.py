from typing import List
from abc import ABC, abstractmethod
from math import pi

"""
Object-Oriented, Clean Version
"""


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def corner_count(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def corner_count(self) -> int:
        return 4


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2

    def corner_count(self) -> int:
        return 0


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def corner_count(self) -> int:
        return 3


def total_area_oop(shapes: List[Shape]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += shape.area()
        return accum


"""
get the sum total of corner weighted areas
"""


def total_corner_weighted_areas_oop(shapes: List[Shape]) -> float:
    accum: int = 0.0
    for shape in shapes:
        accum += (1.0 / (1.0 + shape.corner_count())) * shape.area()
    return accum
