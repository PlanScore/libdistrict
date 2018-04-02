import unittest
import math
from osgeo import ogr
from district import District
from compactness import polsby_popper, schwartzberg, is_district, has_geometry

class TestHelperMethods(unittest.TestCase):

    def test_not_district(self):

        district = None

        with self.assertRaises(TypeError):
            is_district(district)

    def test_no_geometry(self):

        district = District()

        with self.assertRaises(TypeError):
            has_geometry(district)

    def test_not_geometry(self):

        not_geometry = "Not a geometry"

        district = District(id=id, geometry=not_geometry)

        with self.assertRaises(AttributeError):
            has_geometry(district)


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


    def test_polsby_popper_square_4326(self):

        # A square around Lake Merritt: From PlanScore
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-122.2631266, 37.7987797], [-122.2631266, 37.8103489], [-122.2484841, 37.8103489], [-122.2484841, 37.7987797], [-122.2631266, 37.7987797]]]}')

        district = District(geometry=geom)

        self.assertAlmostEqual(math.pi/4, polsby_popper(district), places=5)


    def test_polsby_popper_line_4326(self):

        # A thin line through Lake Merritt: From PlanScore
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-122.2631266, 37.804111], [-122.2631266, 37.804112], [-122.2484841, 37.804112], [-122.2484841, 37.804111], [-122.2631266, 37.804111]]]}')

        district = District(geometry = geom)

        self.assertAlmostEqual(0., polsby_popper(district), places=3)


    def test_polsby_popper_square_3857(self):

        # A square around Lake Winnebago
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-9839815.088179024,5505529.83629639],[-9881396.831566159,5468840.062719505],[-9844707.057989275,5427258.31933237],[-9803125.31460214,5463948.092909254],[-9839815.088179024,5505529.83629639]]]}')

        district = District(geometry=geom)

        self.assertAlmostEqual(math.pi/4, polsby_popper(district), places=5)


    def test_polsby_popper_triangle_3857(self):

        # An equilateral triangle around Lake Mendota
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-9942183.378309947,5335705.868703798],[-9966678.038775941,5335248.39511508],[-9954034.524793552,5314264.133688814],[-9942183.378309947,5335705.868703798]]]}')

        district = District(geometry=geom)
        triangle_score = (4.0*math.pi) * ((math.sqrt(3.0)/4.0)/9.0)

        self.assertAlmostEqual(triangle_score, polsby_popper(district), places=5)
        

class TestSchwartzberg(unittest.TestCase):

    def test_schwartzberg_square_4326(self):

        # A square around Lake Merritt: From PlanScore
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-122.2631266, 37.7987797], [-122.2631266, 37.8103489], [-122.2484841, 37.8103489], [-122.2484841, 37.7987797], [-122.2631266, 37.7987797]]]}')

        district = District(geometry=geom)

        radius = math.sqrt(1/math.pi)

        circumference = 2*math.pi*radius

        schwartzberg_score = 1/(4/circumference)

        self.assertAlmostEqual(schwartzberg_score, schwartzberg(district), places=5)

    def test_schwartzberg_square_3857(self):

        # A square around Lake Winnebago
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-9839815.088179024,5505529.83629639],[-9881396.831566159,5468840.062719505],[-9844707.057989275,5427258.31933237],[-9803125.31460214,5463948.092909254],[-9839815.088179024,5505529.83629639]]]}')

        district = District(geometry=geom)

        radius = math.sqrt(1/math.pi)

        circumference = 2*math.pi*radius

        schwartzberg_score = 1/(4/circumference)

        self.assertAlmostEqual(schwartzberg_score, schwartzberg(district), places=5)

    def test_schwartzberg_triangle_3857(self):

        # An equilateral triangle around Lake Mendota
        geom = ogr.CreateGeometryFromJson('{"type": "Polygon", "coordinates": [[[-9942183.378309947,5335705.868703798],[-9966678.038775941,5335248.39511508],[-9954034.524793552,5314264.133688814],[-9942183.378309947,5335705.868703798]]]}')

        district = District(geometry=geom)

        area_of_triangle = math.sqrt(3)/4

        radius = math.sqrt(area_of_triangle/math.pi)

        circumference = 2*math.pi*radius

        schwartzberg_score = 1/(3/circumference)
        
        self.assertAlmostEqual(schwartzberg_score, schwartzberg(district), places=5)
 