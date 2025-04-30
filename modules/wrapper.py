from modules import clean
from modules import demo
from enum import Enum


class Wrapper:

    def __init__(self, module_type):
        self.shape_type = ShapeType.SQUARE
        if module_type == "clean":
            self.module = clean
        else:
            self.module = demo

    def shape_from_index(self, index):
        side_length = index % 100 + 1
        if self.shape_type == ShapeType.SQUARE:
            return self.module.Square(side_length)
        if self.shape_type == ShapeType.CIRCLE:
            return self.module.Circle(side_length)
        return self.module.Triangle(side_length, side_length)

    def next(self):
        self.shape_type = self.shape_type.next()


class ShapeType(Enum):
    SQUARE = 1
    CIRCLE = 2
    TRIANGLE = 3

    def next(self):
        value = self.value + 1
        if value > 3:
            return ShapeType(1)
        return ShapeType(value)
