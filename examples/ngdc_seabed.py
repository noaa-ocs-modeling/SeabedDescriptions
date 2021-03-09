import numpy
from pyproj import CRS, Transformer

from seabed.ngdc import NGDCSeabedDescriptions

CRS = CRS.from_epsg(32618)

BOUNDS = numpy.array([[-77, 39], [-75, 40]])
BOUNDS = numpy.ravel(
    numpy.stack(
        Transformer.from_crs(CRS.from_epsg(4326), CRS).transform(BOUNDS[:, 0], BOUNDS[:, 1]),
        axis=1,
    )
)

if __name__ == '__main__':
    surveys = NGDCSeabedDescriptions.all_surveys()[:5]
    seabed = NGDCSeabedDescriptions(bounds=BOUNDS, surveys=surveys, crs=CRS)
