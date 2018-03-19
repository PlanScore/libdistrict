import unittest
from district import District


"""
TODO write tests for the District class
"""


class TestDistrict(unittest.TestCase):

    def test_set_id(self):
        district = District(id=10)
        self.assertEqual(district.id, 10)

    def test_no_id(self):
        district = District()
        self.assertTrue(district.id is None)