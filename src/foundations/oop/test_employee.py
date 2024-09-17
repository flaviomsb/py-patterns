import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_display_name(self):
        emp = Employee(name="Paul Doe", uuid=212392, role="Manager")
        self.assertEqual(emp.display_name(), "Paul Doe (000212392) - Manager")

    def test_company_as_class_method(self):
        self.assertEqual(Employee.company(), "Patterns corp")

    def test_work_schedule(self):
        self.assertEqual(Employee.work_schedule(), "40 hours / week")

    def test_str_dunder(self):
        self.assertEqual(
            str(Employee(name="Paul Doe", uuid=212392, role="Systems Engineer")),
            "Employee with name Paul Doe and uuid 000212392 with role Systems Engineer",
        )
