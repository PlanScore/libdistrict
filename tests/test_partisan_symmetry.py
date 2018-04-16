import unittest
from libdistrict.district import District
from libdistrict.partisan_symmetry import efficiency_gap, mean_median_diff


class TestEfficiencyGap(unittest.TestCase):

    def setUp(self):

        # District example from https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2457468
        district1 = District(id=1, party_votes={'partyA': 70, 'partyB': 30})
        district2 = District(id=2, party_votes={'partyA': 70, 'partyB': 30})
        district3 = District(id=3, party_votes={'partyA': 70, 'partyB': 30})
        district4 = District(id=4, party_votes={'partyA': 54, 'partyB': 46})
        district5 = District(id=5, party_votes={'partyA': 54, 'partyB': 46})
        district6 = District(id=6, party_votes={'partyA': 54, 'partyB': 46})
        district7 = District(id=7, party_votes={'partyA': 54, 'partyB': 46})
        district8 = District(id=8, party_votes={'partyA': 54, 'partyB': 46})
        district9 = District(id=9, party_votes={'partyA': 35, 'partyB': 65})
        district10 = District(id=10, party_votes={'partyA': 35, 'partyB': 65})
        self.district_plan = {district1, district2, district3, district4, district5, 
                                district6, district7, district8, district9, district10}

        self.key_a = 'partyA'
        self.key_b = 'partyB'

    def test_EG_positive_result(self):
        gap = efficiency_gap(self.district_plan, self.key_a, self.key_b)

        # partyA has a +20% efficiency gap
        self.assertEqual(0.2, gap)

    def test_EG_negative_result(self):
        gap = efficiency_gap(self.district_plan, self.key_b, self.key_a)

        # partyB has a -20% efficiency gap
        self.assertEqual(-0.2, gap)

    def test_EG_None_district_plan(self):
        districtNone = None

        with self.assertRaises(TypeError):
            efficiency_gap(districtNone, self.key_a, self.key_b)

    def test_EG_bad_district_plan(self):
        district1 = District(id=1, party_votes={'partyA': 70, 'partyB': 30})
        district2 = District(id=2, party_votes={'partyA': 70, 'partyB': 30})
        district_plan = {district1, "not a district", district2}

        with self.assertRaises(TypeError):
            efficiency_gap(district_plan, self.key_a, self.key_b)

class TestMeanMedianDifference(unittest.TestCase):

    def setUp(self):

        # District example from https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2457468
        district1 = District(id=1, party_votes={'partyA': 70, 'partyB': 30})
        district2 = District(id=2, party_votes={'partyA': 70, 'partyB': 30})
        district3 = District(id=3, party_votes={'partyA': 70, 'partyB': 30})
        district4 = District(id=4, party_votes={'partyA': 54, 'partyB': 46})
        district5 = District(id=5, party_votes={'partyA': 54, 'partyB': 46})
        district6 = District(id=6, party_votes={'partyA': 54, 'partyB': 46})
        district7 = District(id=7, party_votes={'partyA': 54, 'partyB': 46})
        district8 = District(id=8, party_votes={'partyA': 54, 'partyB': 46})
        district9 = District(id=9, party_votes={'partyA': 35, 'partyB': 65})
        district10 = District(id=10, party_votes={'partyA': 35, 'partyB': 65})
        self.district_plan = {district1, district2, district3, district4, district5,
                                district6, district7, district8, district9, district10}


        # District example from PlanScore
        district11 = District(id=11, party_votes={'partyA': 6, 'partyB': 5})
        district12 = District(id=12, party_votes={'partyA': 6, 'partyB': 5})
        district13 = District(id=13, party_votes={'partyA': 4, 'partyB': 5})
        district14 = District(id=14, party_votes={'partyA': 4, 'partyB': 8})
        district15 = District(id=15, party_votes={'partyA': 4, 'partyB': 8})

        self.district_plan_2 = {district11, district12, district13, district14, district15}

        self.key_a = 'partyA'
        self.key_b = 'partyB'

    def test_mmd_party_a_disadvantage(self):

        self.assertAlmostEqual(-.01, mean_median_diff(self.district_plan, self.key_a, self.key_b), places=10)

    def test_mmd_party_b_advantage(self):

        self.assertAlmostEqual(.01, mean_median_diff(self.district_plan, self.key_b, self.key_a), places=10)

    def test_mmd_no_advantage(self):

        self.assertAlmostEqual(0, mean_median_diff(self.district_plan_2, self.key_a, self.key_b), places=2)

    def test_mmd_none_district_plan(self):

        district_none = None

        with self.assertRaises(TypeError):
            mean_median_diff(district_none, self.key_a, self.key_b)

    def test_mmd_bad_district_plan(self):

        district1 = District(id=1, party_votes={'partyA': 70, 'partyB': 30})
        district2 = District(id=2, party_votes={'partyA': 70, 'partyB': 30})
        district_plan = {district1, "not a district", district2}

        with self.assertRaises(TypeError):
            mean_median_diff(district_plan, self.key_a, self.key_b)
