#!/usr/bin/env python
""" obspyInterface contains the class which mainly focuses on interfacing with obspy APIs.

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

from obspy.core import *
from obspy.clients.fdsn import Client
import calendar
from obspy.clients.fdsn import Client as FDSN_Client
from obspy import read_inventory
import numpy as np
from obspy.core.util import (BASEMAP_VERSION, CARTOPY_VERSION, MATPLOTLIB_VERSION, PROJ4_VERSION)
from obspy import Stream
import math
from geoLocator import *

class obspyInterface:
  def __init__(self, client):
    self.client = Client(client)
    self.startyr = None
    self.endyr = None
    self.startmonth = None
    self.endmonth = None
    self.startday = None
    self.endday = None
    self.starthour = None
    self.endhour = None
    self.minmag = None
    self.cat = None
    self.start = None
    self.end = None
    self.eventid = None
    self.maxmag = 0.0 #max preferred magnitude type
    self.maxev = None #event of max preferred magnitude type
    self.longitude = 0.0 #longitude of the origin of the event
    self.latitude = 0.0 #latitude of the origin of the event
    self.inventory = None #list of stations
    self.st = None #stream is a list of traces. trace is waveform data of each station.

  def setyear(self, startyr, endyr = None):
    self.startyr = int(startyr)
    if endyr == None:
      self.endyr = int(startyr)
    else:
      self.endyr = int(endyr)
  def getstartyr(self):
    return self.startyr
  def getendyr(self):
    return self.endyr

  def setmonth(self, startmonth, endmonth = None):
    self.startmonth = int(startmonth)
    if endmonth == None:
      self.endmonth = int(startmonth)
    else:
      self.endmonth = int(endmonth)
  def getstartmonth(self):
    return self.startmonth
  def getendmonth(self):
    return self.endmonth

  def setday(self, startday, endday = None):
    self.startday = int(startday)
    if endday == None:
      self.endday = int(startday)
    else:
      self.endday = int(endday)
  def getstartday(self):
    return self.startday
  def getendday(self):
    return self.endday  

  def sethour(self, starthour, endhour = None):
    self.starthour = int(starthour)
    if endhour == None:
      self.endhour = int(starthour)
    else:
      self.endhour = int(endhour)
  def getstarthour(self):
    return self.starthour
  def getendhour(self):
    return self.endhour 

  def setminmag(self, minmag):
    self.minmag = float(minmag)
  def getminmag(self):
    return self.minmag

  def SearchByYear(self, startyr):
    self.setyear(startyr)
    self.start = UTCDateTime(self.startyr, 1, 1, 0, 0, 0)
    self.end = UTCDateTime(self.endyr, 12, 31, 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag, minlongitude = -178.00417, minlatitude = -46.56069, maxlongitude = -176.55973, maxlatitude = -35.22676)
    return self.cat

  def SearchByYrtoYr(self, startyr, endyr):
    self.start = UTCDateTime(self.startyr, 1, 1, 0, 0, 0)
    self.end = UTCDateTime(self.endyr, 12, 31, 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag, minlongitude = -178.00417, minlatitude = -46.56069, maxlongitude = -176.55973, maxlatitude = -35.22676)
    return self.cat

  def SearchByMonth(self, month):
    self.setmonth(month)
    thirtyonedaymonths = [1, 3, 5, 7, 8, 10, 12]
    thirtydaymonths = [4, 6, 9, 11]
    if self.startmonth in thirtyonedaymonths:
      day = 31
    elif self.startmonth in thirtydaymonths:
      day = 30
    else:
      if calender.isleap(self.startyr):
        day = 28
      else:
        day = 29
    self.start = UTCDateTime(self.startyr, self.startmonth, int(day), 0, 0, 0)
    self.end = UTCDateTime(self.endyr, self.endmonth, int(day), 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag, minlongitude = -178.00417, minlatitude = -46.56069, maxlongitude = -176.55973, maxlatitude = -35.22676)
    return self.cat

  def SearchByMonthtoMonth(self, startmonth, endmonth):
    self.setmonth(startmonth, endmonth)
    thirtyonedaymonths = [1, 3, 5, 7, 8, 10, 12]
    thirtydaymonths = [4, 6, 9, 11]
    if self.startmonth in thirtyonedaymonths:
      day = 31
    elif self.startmonth in thirtydaymonths:
      day = 30
    else:
      if calender.isleap(self.startyr):
        day = 28
      else:
        day = 29
    if self.endmonth in thirtyonedaymonths:
      day1 = 31
    elif self.endmonth in thirtydaymonths:
      day1 = 30
    else:
      if calender.isleap(self.endyr):
        day1 = 28
      else:
        day1 = 29
    self.start = UTCDateTime(self.startyr, self.startmonth, int(day), 0, 0, 0)
    self.end = UTCDateTime(self.endyr, self.endmonth, int(day1), 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag, longitude = -178.00417, latitude = -41, maxradius = 6.5)
    return self.cat

  def SearchByMinMag(self, minmag):
    self.setminmag(minmag)
    self.start = UTCDateTime(self.year, 1, 1, 0, 0, 0)
    self.end = UTCDateTime(self.year, 12, 31, 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = start.end, minmagnitude = self.minmag)
    return self.cat
 
  def SearchByDate(self, year, month, day, starthour, endhour, minmag):
    self.setyear(year)
    self.setmonth(month)
    self.setday(day)
    self.sethour(starthour, endhour)
    self.setminmag(minmag)
    self.start = UTCDateTime(self.startyr, self.startmonth, self.startday, self.starthour, 0, 0)
    self.end = UTCDateTime(self.startyr, self.endmonth, self.endday, self.endhour, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag)
    self.cat.plot(projection = "local")
    return self.cat

  def SearchByDatetoDate(self, startyr, endyr, startmonth, endmonth, startday, endday, minmag):
    self.setyear(startyr, endyr)
    self.setmonth(startmonth, endmonth)
    self.setday(startday, endday)
    self.setminmag(minmag)
    self.start = UTCDateTime(self.startyr, self.startmonth, self.startday, 0, 0, 0)
    self.end = UTCDateTime(self.endyr, self.endmonth, self.endday, 23, 59, 59)
    self.cat = self.client.get_events(starttime = self.start, endtime = self.end, minmagnitude = self.minmag, minlongitude = -178.00417, minlatitude = -46.56069, maxlongitude = -176.55973, maxlatitude = -35.22676)
    self.cat.plot(projection = "local")
    return self.cat

  def SearchByEventID(self, eventid):
    self.eventid = eventid
    self.cat = self.client.get_events(eventid = self.eventid)
    self.start = self.cat[0].origins[0].time
    self.end = self.start + 600
    self.cat.plot(projection = "local")
    return self.cat

  def maxevent(self): #event of maximum magnitude based on preferred magnitude type  
    for ev in self.cat:
        if len(self.cat) > 1:
            for m in range(len(ev.magnitudes)):
                if ev.magnitudes[m].magnitude_type == "Mw":
                    if ev.magnitudes[m].mag > self.maxmag:
                        self.maxmag = ev.magnitudes[m].mag
                        self.maxev = ev
                elif ev.magnitudes[m].magnitude_type == "M":
                    if ev.magnitudes[m].mag > self.maxmag:
                        self.maxmag = ev.magnitudes[m].mag
                        self.maxev = ev
        else:
            self.maxev = ev
    self.start = self.maxev.origins[0].time
    self.end = self.start + 600
    return self.maxev

  def stations(self, location, maxrad):
    geolocator = geoLocator()
    self.longitude = geolocator.getLongitude(location)
    self.latitude = geolocator.getLatitude(location)
    maxradius = maxrad/110.574
    #maxlong = self.longitude + maxrad/(111.32*math.cos(maxlat*math.pi/180))
    self.inventory = self.client.get_stations(latitude = float(self.latitude), longitude = float(self.longitude), maxradius= maxradius, starttime = self.start, endtime = self.end)
    #self.inventory = self.client.get_stations(latitude=-42.693,longitude=173.022,maxradius=0.5, starttime = "2016-11-13 11:05:00.000",endtime = "2016-11-14 11:00:00.000")
    self.inventory.plot(projection = "local")
    return self.inventory

  def getwaveforms(self, stationcode):
    self.st = Stream()
    for network in self.inventory:
        for station in network:
            if stationcode == station.code:
                self.st = self.client.get_waveforms(network.code, station.code, "*", "*",
                                          self.start, self.end, attach_response = True)
                 #refer to link for arguments for get waveforms: https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.get_waveforms.html?highlight=get_waveforms#obspy.clients.fdsn.client.Client.get_waveforms        
                #self.st.plot()
    return self.st
    
  def gettrace(self, stationcode):
      self.getwaveforms(stationcode)
      for trace in self.st:
          print(trace.stats)
          print(type(trace.stats))
 
    
 
# Unit testing     
def main():
  obspyTest = obspyInterface('GEONET')
  print(obspyTest.SearchByDate(2016, 11, 13, 0, 23, 5))
  print(obspyTest.maxevent())
  print(obspyTest.stations('50 customhouse quay, wellington', 5))
  #print(obspyTest.getwaveforms('CPLB'))
  print(obspyTest.gettrace('CPLB'))
  
if __name__ == "__main__":
    main()