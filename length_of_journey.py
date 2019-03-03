#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:39:24 2019

@author: fatmaa.b
"""

#%%
import geopandas as gpd
import matplotlib.pyplot as plt

import pandas as pd

#%%
dataset1 = pd.read_csv('Dataset1_combined.csv')
#%%
import math
#%%
# Code: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1 = math.radians(lon1)
    lat1 = math.radians(lat1)
    lon2 = math.radians(lon2)
    lat2 = math.radians(lat2)

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
#%%
tot = 0
for i in range (len(dataset1)-1):
    lon1 = dataset1.iloc[i,2]
    lon2 = dataset1.iloc[i+1,2]
    lat1 = dataset1.iloc[i,2]
    lat2 = dataset1.iloc[i+1,2]
    d = haversine(lon1, lat1, lon2, lat2)
    tot = tot + d
total = tot*0.621371
print('Total Length of Journey in Miles: ', total )