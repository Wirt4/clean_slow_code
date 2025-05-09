import random

from modules.oop import Circle, Rectangle, Shape, Triangle
from modules.typeddict import ShapeType, ShapeUnion


def random_side() -> float:
    return random.uniform(1.0, 10.0)


def random_radius() -> float:
    return random.uniform(1.0, 5.0)


def random_shape_type() -> ShapeType:
    return random.choice([ShapeType.RECTANGLE, ShapeType.CIRCLE, ShapeType.TRIANGLE])


def random_shape_oop() -> Shape:
    shape: ShapeType = random_shape_type()
    if shape == ShapeType.RECTANGLE:
        return Rectangle(random_side(), random_side())
    elif shape == ShapeType.CIRCLE:
        return Circle(random_radius())
    else:
        return Triangle(random_side(), random_side())


def random_shape_typeddict() -> ShapeUnion:
    shape: ShapeType = random_shape_type()
    if shape == ShapeType.RECTANGLE:
        return {
            "shape_type": ShapeType.RECTANGLE,
            "width": random_side(),
            "height": random_side(),
        }
    elif shape == ShapeType.CIRCLE:
        radius: float = random_radius()
        return {
            "shape_type": ShapeType.CIRCLE,
            "width": 2 * radius,
            "height": 2 * radius,
        }
    else:
        return {
            "shape_type": ShapeType.TRIANGLE,
            "width": random_side(),
            "height": random_side(),
        }
