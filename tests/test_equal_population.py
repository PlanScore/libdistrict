import unittest
from district import District
from equal_population import districts_in_range

class TestEqualPopulation(unittest.TestCase):


    def test_dist_in_range(self):
        district1 = District(population=100)
        district2 = District(population=5)
        district3 = District(population=125)
        district4 = District(population=130)
        district5 = District(population=113)
        district_plan = {district1, district2, district3, district4, district5}
        max = 125
        min =100

        # districts 1, 3, 5 are in range, 2, 4 out of range
        self.assertEqual(3, districts_in_range(district_plan, min, max))