import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        cir = Circle(radius=58.9)
        self.assertAlmostEqual(cir.area(), 10898.844649760247)
