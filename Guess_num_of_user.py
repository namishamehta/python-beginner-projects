# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:28:35 2021

@author: namis
"""
#In this, the computer will guess the number chosen by the user
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f" {guess} Too low (L) or Too high(H)??")
        if feedback == "L":
            low = guess + 1
        if feedback == "H":
            high = guess - 1
    print(f"Yayy, you guessed the num {guess} correctly")
computer_guess(100)
            
