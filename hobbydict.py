#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:15 2019

@author: pedrorossi
"""

# hobbyBook

hobbyDict = {"Name" : "Pedro Rossi", "Age" : 26, "Hobbies" : ["Piano", "Tennis", "Pool"], "Wakeup": {"Monday": "6 am", "Tuesday": "5 am", "Wednsday": "6am", "Thirsday": "5 am", "Friday": "6 am"}}

print(hobbyDict["Name"])
print("Numer of hobbies: " + str(len(list(hobbyDict["Hobbies"]))))
print("He wakes up at: ")
for day, time in hobbyDict["Wakeup"].items():
    print(day,time)