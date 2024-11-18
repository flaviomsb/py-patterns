import inspect
import unittest

from find_middle_node import find_middle_node


class TestFindMiddleNode(unittest.TestCase):
    def test_has_loop_is_a_function(self):
        self.assertTrue(inspect.isfunction(find_middle_node))
