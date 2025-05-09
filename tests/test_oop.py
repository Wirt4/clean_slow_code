import math
import unittest

from modules.oop import (
    Circle,
    Rectangle,
    Triangle,
    total_area,
    total_area_in_groups_of_4,
)


class TestOOPShapes(unittest.TestCase):
    def test_circle_area(self):
        """
        Confirms the area of the circle calculates correctly:w
        """
        radius = 1.75
        self.assertEqual(Circle(radius).area(), math.pi * radius**2)

    def test_rectangle_area(self):
        """
        Confirms the area of the rectangle object calculates correctly
        """
        side_a = 40
        side_b = 11
        self.assertEqual(Rectangle(side_a, side_b).area(), side_a * side_b)

    def test_triangle_area(self):
        """
        Confirms the rendered area of the triangle object
        """
        base = 10
        height = 5
        self.assertEqual(Triangle(base, height).area(), base * height / 2.0)


class TestOOPMethods(unittest.TestCase):
    def test_total_area(self):
        """
        Confirms the sum total of the area of shapes in an array
        The circle's radius is 1. The rectangle is 1 x 1. The triangle has a base and height of 1 each. So the expected value is pi + 1.5
        """
        shape_list = [Circle(1), Rectangle(1, 1), Triangle(1, 1)]
        self.assertEqual(total_area(shape_list), math.pi + 1.5)

    def test_total_area_in_groups_of_4(self):
        """
        Confirms the 4-batch version gets the same results as the regular version.
        The only difference, if any, should be the number of execution cycles.
        """
        shape_list = [
            Circle(1),
            Rectangle(1, 1),
            Triangle(1, 1),
            Circle(1),
            Rectangle(1, 1),
            Triangle(1, 1),
        ]
        self.assertEqual(total_area_in_groups_of_4(shape_list), total_area(shape_list))
