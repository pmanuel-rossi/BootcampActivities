#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:03:13 2019

@author: pedrorossi
"""

import pandas as pd

netflixPath = r'/Users/pedrorossi/Documents/BC Activities/Resources/Week 3 - Python-Activities-2-08-Stu_ReadNetFlix-Resources-netflix_ratings.csv'

netflixDF = pd.read_csv(netflixPath, index_col = 0)



while True : 
    try: 
        titleVar = input('What are you watching?')
        titleList = netflixDF.loc[titleVar]
        
        rating = titleList[0]
        userRating = titleList[-1]

        print(str(titleVar) + ' is rated ' + str(rating) + ' with a user rating of ' + str(userRating) + '.')
        
        break
    
    except ValueError:
        print('This show or movie has not been fond')