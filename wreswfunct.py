#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:39:32 2019

@author: pedrorossi
"""

# wrestling with functions

import pandas as pd

wrestlerPath = r'/Users/pedrorossi/Documents/BC_activities/Resources'

wrestlerFile = '/Week 3 - Python-Activities-3-08-Par_WrestlingWithFunctions-Resources-WWE-Data-2016.csv'

wrestlerDF = pd.read_csv(wrestlerPath +wrestlerFile, index_col = 0)

wrestler_data = str(input('What is the wrestler name?'))


def print_percentages(wrestler_data):
    wrestlerList = wrestlerDF.loc[[wrestler_data]]
    fightTotal = wrestlerList['Wins'] + wrestlerList['Losses'] + wrestlerList['Draws'] 
    winPerc = float(wrestlerList['Wins'] / fightTotal)
    losePerc = float(wrestlerList['Losses'] / fightTotal)
    drawPerc = float(wrestlerList['Draws'] / fightTotal)
    print('Win percentage: ' + str(winPerc))
    print('Loss percentage: ' + str(losePerc))
    print('Draw percentage: ' + str(drawPerc))

print_percentages(wrestler_data)

