import unittest

from user import User


class TestUser(unittest.TestCase):
    def test_get_name(self):
        _user = User(name="John Doe", uuid=5793238)
        self.assertEqual(_user.get_name(), "John Doe")

    def test_set_name(self):
        _user = User(name="Jane Doe", uuid=198795)
        self.assertEqual(_user.get_name(), "Jane Doe")
        _user.set_name(name="Jane Louise Doe")
        self.assertEqual(_user.get_name(), "Jane Louise Doe")

    def test_uuid(self):
        _user = User(name="Thomas Doe", uuid=38292)
        self.assertEqual(_user.uuid, "00038292")

    def test_display_name(self):
        _user = User(name="Paul Doe", uuid=212392)
        self.assertEqual(_user.display_name(), "Paul Doe (000212392)")
