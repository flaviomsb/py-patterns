import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        cir = Circle(radius=58.9)
        self.assertAlmostEqual(cir.area(), 10898.844649760247)

    def test_radius_type_in_setter(self):
        with self.assertRaises(TypeError):
            Circle(radius="hello")

    def test_radius_value_in_setter(self):
        with self.assertRaises(ValueError):
            Circle(radius=-10.2)

    def test_repr(self):
        cir = Circle(radius=54.2)
        self.assertEqual(repr(cir), "Circle w/ area {0}".format(cir.area()))

    def test_dunder_eq(self):
        self.assertEqual(Circle(radius=10), Circle(radius=10))
        self.assertNotEqual(Circle(radius=10.2), Circle(radius=10.1))

    def test_dunder_gt(self):
        self.assertGreater(Circle(radius=43.23), Circle(radius=42))
