import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        rec = Rectangle(width=100, height=50)
        self.assertEqual(rec.area(), 5000)
