from abc import ABC, abstractmethod
from math import pi


class ShapeBase(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError("area is an abstract method")

    @abstractmethod
    def corner_count(self) -> int:
        raise NotImplementedError("corner_count is an abstract method")

    def weighted_corner_area(self) -> float:
        return 1.0 / (1.0 + self.corner_count() * self.area())


class Square(ShapeBase):
    def __init__(self, side: float):
        self._side: float = side

    def area(self) -> float:
        return self._side**2

    def corner_count(self) -> int:
        return 4


class Rectangle(ShapeBase):
    def __init__(self, width: float, height: float):
        self._width: float = width
        self._height: float = height

    def area(self) -> float:
        return self._width * self._height

    def corner_count(self) -> int:
        return 4


class Triangle(ShapeBase):
    def __init__(self, base: float, height: float):
        self._base: float = base
        self._height: float = height

    def area(self) -> float:
        return self._base * self._height / 2.0

    def corner_count(self) -> int:
        return 3


class Circle(ShapeBase):
    def __init__(self, radius: float):
        self._radius: float = radius

    def area(self) -> float:
        return pi * self._radius**2

    def corner_count(self) -> int:
        return 0


def total_area(shapes: list[ShapeBase]) -> float:
    return sum(shape.area() for shape in shapes)


def total_corner_weighted_area(shapes: list[ShapeBase]) -> float:
    return sum(shape.weighted_corner_area() for shape in shapes)


def shape_factory(specs: list[str]) -> ShapeBase:
    if specs[0] == "square":
        return Square(float(specs[1]))
    if specs[0] == "rectangle":
        return Rectangle(float(specs[1]), float(specs[2]))
    if specs[0] == "circle":
        return Circle(float(specs[1]))
    if specs[0] == "triangle":
        return Triangle(float(specs[1]), float(specs[2]))
    else:
        raise ValueError("invalid shape type")


def read_profiles_to_shapes(filename: str) -> list[ShapeBase]:
    shapes: list[ShapeBase] = []
    with open(filename, "r") as f:
        for line in f:
            shapes.append(shape_factory(line.strip().split()))
    return shapes


if __name__ == "__main__":
    # read the list of shapes
    shapes: list[ShapeBase] = read_profiles_to_shapes("shapes.txt")
    total_area(shapes)
    total_corner_weighted_area(shapes)
