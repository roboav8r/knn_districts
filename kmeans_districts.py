# Import packages

from json.tool import main
from unicodedata import name
import pandas as pd
import numpy as np
import zipcodes
from census import Census
from us import states

# Define the District Clustering class
class DistrictClustering():

    def __init__(self, state='TX'):
        
        self.check_for_data(self,state)


    def check_for_data(self,state):
        print('checking for data from {}'.format(state))


# If running this as a standalone script
if __name__=='__main__':
    print('you ran this as a standalone script instead of a class/library')
    clustering = DistrictClustering()