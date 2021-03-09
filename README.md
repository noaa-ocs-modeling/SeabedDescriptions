# Seabed

[![tests](https://github.com/noaa-ocs-modeling/seabed/workflows/tests/badge.svg)](https://github.com/noaa-ocs-modeling/seabed/actions?query=workflow%3Atests)
[![build](https://github.com/noaa-ocs-modeling/seabed/workflows/build/badge.svg)](https://github.com/noaa-ocs-modeling/seabed/actions?query=workflow%3Abuild)
[![version](https://img.shields.io/pypi/v/seabed)](https://pypi.org/project/seabed)
[![license](https://img.shields.io/github/license/noaa-ocs-modeling/seabed)](https://creativecommons.org/share-your-work/public-domain/cc0)
[![style](https://sourceforge.net/p/oitnb/code/ci/default/tree/_doc/_static/oitnb.svg?format=raw)](https://sourceforge.net/p/oitnb/code)

parses seabed descriptions from https://www.ngdc.noaa.gov/geosamples/surveydisplay.jsp

## Usage

#### retrieve a list of surveys from the NGBC web page

```python
from seabed import NGDCSeabedDescriptions

surveys = NGDCSeabedDescriptions.all_surveys()
```

#### get seabed descriptions for specific surveys, within specified bounds

```python
import numpy

from seabed import NGDCSeabedDescriptions

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
```
