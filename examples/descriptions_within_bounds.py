import numpy

from seabed.ngdc import NGDCSeabedDescriptions

if __name__ == '__main__':
    # define bounds
    bounds = numpy.array([[-77, 39], [-75, 40]])

    # retrieve a list of the first 5 surveys
    first_5_surveys = NGDCSeabedDescriptions.all_surveys()[:5]

    # intialize a Seabed Description object with specific surveys and bounds
    seabed_object = NGDCSeabedDescriptions(surveys=first_5_surveys, bounds=bounds)

    print(f'surveys: {seabed_object.surveys}')
    print(f'bounds: {seabed_object.bounds}')
    print(f'descriptions: {seabed_object.descriptions}')
    print(f'data: \n{seabed_object.data}')

    print(NGDCSeabedDescriptions.all_surveys())
