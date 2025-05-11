from abc import ABC, abstractmethod
from math import pi


class ShapeBase(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError("area is an abstract method")


class Square(ShapeBase):
    def __init__(self, side: float):
        self._side: float = side

    def area(self) -> float:
        return self._side**2


class Rectangle(ShapeBase):
    def __init__(self, width: float, height: float):
        self._width: float = width
        self._height: float = height

    def area(self) -> float:
        return self._width * self._height


class Triangle(ShapeBase):
    def __init__(self, base: float, height: float):
        self._base: float = base
        self._height: float = height

    def area(self) -> float:
        return self._base * self._height / 2.0


class Circle(ShapeBase):
    def __init__self(self, radius: float):
        self._radius: float = radius

    def area(self) -> float:
        return pi * self._radius**2


def total_area(shapes: list[ShapeBase]) -> float:
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    # read the list of shapes
    total_area([])
