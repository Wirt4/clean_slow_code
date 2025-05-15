from enum import Enum
from math import pi


class ShapeType(Enum):
    SQUARE = "square"
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    TRIANGLE = "triangle"


class ShapeUnion:
    def __init__(self, shape_type: ShapeType, width: str, height: str):
        self.shape_type: ShapeType = shape_type
        self.width: float = float(width)
        self.height: float = float(height)


COEFFICIENT_TABLE: dict = {
    ShapeType.SQUARE: 1.0,
    ShapeType.RECTANGLE: 1.0,
    ShapeType.CIRCLE: pi,
    ShapeType.TRIANGLE: 0.5,
}


def get_area(shape: ShapeUnion) -> float:
    return shape.width * shape.height * COEFFICIENT_TABLE[shape.shape_type]


CORNER_TABLE: dict = {
    ShapeType.SQUARE: 4,
    ShapeType.RECTANGLE: 4,
    ShapeType.CIRCLE: 0,
    ShapeType.TRIANGLE: 3,
}


def get_corner_count(shape: ShapeUnion) -> int:
    return CORNER_TABLE[shape.shape_type]


def total_area(shapes: list[ShapeUnion]) -> float:
    return sum(get_area(shape) for shape in shapes)


CORNER_COEFFICIENT_TABLE: dict = {
    ShapeType.SQUARE: 0.2,
    ShapeType.RECTANGLE: 0.2,
    ShapeType.CIRCLE: 1.0,
    ShapeType.TRIANGLE: 0.25,
}


def get_corner_weighted_area(shape: ShapeUnion) -> float:
    return CORNER_COEFFICIENT_TABLE[shape.shape_type] * (get_area(shape) ** -1)


def total_corner_weighted_area(shapes: list[ShapeUnion]) -> float:
    return sum(get_corner_weighted_area(shape) for shape in shapes)


def specs_to_shape(specs: list[str]) -> ShapeUnion:
    if specs[0] == "square":
        return ShapeUnion(ShapeType.SQUARE, specs[1], specs[1])
    elif specs[0] == "rectangle":
        return ShapeUnion(ShapeType.RECTANGLE, specs[1], specs[2])
    elif specs[0] == "circle":
        return ShapeUnion(ShapeType.SQUARE, specs[1], specs[1])
    elif specs[0] == "triangle":
        return ShapeUnion(ShapeType.TRIANGLE, specs[1], specs[2])
    else:
        raise ValueError("invalid shape type")


def read_profiles_to_shapes(filename: str) -> list[ShapeUnion]:
    shapes: list[ShapeUnion] = []
    with open(filename, "r") as f:
        for line in f:
            shapes.append(specs_to_shape(line.strip().split()))
    return shapes


if __name__ == "__main__":
    # read the list of shapes
    shapes: list[ShapeUnion] = read_profiles_to_shapes("shapes.txt")
    total_area(shapes)
    total_corner_weighted_area(shapes)
