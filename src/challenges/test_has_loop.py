import inspect
import unittest

from has_loop import has_loop


class TestHasLoop(unittest.TestCase):
    def test_has_loop_is_a_function(self):
        self.assertTrue(inspect.isfunction(has_loop))
