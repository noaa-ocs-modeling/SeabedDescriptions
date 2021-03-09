import numpy

from seabed.ngdc import NGDCSeabedDescriptions

if __name__ == '__main__':
    # define bounds
    bounds = numpy.array([[-77, 39], [-75, 40]])

    # retrieve a list of the first 5 surveys
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]

    # get surveys within specific bounds
    seabed_object = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=bounds)
    surveys_within_bounds = seabed_object.surveys

    print(f'all surveys: {first_5_surveys}')
    print(f'surveys within transformed bounds: {surveys_within_bounds}')
