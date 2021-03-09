import numpy
from pyproj import CRS, Transformer

from seabed.ngdc import NGDCSeabedDescriptions


def test_surveys():
    surveys = NGDCSeabedDescriptions.all_surveys()

    assert len(surveys) > 0


def test_seabed_descriptions_within_bounds():
    bounds = numpy.array([[-77, 39], [-75, 40]])
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]
    seabed = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=bounds)

    assert seabed.data.shape[0] > 0
    assert seabed.data.shape[1] == 14
    assert len(seabed.descriptions) > 0
    assert any(seabed.data['Survey'].isin(['492']))


def test_seabed_descriptions_within_transformed_bounds():
    bounds = numpy.array([[-77, 39], [-75, 40]])
    transformed_crs = CRS.from_epsg(32618)
    transformed_bounds = numpy.ravel(
        numpy.stack(
            Transformer.from_crs(CRS.from_epsg(4326), transformed_crs).transform(bounds[:, 0], bounds[:, 1]),
            axis=1,
        )
    )
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]
    seabed = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=transformed_bounds, crs=transformed_crs)

    assert seabed.data.shape[0] > 0
    assert seabed.data.shape[1] == 14
    assert len(seabed.descriptions) > 0
    assert any(seabed.data['Survey'].isin(['492']))
