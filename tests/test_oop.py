import math
import unittest

from modules import oop


class TestOOPShapes(unittest.TestCase):
    def test_circle_area(self):
        """
        Confirms the area of the circle calculates correctly:w
        """
        radius = 1.75
        self.assertEqual(oop.Circle(radius).area(), math.pi * radius**2)

    def test_rectangle_area(self):
        """
        Confirms the area of the rectangle object calculates correctly
        """
        side_a = 40
        side_b = 11
        self.assertEqual(oop.Rectangle(side_a, side_b).area(), side_a * side_b)

    def test_triangle_area(self):
        """
        Confirms the rendered area of the triangle object
        """
        base = 10
        height = 5
        self.assertEqual(oop.Triangle(base, height).area(), base * height / 2.0)


class TestOOPMethods(unittest.TestCase):
    def test_total_area(self):
        """
        Confirms the sum total of the area of shapes in an array
        The circle's radius is 1. The rectangle is 1 x 1. The triangle has a base and height of 1 each. So the expected value is pi + 1.5
        """
        shape_list = [oop.Circle(1), oop.Rectangle(1, 1), oop.Triangle(1, 1)]
        self.assertEqual(oop.total_area(shape_list), math.pi + 1.5)

    def test_total_area_in_groups_of_4(self):
        """
        Confirms the 4-batch version gets the same results as the regular version.
        The only difference, if any, should be the number of execution cycles.
        """
        shape_list = [
            oop.Circle(1),
            oop.Rectangle(1, 1),
            oop.Triangle(1, 1),
            oop.Circle(1),
            oop.Rectangle(1, 1),
            oop.Triangle(1, 1),
        ]
        self.assertEqual(
            oop.total_area_in_groups_of_4(shape_list), oop.total_area(shape_list)
        )
