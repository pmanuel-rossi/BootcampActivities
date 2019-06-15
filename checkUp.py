#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:29:09 2019

@author: pedrorossi
"""

print('Hello user!')

userName = input('Whats your name?')

print("Hello " + userName)

userAge = input('Whats your age?')

if int(userAge) < 25:
    print("Awww... you're just a baby!")
else:
    print("Ah... A well traveled soul are ye.")
