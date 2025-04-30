import math


class Shape:
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height / 2


"""
Listing 23
"""


def compute_total_area_polymorphism(shape_count, shapes):
    accumulator = 0.0
    for shape_index in range(shape_count):
        accumulator += shapes[shape_index].area()
    return accumulator
