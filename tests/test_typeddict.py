import unittest
from math import pi

from modules.typeddict import ShapeType, ShapeUnion, get_area


class TestTypedDictMethods(unittest.TestCase):
    """
    arrangement-wise, similar to the oop so as not to hide anything in the comparison
    """

    def test_get_area_of_circle(self):
        """
        Confirm 'get_area_branching' returns the correct circle area.
        Use the same values from the oop test
        """
        circle: ShapeUnion = {"shape_type": ShapeType.CIRCLE, "width": 2, "height": 2}
        self.assertEqual(get_area(circle), pi)
