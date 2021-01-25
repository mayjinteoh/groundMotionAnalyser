# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:33:10 2021

@author: May Jin
"""

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

import math
import decimal
from matplotlib import pyplot as plt

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += float(decimal.Decimal(jump))
    
def AvgAccnMethod(tracelist, alpha = 0.5, beta = 0.25, dampingratio = 5/100):
    #constant average acceleration method 
    amax = 0 #max ground displacement
    init_u = 0 #intial ground displacement
    init_v = 0 #initial ground velocity
    init_a = 0 #initial ground acceleration
    m = 1 #structure mass
    amaxlist = []
    Tslist = []
    
    for trace in tracelist: #to obtain peak ground acceleration for each structural period
        tstep = 1/trace.stats.sampling_rate 
        for Ts in drange(0.03, 0.5, '0.1'):
            c = (2*math.pi/Ts)*dampingratio
            a1 = 4*m/((tstep)**2) + 2*c/tstep
            a2 = 4*m/(tstep) + c
            a3 = m
            u_list = []
            v_list = []
            a_list = []
            p_list = []
            #print(Ts)
            #print(len(trace.data))
            Tslist.append(Ts)
            
            for graccn in trace.data:
                k = (4*m*math.pi**2)/(Ts**2)
                for i in range(0, len(trace.data)):
                    #print(i)
                    if i == 0:
                        u_i = 0
                        u_list.append(u_i)
                        v_i = 0
                        v_list.append(v_i)
                        a_i = 0
                        a_list.append(a_i)
                        if a_i > amax:
                            amax = a_i
                    else:
                        p = graccn + a1*u_list[i-1] + a2*v_list[i-1] + a3*a_list[i-1]
                        u_i = p/(k + a1)
                        u_list.append(u_i)
                        v_i = 2*(u_i - u_list[i-1])/(tstep)- v_list[i-1]
                        v_list.append(v_i)
                        a_i = 4/(tstep**2)*(u_i - u_list[i-1]) - 4/tstep*v_list[i-1] - a_list[i -1]
                        a_list.append(a_i)
                        if a_i > amax:
                            amax = a_i
            amaxlist.append(amax)
        #print(u_list)

    return plt.plot(Tslist, amaxlist)            
                    
    
                
                        