import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        rec = Rectangle(width=100, height=50)
        self.assertEqual(rec.area(), 5000)

    def test_repr(self):
        rec = Rectangle(width=120, height=80)
        self.assertEqual(repr(rec), "Rectangle w/ area {0}".format(rec.area()))

    def test_dunder_eq(self):
        self.assertEqual(Rectangle(130, 50), Rectangle(130, 50))
        self.assertNotEqual(Rectangle(120, 40), Rectangle(120.001, 40.001))

    def test_dunder_gt(self):
        self.assertGreater(Rectangle(41.223, 32.433), Rectangle(41.222, 32.432))
