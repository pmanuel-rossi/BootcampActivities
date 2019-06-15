#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:25:15 2019

@author: pedrorossi
"""

pies = ['(1) Pecan', '(2) Apple Crisp', '(3) Bean', '(4) Banoffee',  '(5) Black Bun', '(6) Blueberry', '(7) Buko', '(8) Burek',  '(9) Tamale', '(10) Steak']

noNumberPie = []

for pie in pies:
    noNum = pie[4:]
    noNumberPie.append(noNum)
    
print(noNumberPie)
    
print('These are our pies')
print(pies)

boughtPies = []
morePie = 'Yes'

while morePie == 'Yes':
    selectedNumber = input('Select the number of the pie you would like to chose')
    selectedPie = pies[int(selectedNumber) - 1][4:]
    print('Great!, well have that ' + selectedPie + ' pie right out for you.')
    boughtPies.append(selectedPie)
    morePie = input('Would You like to select another pie?')
    
print('You bought the following pies:')

pies_dictionary = {}

for pie in boughtPies:
    if pie in pies_dictionary:
        pies_dictionary[pie] +=1
    elif pie not in pies_dictionary:
        pies_dictionary[pie] = 1

for pie in noNumberPie:
    if pie not in pies_dictionary:
        pies_dictionary[pie] = 0
    
    

for key,value in pies_dictionary.items():
    print(value, key)