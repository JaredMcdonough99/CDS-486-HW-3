# -*- coding: utf-8 -*-
"""
Jared McDonough
Team Members: Alexis, Fatima, Matthew, and Nicky 
"""

import pandas as pd

df = pd.read_csv("dataset1_combined.csv")
#yosemdf = df[(df['longitude'].between(-93, -92, inclusive=True))]  
#yosemtrue = yosemdf[(yosemdf['longitude'].between(-93, -92, inclusive=True))]
nonstopmphdf = df[(df['speedmph']) != 0]
print(nonstopmphdf['speedmph'].mean())
print(nonstopmphdf['speedmph'].std())

nonstopkmhdf = df[(df['speedkmh']) != 0]
print(nonstopkmhdf['speedkmh'].mean())
print(nonstopkmhdf['speedkmh'].std())

print('Done')