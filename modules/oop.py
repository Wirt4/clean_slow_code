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


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def total_area_oop(shapes: List[Shape]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += shape.area()
        return accum
