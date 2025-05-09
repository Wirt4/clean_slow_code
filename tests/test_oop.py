import unittest
from math import pi

from modules.oop import (
    Circle,
    Rectangle,
    Triangle,
    total_area,
    total_area_in_groups_of_four,
    total_corner_area,
    total_corner_area_in_groups_of_four,
)


class TestOOPShapes(unittest.TestCase):
    def test_circle_area(self):
        """
        Confirms the area of the circle calculates correctly:w
        """
        radius = 1.75
        self.assertEqual(Circle(radius).area(), pi * radius**2)

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

    def test_circle_corner_count(self):
        """
        A circle has no corners
        """
        self.assertEqual(Circle(1).corner_count(), 0)

    def test_rectangle_corner_count(self):
        """
        Four corners for a rectangle
        """
        self.assertEqual(Rectangle(3, 4).corner_count(), 4)

    def test_triangle_corner_count(self):
        """
        My triangle has three corners. Three corners has my triangle.
        """
        self.assertEqual(Triangle(3, 4).corner_count(), 3)


class TestOOPMethods(unittest.TestCase):
    def test_total_area(self):
        """
        Confirms the sum total of the area of shapes in an array
        The circle's radius is 1. The rectangle is 1 x 1. The triangle has a base and height of 1 each. So the expected value is pi + 1.5
        """
        shape_list = [Circle(1), Rectangle(1, 1), Triangle(1, 1)]
        self.assertEqual(total_area(shape_list), pi + 1.5)

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
        self.assertEqual(
            total_area_in_groups_of_four(shape_list), total_area(shape_list)
        )

    def test_total_corner_area(self):
        """
        confirms that the method sums up the values of 1/(1 + (shape.cornercount * shape.area))
        """
        shape_list = [
            Circle(1),  # 1
            Rectangle(1, 1),  # 0.2
            Triangle(2, 1),  # 0.25
            Circle(1),  # 1
            Rectangle(1, 1),  # 0.04
            Triangle(1, 2),  # 0.25
        ]
        self.assertAlmostEqual(total_corner_area(shape_list), 2.9)

    def test_total_corner_area_groups_of_four(self):
        """
        confirms that the methods for summing up the weighted corner areas do the same work
        """
        shape_list = [
            Circle(1),  # 1
            Rectangle(1, 1),  # 0.2
            Triangle(2, 1),  # 0.25
            Circle(1),  # 1
            Rectangle(1, 1),  # 0.04
            Triangle(1, 2),  # 0.25
        ]
        self.assertAlmostEqual(total_corner_area_in_groups_of_four(shape_list), 2.9)
