import abc
import random
import sys
from enum import Enum, auto


def random_side() -> float:
    return random.uniform(1.0, 10.0)


def random_radius() -> float:
    return random.uniform(1.0, 5.0)


class ShapeGenerator(abc.ABC):
    def generate(self) -> str:
        raise NotImplementedError


class SquareGenerator(ShapeGenerator):
    def generate(self) -> str:
        return f"square {random_side()}"


class RectangleGenerator(ShapeGenerator):
    def generate(self) -> str:
        return f"rectangle {random_side()} {random_side()}"


class CircleGenerator(ShapeGenerator):
    def generate(self) -> str:
        return f"circle {random_radius()}"


class TriangleGenerator(ShapeGenerator):
    def generate(self) -> str:
        return f"triangle {random_side()} {random_side()}"


class ShapeTypes(Enum):
    SQUARE = auto()
    RECTANGLE = auto()
    CIRCLE = auto()
    TRIANGLE = auto()


def generator_factory(shape_type: ShapeTypes):
    if shape_type == ShapeTypes.SQUARE:
        return SquareGenerator()
    elif shape_type == ShapeTypes.RECTANGLE:
        return RectangleGenerator()
    elif shape_type == ShapeTypes.CIRCLE:
        return CircleGenerator()
    elif shape_type == ShapeTypes.TRIANGLE:
        return TriangleGenerator()
    else:
        raise ValueError("invalid shape type")


def write_a_random_shape(file_writer):
    generator = generator_factory(random.choice(list(ShapeTypes)))
    file_writer.write(generator.generate() + "\n")


def print_random_shapes(file_writer, number_of_shapes):
    for _ in range(number_of_shapes):
        write_a_random_shape(file_writer)


if __name__ == "__main__":
    number_of_shapes: int = int(sys.argv[1])
    with open("shapes.txt", "w") as f:
        print_random_shapes(f, number_of_shapes)
