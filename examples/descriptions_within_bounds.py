import numpy

from seabed.ngdc import NGDCSeabedDescriptions

if __name__ == '__main__':
    # define bounds
    bounds = numpy.array([[-77, 39], [-75, 40]])

    # retrieve a list of the first 5 surveys
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]

    # intialize a Seabed Description object with specific surveys and bounds
    seabed_descriptions = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=bounds)

    print(f'surveys: {seabed_descriptions.surveys}')
    print(f'bounds: {seabed_descriptions.bounds}')
    print(f'descriptions: {seabed_descriptions.descriptions}')
    print(f'data: {seabed_descriptions.data}')
