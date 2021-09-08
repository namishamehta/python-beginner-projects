# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:09:06 2021

@author: namis
"""

import random

class Player:
    def __init__(self,letter):
        #letter x or letter o
        self.letter = letter
        
    def get_move(self,game):
        #here we want all the players to get their next move
        pass

#inheritance 
class RandomComputerUser(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square 
    
#inheritance
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square = False 
        val = None 
        while valid_square == False:
            square = input(self.letter + '\'s turn. Input moves from (0-8)')
            # Here we are going to incoroporate couple of checks 
            # If we can cast it as integer, it is valid
            # The value should be in available
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print("Invalid square!!")
        
        return val 
                
    
    