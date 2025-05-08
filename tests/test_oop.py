import math
import unittest

from modules import oop


class TestOOPShapes(unittest.TestCase):
    def test_circle_area(self):
        """
        Confirms the area of the circle calculates correctly
        """
        radius = 1.75
        expected_area = math.pi * radius**2
        oop_circle = oop.Circle(radius)
        self.assertEqual(oop_circle.area(), expected_area)

    def test_rectangle_area(self):
        """
        Confirms the area of the rectangle object calculates correctly
        """
        side_a = 40
        side_b = 11
        expected_area = 440
        self.assertEqual(oop.Rectangle(side_a, side_b).area(), expected_area)
