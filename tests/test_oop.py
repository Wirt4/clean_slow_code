import math
import unittest

from modules import oop


class TestOOPShapes(unittest.TestCase):
    def test_circle_area(self):
        """
        Confirms the area of the circle calculates correctly
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
