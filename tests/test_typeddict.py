import unittest
from math import pi

from modules.typeddict import ShapeType, ShapeUnion, get_area


class TestTypedDictMethods(unittest.TestCase):
    """
    arrangement-wise, similar to the oop so as not to hide anything in the comparison
    """

    def test_get_area_of_circle(self):
        """
        Confirm the brancing 'get_area' returns the correct circle area.
        Use the same values from the oop test
        """
        circle: ShapeUnion = {"shape_type": ShapeType.CIRCLE, "width": 2, "height": 2}
        self.assertEqual(get_area(circle), pi)

    def test_get_area_of_rectangle(self):
        """
        Confirm the branching "get_area" returns the correct rectangle area.
        Use the same values from the oop test.
        """
        rectangle: ShapeUnion = {
            "shape_type": ShapeType.RECTANGLE,
            "width": 40,
            "height": 11,
        }
        self.assertEqual(get_area(rectangle), 440)

    def test_get_area_of_triangle(self):
        """
        confirm the branching "get_area" returns the correct rectangle area.
        Use the same value from the oop test
        """
        triangle: ShapeUnion = {
            "shape_type": ShapeType.TRIANGLE,
            "width": 10,
            "height": 5,
        }
        self.assertEqual(get_area(triangle), 25)
