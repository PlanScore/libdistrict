import unittest
from district import District
from equal_population import districts_in_range, districts_in_percent_deviation


class TestEqualPopulation(unittest.TestCase):

    def setUp(self):
        district1 = District(population=100)
        district2 = District(population=130)
        district3 = District(population=125)
        district4 = District(population=110)
        district5 = District(population=90)
        self.district_plan = {district1, district2, district3, district4, district5}

    def test_dist_in_range(self):
        max_target = 125
        min_target = 100

        # districts 1, 3, 4 are in range and 2, 5 are out of range
        self.assertEqual(3, districts_in_range(self.district_plan, min_target, max_target))

    def test_dist_in_percent_dev(self):
        percent_deviation = 10

        # districts 1, 4 are in percent deviation and 2, 3, 5 are not
        self.assertEqual(2, districts_in_percent_deviation(self.district_plan, percent_deviation))


