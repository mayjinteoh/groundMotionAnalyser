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
        for Ts in drange(0.03, 5, '0.1'):
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
            
            #for graccn in trace.data:
            k = (4*m*math.pi**2)/(Ts**2)
            for i in range(0, len(trace.data)):
                #print(i)
                graccn = trace.data[i]
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
        print(amaxlist)

        plt.plot(Tslist, amaxlist)            
                    
def test(p, m=0.4559, k=18, c=0.2865, s0=0, v0=0, p0=0):    
    # 1.1
    a0 = (p0-c*v0-k*s0)/m
    print('a0=',a0)

    #1.2
    t_delta = 0.1

    #1.3
    a1 = 4/(t_delta**2)*m + 2/t_delta*c
    print('a1=',a1)
    a2 = 4/t_delta*m + c
    print('a2=',a2)
    a3 = m
    print('a3=',a3)

    # 1.4
    k_h = k + a1
    print('k_h=',k_h)

    #2.0
    u = []
    u_b = []
    u_bb = []
    for i in range(len(p)):
        if i == 0:
            u.append(0.0)
            u_b.append(0.0)
            u_bb.append(0.0)

        else:
            p_h = p[i] + a1*u[i-1] + a2*u_b[i-1] + a3*u_bb[i-1]
            temp_u = p_h/k_h
            temp_u_b = 2/t_delta*(temp_u-u[i-1]) - u_b[i-1]
            temp_u_bb = 4/(t_delta**2)*(temp_u-u[i-1]) - 4/t_delta*u_b[i-1] - u_bb[i-1]
            u.append(temp_u)
            u_b.append(temp_u_b)
            u_bb.append(temp_u_bb)

    print('u list=',u)
    print('u_b list=',u_b)
    print('u_bb list = ', u_bb)

p = [0.00,25.00,43.3013,50.0,43.3013,25.0,0.0,0.0,0.0,0.0,0.0]
test(p)
                        