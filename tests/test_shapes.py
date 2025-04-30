import unittest
import math
from modules import clean


class TestShapeMethods(unittest.TestCase):
    def test_circle_areae(self):
        expected = 4 * math.pi
        cleanCircle = clean.Circle(2)
        self.assertEqual(cleanCircle.area(), expected)
