import random

from modules.oop import Circle, Rectangle, Shape, Triangle
from modules.struct import ShapeStruct


def random_side() -> float:
    return random.uniform(1.0, 10.0)


def random_radius() -> float:
    return random.uniform(1.0, 5.0)


def random_shape_oop() -> Shape:
    shape: str = random.choice(["rectangle", "circle", "triangle"])
    if shape == "rectangle":
        return Rectangle(random_side(), random_side())
    elif shape == "circle":
        return Circle(random_radius())
    else:
        return Triangle(random_side(), random_side())


def random_shape_struct() -> ShapeStruct:
    shape = random.choice(["rectangle", "circle", "triangle"])
    if shape == "rectangle":
        return {
            "type": "rectangle",
            "width": random_side(),
            "height": random_side(),
        }
    elif shape == "circle":
        radius = random_radius()
        return {
            "type": "circle",
            "radius": radius,
            "width": 2 * radius,
            "height": 2 * radius,
        }
    else:
        return {
            "type": "triangle",
            "width": random_side(),
            "height": random_side(),
        }
