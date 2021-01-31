# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:33:10 2021

@author: May Jin
"""

#!/usr/bin/env python
"""This file contains NZS1170.5 Z hazard factor and D, dstance to fault based on locations 

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

locationZ_D = {'Kaitaia': {'Z': 0.1, 'D': None}, 'Paihia/Russell': {'Z': 0.1, 'D': None}, 'Kaikohe': {'Z': 0.1, 'D': None},
               'Whangarei': {'Z': 0.1, 'D': None}, 'Dargaville': {'Z': 0.1, 'D': None}, 'Warkworth': {'Z': 0.13, 'D': None},
               'Auckland': {'Z': 0.13, 'D': None}, 'Manakau City': {'Z': 0.13, 'D': None}, 'Waiuku': {'Z': 0.13, 'D': None},
               'Pukekohe': {'Z': 0.13, 'D': None}, 'Thames': {'Z': 0.16, 'D': None}, 'Paeroa': {'Z': 0.18, 'D': None},
               'Waihi': {'Z': 0.18, 'D': None}, 'Huntly': {'Z': 0.15, 'D': None}, 'Ngaruawahia': {'Z': 0.15, 'D': None},
               'Morrinsville': {'Z': 0.18, 'D': None}, 'Te Aroha': {'Z': 0.18, 'D': None}, 'Tauranga': {'Z': 0.2, 'D': None},
               'Mount Maunganui': {'Z': 0.2, 'D': None}, 'Hamilton': {'Z': 0.16, 'D': None}, 'Cambridge': {'Z': 0.18, 'D': None},
               'Te Awamutu': {'Z': 0.17, 'D': None}, 'Matamata': {'Z': 0.19, 'D': None}, 'Te Puke': {'Z': 0.22, 'D': None},
               'Putaturu': {'Z': 0.21, 'D': None}, 'Tokoroa': {'Z': 0.21, 'D': None}, 'Otorohanga': {'Z': 0.17, 'D': None},
               'Te Kuiti': {'Z': 0.18, 'D': None}, 'Mangakino': {'Z': 0.21, 'D': None}, 'Rotorua': {'Z': 0.24, 'D': None},
               'Kawerau': {'Z': 0.29, 'D': None}, 'Whakatane': {'Z': 0.3, 'D': None}, 'Opotiki': {'Z': 0.3, 'D': None},
               'Ruatoria': {'Z': 0.33, 'D': None}, 'Murupara': {'Z': 0.3, 'D': None}, 'Taupo': {'Z': 0.28, 'D': None},
               'Taumarunui': {'Z': 0.21, 'D': None}, 'Turangi': {'Z': 0.27, 'D': None}, 'Gisborne': {'Z': 0.36, 'D': None},
               'Wairoa': {'Z': 0.37, 'D': None}, 'Waitara': {'Z': 0.18, 'D': None}, 'New Plymouth': {'Z': 0.18, 'D': None},
               'Inglewood': {'Z': 0.18, 'D': None}, 'Stratford': {'Z': 0.18, 'D': None}, 'Opunake': {'Z': 0.18, 'D': None},
               'Hawera': {'Z': 0.18, 'D': None}, 'Patea': {'Z': 0.19, 'D': None}, 'Raetihi': {'Z': 0.26, 'D': None},
               'Ohakune': {'Z': 0.27, 'D': None}, 'Waiouru': {'Z': 0.29, 'D': None}, 'Napier': {'Z': 0.38, 'D': None},
               'Hastings': {'Z': 0.39, 'D': None}, 'Wanganui': {'Z': 0.25, 'D': None}, 'Waipawa': {'Z': 0.41, 'D': None},
               'Waipukurau': {'Z': 0.41, 'D': None}, 'Taihape': {'Z': 0.33, 'D': None}, 'Marton': {'Z': 0.3, 'D': None},
               'Bulls': {'Z': 0.31, 'D': None}, 'Feilding': {'Z': 0.37, 'D': None}, 'Palmerston North': {'Z': 0.38, 'D': 16},
               'Dannevirke': {'Z': 0.42, 'D': 10}, 'Woodville': {'Z': 0.41, 'D': 2}, 'Pahiatua': {'Z': 0.42, 'D': 8},
               'Foxton/Foxton Beach': {'Z': 0.36, 'D': None}, 'Levin': {'Z': 0.4, 'D': None}, 'Otaki': {'Z': 0.4, 'D': None},
               'Waikanae': {'Z': 0.4, 'D': 20}, 'Paraparaumu': {'Z': 0.4, 'D': 20}, 'Masterton': {'Z': 0.42, 'D': 10},
               'Porirua': {'Z': 0.4, 'D': 12}, 'Wellington CBD': {'Z': 0.4, 'D': 2}, 'Wellington': {'Z': 0.4, 'D': 8},
               'Hutt Valley-south of Taita Gorge': {'Z': 0.4, 'D': 4}, 'Upper Hutt': {'Z': 0.42, 'D': 2}, 'Eastbourne - Point Howard': {'Z': 0.4, 'D': 8},
               'Wainuiomata': {'Z': 0.4, 'D': 8}, 'Takaka': {'Z': 0.23, 'D': None}, 'Motueka': {'Z': 0.26, 'D': None},
               'Nelson': {'Z': 0.27, 'D': None}, 'Picton': {'Z': 0.3, 'D': 16}, 'Blenheim': {'Z': 0.33, 'D': 5},
               'St Arnaud': {'Z': 0.36, 'D': 2}, 'Westport': {'Z': 0.3, 'D': None}, 'Reefton': {'Z': 0.37, 'D': None},
               'Murchison': {'Z': 0.34, 'D': None}, 'Springs Junction': {'Z': 0.45, 'D': 3}, 'Hanmer Springs': {'Z': 0.55, 'D': 2-6},
               'Seddon': {'Z': 0.4, 'D': 6}, 'Ward': {'Z': 0.4, 'D': 4}, 'Cheviot': {'Z': 0.4, 'D': None},
               'Greymouth': {'Z': 0.37, 'D': None}, 'Kaikoura': {'Z': 0.42, 'D': 12}, 'Harihari': {'Z': 0.46, 'D': 4},
               'Hokitika': {'Z': 0.45, 'D': None}, 'Fox Glacier': {'Z': 0.44, 'D': 2}, 'Franz Josef': {'Z': 0.44, 'D': 2},
               'Otira': {'Z': 0.6, 'D': 3}, 'Arthurs Pass': {'Z': 0.6, 'D': 12}, 'Rangiora': {'Z': 0.33, 'D': None},
               'Darfield': {'Z': 0.3, 'D': None}, 'Akaroa': {'Z': 0.3, 'D': None}, 'Christchurch': {'Z': 0.3, 'D': None},
               'Geraldine': {'Z': 0.19, 'D': None}, 'Ashburton': {'Z': 0.2, 'D': None}, 'Fairlie': {'Z': 0.24, 'D': None},
               'Temuka': {'Z': 0.17, 'D': None}, 'Timaru': {'Z': 0.15, 'D': None}, 'Mt Cook': {'Z': 0.38, 'D': None},
               'Twizel': {'Z': 0.27, 'D': None}, 'Waimate': {'Z': 0.14, 'D': None}, 'Cromwell': {'Z': 0.24, 'D': None},
               'Wanaka': {'Z': 0.3, 'D': None}, 'Arrowtown': {'Z': 0.3, 'D': None}, 'Alexandra': {'Z': 0.21, 'D': None},
               'Queenstown': {'Z': 0.32, 'D': None}, 'Milford Sound': {'Z': 0.54, 'D': None}, 'Palmerston': {'Z': 0.13, 'D': None},
               'Oamaru': {'Z': 0.13, 'D': None}, 'Dunedin': {'Z': 0.13, 'D': None}, 'Mosgiel': {'Z': 0.13, 'D': None},
               'Riverton': {'Z': 0.2, 'D': None}, 'Te Anau': {'Z': 0.36, 'D': None}, 'Gore': {'Z': 0.18, 'D': None},
               'Winton': {'Z': 0.2, 'D': None}, 'Balclutha': {'Z': 0.13, 'D': None}, 'Mataura': {'Z': 0.17, 'D': None},
               'Bluff': {'Z': 0.15, 'D': None}, 'Invercargill': {'Z': 0.17, 'D': None}, 'Oban': {'Z': 0.14, 'D': None}}

#for location in locationZ_D:
#    print(location, locationZ_D[location])