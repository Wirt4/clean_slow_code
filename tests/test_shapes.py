import unittest
import math
from modules import clean
from modules import demo


class TestShapeMethods(unittest.TestCase):
    def test_circle_areae(self):
        expected = 4 * math.pi
        radius = 2
        cleanCircle = clean.Circle(radius)
        optimizedCircle = demo.Circle(radius)
        self.assertEqual(cleanCircle.area(), expected)
        self.assertEqual(optimizedCircle.area(), expected)

    def test_square_area(self):
        expected = 4
        side = 2
        cleanSquare = clean.Square(side)
        optimizedSquare = demo.Square(side)
        self.assertEqual(cleanSquare.area(), expected)
        self.assertEqual(optimizedSquare.area(), expected)

    def test_triangle_area(self):
        expected = 6
        base = 3
        height = 4
        cleanTriangle = clean.Triangle(base, height)
        self.assertEqual(cleanTriangle.area(), expected)
