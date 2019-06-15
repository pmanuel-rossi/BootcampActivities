#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:13:17 2019

@author: pedrorossi
"""

import pandas as pd

udemyPath = r'/Users/pedrorossi/Documents/BC Activities/'
udemyFile = 'Resources/Week 3 - Python-Activities-2-11-Stu_UdemyZip-Resources-web_starter.csv'
udemyDF = pd.read_csv(udemyPath + udemyFile, header = None, usecols = [1,4,5,6,9], names = ['Title', 'Price', 'Subscriber Count', 'Number of Reviews', 'Course Length'])

udemyDF['Review Percentage'] = udemyDF['Number of Reviews']/udemyDF['Subscriber Count']

for date in udemyDF['Course Length']:
    udemyDF['Course Length']

udemyWrite = udemyDF.to_csv(udemyPath + 'udemyPrint.csv', index = False)