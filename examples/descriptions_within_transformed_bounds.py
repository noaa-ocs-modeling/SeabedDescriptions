import numpy
from pyproj import CRS, Transformer

from seabed.ngdc import NGDCSeabedDescriptions

if __name__ == '__main__':
    # define bounds
    bounds = numpy.array([[-77, 39], [-75, 40]])

    # transform bounds to desired CRS
    source_crs = CRS.from_epsg(4326)
    transformed_crs = CRS.from_epsg(32618)
    transformed_bounds = numpy.ravel(
        numpy.stack(
            Transformer.from_crs(source_crs, transformed_crs).transform(bounds[:, 0], bounds[:, 1]),
            axis=1,
        )
    )

    # retrieve a list of the first 5 surveys
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]

    # get surveys within specific bounds
    seabed_object = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=transformed_bounds, crs=transformed_crs)
    surveys_within_bounds = seabed_object.surveys

    print(f'all surveys: {first_5_surveys}')
    print(f'surveys within transformed bounds: {surveys_within_bounds}')
