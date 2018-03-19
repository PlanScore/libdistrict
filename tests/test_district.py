import unittest
from district import District


"""
TODO write tests for the District class
"""


class TestDistrict(unittest.TestCase):

    def test_set_id(self):
        district = District(id=10)
        self.assertEqual(10, district.id)

    def test_no_id(self):
        district = District()
        self.assertTrue(district.id is None)

    def test_dict_party(self):
        party_votes = {"republican":100, "democrat":200, "other":700}
        district = District(party_votes=party_votes)
        self.assertEqual(party_votes, district.party_votes)
