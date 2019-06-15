# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

options = ('r','p','s')

userChoice = input('Pick (r)ock, (p)aper, (s)cisors')

computerChoice = random.choice(options)

if computerChoice == 'r':
    print('The computer chose Rock.')
elif computerChoice == 'p':
    print('The computer chose Paper.')
else:
    print('The computer chose Scisors.')

if userChoice == computerChoice:
    print("Tie!")
elif (userChoice == 'r' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 's') or (userChoice == 's' and computerChoice == 'r'):
    print ("You Lost!")
elif (userChoice == 'r' and computerChoice == 's') or (userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p'):
    print ("You Won!")
else:
    print("Please pick a valid option")