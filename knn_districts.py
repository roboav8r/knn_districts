# Notes:
# State boundary data gathered from https://www.census.gov/cgi-bin/geo/shapefiles/index.php on 15 Jan 2022. 2021 States (and equivalent)
# ACK: https://medium.com/@jl_ruiz/plot-maps-from-the-us-census-bureau-using-geopandas-and-contextily-in-python-df787647ef77 for geographic plotting data
# https://pypi.org/project/zipcodes/
# https://towardsdatascience.com/getting-census-data-in-5-easy-steps-a08eeb63995d
# https://api.census.gov/data/2019/acs/acs5/variables.html full variable list

# Import packages
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
#import contextily as ctx 
import geopandas as gpd 
import os 
from mpl_toolkits.axes_grid1 import make_axes_locatable
from census import Census
import pickle

# Define state index for the dataset
state_index = 25 # 25 = Texas
state_abbr = 'TX'

# Read shape data file
df = gpd.read_file('tl_2021_us_state/tl_2021_us_state.shp')
print(type(df))
df = df.to_crs("EPSG:4326") # Convert to coordinate reference system
#df = df.to_crs("EPSG:3395") # Convert to coordinate reference system



# Get the dataframe relating to the state of interest
state_df = df[df['NAME'] == 'Texas'] # geopandas.geodataframe.GeoDataFrame
state_df_iloc = df.iloc[state_index,:] # pandas.core.series.Series


# Get state centroid
print(type(state_df.centroid))


# Get population by lat/lon
c = Census("c233266138b0f02f6217194066f858414e128d04")


# dir(c) = ['ALL', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_acs', 'acs', 'acs1', 'acs1dp', 'acs3', 'acs3dp', 'acs5', 'acs5dp', 'acs5st', 'pl', 'session', 'sf1']
print(c.acs.tables())


#import pickle


# # Open a file and use dump()
# with open('censusdata.pkl', 'wb') as file:
      
#     # A new file will be created
#     pickle.dump(c, file)

  
# Open the file in binary mode
# with open('file.pkl', 'rb') as file:
      
#     # Call load method to deserialze
#     myvar = pickle.load(file)
  
#     print(myvar)