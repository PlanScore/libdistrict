import math
from libdistrict.district import District
from osgeo import ogr, osr

"""
Spherical mercator code from: 
https://github.com/PlanScore/PlanScore/blob/07dc7b023a9547723964f1c442cc1a231948b7f4/planscore/compactness/__init__.py
"""
# Spherical mercator should work at typical district sizes
EPSG4326 = osr.SpatialReference(); EPSG4326.ImportFromEPSG(4326)
EPSG3857 = osr.SpatialReference(); EPSG3857.ImportFromEPSG(3857)
projection = osr.CoordinateTransformation(EPSG4326, EPSG3857)
"""
"""


def polsby_popper(district):

    is_district(district)
    has_geometry(district)

    geometry = district.geometry


    """
    From PlanScore Compactness/__init__.py
    """
    projected = geometry.Clone()
    projected.Transform(projection)
    boundary = projected.GetBoundary()
    geom_area = projected.GetArea()

    if boundary.GetGeometryType() in (ogr.wkbMultiLineString, ogr.wkbMultiLineString25D):
        geoms = [boundary.GetGeometryRef(i) for i in range(boundary.GetGeometryCount())]
        length = sum([geom.Length() for geom in geoms])
    else:
        length = boundary.Length()

    """
    """

    return 4 * math.pi * (geom_area / (length ** 2))


def schwartzberg(district):

    is_district(district)
    has_geometry(district)

    geometry = district.geometry


    """
    From PlanScore Compactness/__init__.py
    """
    projected = geometry.Clone()
    projected.Transform(projection)
    boundary = projected.GetBoundary()
    area = projected.GetArea()

    if boundary.GetGeometryType() in (ogr.wkbMultiLineString, ogr.wkbMultiLineString25D):
        geoms = [boundary.GetGeometryRef(i) for i in range(boundary.GetGeometryCount())]
        perimeter = sum([geom.Length() for geom in geoms])
    else:
        perimeter = boundary.Length()

    """
    """

    radius = math.sqrt(area/math.pi)
    circumference = 2*math.pi*radius
    schwartzberg_score = 1/(perimeter/circumference)

    return schwartzberg_score


def convex_hull_ratio(district):

    is_district(district)
    has_geometry(district)

    geometry = district.geometry

    projected = geometry.Clone()
    projected.Transform(projection)
    area = projected.GetArea()

    convex_hull = projected.ConvexHull().GetArea()

    return area / convex_hull


#Helper Methods for Compactness Functions
def is_district(district):
    if not isinstance(district, District):
        raise TypeError

def has_geometry(district):
    geometry = district.geometry

    if geometry is None:
        raise TypeError
