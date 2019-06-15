#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:58:43 2019

@author: pedrorossi
"""

from collections import Counter

candy = ['0: Snickers','1: Sour patch kids', '2: MnMs']

print('This candy is available')
print(candy)

allowance = input('Whats your allowance')
candyList = []
print('You can choose ' + str(allowance) + ' candy.')
for x in range(int(allowance)):
    selectedCandy = input('What candy would you like?')
    candyList.append(candy[int(selectedCandy)][3:])

print('You chose the following candy:')
print(Counter(candyList))