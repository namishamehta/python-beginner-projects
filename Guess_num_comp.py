# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:50:19 2021

@author: namis
"""

import random
def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a num between 1 and {x}:'))
        if guess < random_num:
            print("Sorry, guess again. Too low")
        elif guess > random_num:
            print("Sorry, guess again. Too high")
    print(f"Yayy, you guessed the num {random_num} correctly")
guess(10)