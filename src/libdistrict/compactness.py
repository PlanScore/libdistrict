import math
from district import District
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

    check_if_district(district)
    check_if_has_geometry(district)

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


"""
Helper Methods for Compactness Functions
"""
def check_if_district(district):
    if not isinstance(district, District):
        raise TypeError

def check_if_has_geometry(district):
    geometry = district.geometry

    if geometry is None:
        raise TypeError
