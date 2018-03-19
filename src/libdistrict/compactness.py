import math
from district import District
from osgeo import ogr, osr


def polsby_popper(district):
    if isinstance(district, District):
        geometry = district.geometry

        # TODO implement polsby popper here

    else:
        raise TypeError