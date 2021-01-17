#!/usr/bin/env python
""" Geolocator class uses Python requests and the Google Maps Geocoding API.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "May Jin Teoh"
__contact__ = "mayjin.teoh@gmail.com"
__copyright__ = "Copyright 2021, May Jin Teoh"
__deprecated__ = False
__license__ = "GPLv3"

import requests

# Default google maps API URL
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {
    'address': '',
    'sensor': 'false',
    'key': 'AIzaSyAWLjkXvH5-ActnNlZ32QZFkmIpHI4LDd0' # API key needed for accessing data
}

class geoLocator:
    def __init__(self):
        self.URL = GOOGLE_MAPS_API_URL
        self.params = params

    def updateLocation(self, location):
        # Takes a location/address in str
        self.params['address'] = location

    def requestGeoData(self, location):
        self.updateLocation(location)
        req = requests.get(self.URL, params=self.params)
        return req.json()

    def getLongitude(self, location):
        res = self.requestGeoData(location)

        # Use the first result
        result = res['results'][0]

        return float(result['geometry']['location']['lng'])

    def getLatitude(self, location):
        res = self.requestGeoData(location)

        # Use the first result
        result = res['results'][0]

        return float(result['geometry']['location']['lat'])

    def getLongitudeLatitude(self, location):
        res = self.requestGeoData(location)

        # Use the first result
        result = res['results'][0]

        # Abstract longitude and latitude
        longitude = float(result['geometry']['location']['lng'])
        latitude = float(result['geometry']['location']['lat'])

        return longitude, latitude


# Unit testing 
def main():
    geoLocatorTest = geoLocator()
    print('Longitude:', geoLocatorTest.getLongitude('Eiffel Tower'))
    print('Latitude:', geoLocatorTest.getLatitude('Buckingham Palace'))
    print('Longitude, Latitude:', geoLocatorTest.getLongitudeLatitude('50 Customhouse Quay, Wellington'))

if __name__ == "__main__":
    main()