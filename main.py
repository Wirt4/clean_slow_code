import random
import cProfile
import math
from typing import List, Literal, TypedDict, Union
from abc import ABC, abstractmethod

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
        return math.pi * self.radius**2


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


def random_shape_oop() -> Shape:
    shape = random.choice(["rectangle", "circle", "triangle"])
    if shape == "rectangle":
        return Rectangle(random.uniform(1.0, 10.0), random.uniform(1.0, 10.0))
    elif shape == "circle":
        return Circle(random.uniform(1.0, 5.0))
    else:
        return Triangle(random.uniform(1.0, 10.0), random.uniform(1.0, 10.0))


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


ShapeStruct = Union[RectangleStruct, CircleStruct]


def area(shape: ShapeStruct) -> float:
    if shape["type"] == "rectangle":
        return shape["width"] * shape["height"]
    elif shape["type"] == "circle":
        return math.pi * shape["radius"] ** 2
    elif shape["type"] == "triangle":
        return 0.5 * shape["base"] * shape["height"]
    else:
        raise ValueError("Unknown shape")


def total_area_struct(shapes: List[ShapeStruct]) -> float:
    accum = 0.0
    for shape in shapes:
        accum += area(shape)
    return accum


def random_shape_struct() -> ShapeStruct:
    shape = random.choice(["rectangle", "circle", "triangle"])
    if shape == "rectangle":
        return {
            "type": "rectangle",
            "width": random.uniform(1.0, 10.0),
            "height": random.uniform(1.0, 10.0),
        }
    elif shape == "circle":
        return {"type": "circle", "radius": random.uniform(1.0, 5.0)}
    else:
        return {
            "type": "triangle",
            "base": random.uniform(1.0, 10),
            "height": random.uniform(1.0, 10.0),
        }


# ----- Profiling Functions -----
def run_oop():
    shapes = [random_shape_oop() for _ in range(100000)]
    total_area_oop(shapes)


def run_struct():
    shapes = [random_shape_struct() for _ in range(100000)]
    total_area_struct(shapes)


# ----- Main entry point -----
if __name__ == "__main__":
    print("OOP Version:")
    cProfile.run("run_oop()", sort="cumtime")

    print("\nFlat Struct Version:")
    cProfile.run("run_struct()", sort="cumtime")
