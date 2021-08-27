# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:24:00 2021

@author: namis
"""

from Samplemadlib import hp, zombie, hungergame
import random

if __name__ == '__main__':
    m = random.choice([hp, zombie, hungergame])
    m.madlib()