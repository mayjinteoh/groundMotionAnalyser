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
import matplotlib.pyplot as plt
from NZS1170Z_D import *

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += float(decimal.Decimal(jump))
    
def RS(tracelist, alpha = 0.5, beta = 0.25, dampingratio = 5/100):
    #constant average acceleration method 
    amax = 0 #max ground displacement
    init_u = 0 #intial ground displacement
    init_v = 0 #initial ground velocity
    init_a = 0 #initial ground acceleration
    m = 1 #structure mass
    
    
    for trace in tracelist: #to obtain peak ground acceleration for each structural period
        t_delta = 1/trace.stats.sampling_rate 
        m = 1
        ubbmax_list = []
        Tslist = []
        for Ts in drange(0.03, 7, '0.1'):
            c = (2*math.pi/Ts)*dampingratio
            k = (4*m*math.pi**2)/(Ts**2)
            # a1 = 4*m/((tstep)**2) + 2*c/tstep
            # a2 = 4*m/(tstep) + c
            # a3 = m
            # u_list = []
            # v_list = []
            # a_list = []
            # p_list = []
            #print(Ts)
            #print(len(trace.data))
            Tslist.append(Ts)
            ubb = AvgAccnMethod(trace.data, t_delta = t_delta, m = 1, k = k, c = c)
            ubbmax_list.append(max(ubb))
        plt.plot(Tslist, ubbmax_list)    
    print(ubbmax_list)
    print(Tslist)    
            #for graccn in trace.data:
        #     
        #     for i in range(0, len(trace.data)):
        #         #print(i)
        #         graccn = trace.data[i]
        #         if i == 0:
        #             u_i = 0
        #             u_list.append(u_i)
        #             v_i = 0
        #             v_list.append(v_i)
        #             a_i = 0
        #             a_list.append(a_i)
        #             if a_i > amax:
        #                 amax = a_i
        #         else:
        #             p = graccn + a1*u_list[i-1] + a2*v_list[i-1] + a3*a_list[i-1]
        #             u_i = p/(k + a1)
        #             u_list.append(u_i)
        #             v_i = 2*(u_i - u_list[i-1])/(tstep)- v_list[i-1]
        #             v_list.append(v_i)
        #             a_i = 4/(tstep**2)*(u_i - u_list[i-1]) - 4/tstep*v_list[i-1] - a_list[i -1]
        #             a_list.append(a_i)
        #             if a_i > amax:
        #                 amax = a_i
        #     amaxlist.append(amax)
        # print(amaxlist)

        # plt.plot(Tslist, amaxlist)            
                    
def AvgAccnMethod(p, t_delta = 0.1, m = 0.4559, k = 18, c = 0.2865, s0=0, v0=0, p0=0):    
    # 1.1
    a0 = (p0-c*v0-k*s0)/m
    print('a0=',a0)


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

    # print('u list=',u)
    # print('u_b list=',u_b)
    return u_bb

# p = [0.00,25.00,43.3013,50.0,43.3013,25.0,0.0,0.0,0.0,0.0,0.0]
# test(p)
def NZRS(subsoilclass, location, returnperiod): #Response Spectrum based on standard 1170.5
    Tlist = []
    RSlist = []
    for T in range(0, 10, 1):
        ChT(subsoilclass, T)
        R(returnperiod)
        Z(location)
        N(T, returnperiod)
            
def ChT(subsoilclass, T):
    if subsoilclass == "A" or subsoilclass == "B":
        if T == 0:
            return 1
        elif T > 0 and T <= 0.1:
            return 1 + 1.35*T/0.1
        elif T > 0.1 and T < 0.3:
            return 2.35
        elif T >= 0.3 and T <= 1.5:
            return 1.6*(0.5/5)**0.75
        elif T > 1.5 and T <= 3:
            return 1.05/ T
        else:
            return 3.15/T**2
 
    elif subsoilclass == "C":
        if T == 0:
            return 1.33
        elif T > 0 and T <= 0.1:
            return 1.33 + 1.6*T/0.1
        elif T > 0.1 and T < 0.3:
            return 2.93
        elif T >= 0.3 and T >= 1.5:
            return 2*(0.5/T)**0.75
        elif T > 1.5 and T <= 3:
            return 1.32/T
        else:
            return 3.96/(T**2)
     
    elif subsoilclass == "D":
        if T == 0:
            return 1.12
        elif T > 0 and T < 0.1:
            return 1.12 + 1.88*T/0.1
        elif T >= 0.1 and T < 0.56:
            return 3
        elif T >= 0.56 and T >= 1.5:
            return 2.4*(0.75/T)**0.75
        elif T > 1.5 and T <= 3:
            return 2.14/T
        else:
            return 6.42/(T**2)  
            
    elif subsoilclass == "E":
        if T == 0:
            return 1.12
        elif T > 0 and T < 0.1:
            return 1.12 + 1.88*T/0.1
        elif T >= 0.1 and T < 1:
            return 3
        elif T >= 1 and T <= 1.5:
            return 3/(T**0.75)
        elif T > 1.5 and T <= 3:
            return 3.32/T
        else:
            return 9.96/(T**2)

def R(returnperiod):
    Rdict = {20: 0.2, 25: 0.25, 50: 0.35, 100: 0.5, 250: 0.75, 500: 1, 1000: 1.3, 2000: 1.7, 2500: 1.8} 
    return Rdict[int(returnperiod)]    

def Z(location):
    return locationZ_D[location]['Z']
    
print(Z('Paraparaumu'))