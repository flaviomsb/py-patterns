import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_display_name(self):
        emp = Employee(name="Paul Doe", uuid=212392, role="Manager")
        self.assertEqual(emp.display_name(), "Paul Doe (000212392) - Manager")
