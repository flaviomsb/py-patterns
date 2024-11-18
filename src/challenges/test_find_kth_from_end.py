import inspect
import unittest

from find_kth_from_end import find_kth_from_end


class TestFindKthFromEnd(unittest.TestCase):
    def test_has_loop_is_a_function(self):
        self.assertTrue(inspect.isfunction(find_kth_from_end))
