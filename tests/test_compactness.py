import unittest
import math
from osgeo import ogr
from district import District
from compactness import polsby_popper

class TestPolsbyPopper(unittest.TestCase):

    def test_polsby_popper_not_district(self):

        district = None

        with self.assertRaises(TypeError):
            polsby_popper(district)

    def test_polsby_popper_no_geometry(self):

        district = District()

        with self.assertRaises(TypeError):
            polsby_popper(district)

    def test_polsby_popper_not_geometry(self):

        not_geometry = "Not a geometry"

        district = District(id=id, geometry=not_geometry)

        with self.assertRaises(AttributeError):
            polsby_popper(district)


    def test_polsby_popper_square(self):

        # A square around Lake Merritt: From PlanScore
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-122.2631266, 37.7987797], [-122.2631266, 37.8103489], [-122.2484841, 37.8103489], [-122.2484841, 37.7987797], [-122.2631266, 37.7987797]]]}')

        district = District(geometry=geom)

        self.assertAlmostEqual(math.pi/4, polsby_popper(district), places=5)


    def test_polsby_popper_line(self):

        # A thin line through Lake Merritt: From PlanScore
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-122.2631266, 37.804111], [-122.2631266, 37.804112], [-122.2484841, 37.804112], [-122.2484841, 37.804111], [-122.2631266, 37.804111]]]}')

        district = District(geometry = geom)

        self.assertAlmostEqual(0., polsby_popper(district), places=3)

