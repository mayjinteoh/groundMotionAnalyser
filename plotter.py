#!/usr/bin/env python
""" plotter contains the class which mainly focuses on interfacing with plotting graphs and images.

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

from obspyInterface import *

class plotter:
  def __init__(self, obspyInterface):
    self.obspyInterface = obspyInterface
    self.categories = obspyInterface.cat
    self.inventory = obspyInterface.inventory

  def plotev(self):
    map = self.categories.plot(projection = "local")
    return map

# Unit testing 
def main():
	obspyTest = obspyInterface('GEONET')
	obspyTest.SearchByDatetoDate(2016, 2016, 11, 11, 13, 14, 5)
	obspyTest.maxevent()
	obspyTest.stations(0.5)
	plot = plotter(obspyTest)
	plot.plotev()

if __name__ == "__main__":
    main()