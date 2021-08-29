# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:30:09 2021

@author: namishamehta
"""

#This is a game for rock, paper and scissors. 
# method 1
import random
def play():
    comp = random.choice(['Rock','Paper','Scissors'])
    user = input("Please choose between ['Rock','Paper','Scissors']")
    
    if user == comp:
        return "You both selected the same input"
    
    def iswin(user,comp):
        return "Yayy, you win!"
    
    return "You lost!!"

def iswin(player,opponent):
    if ((player == 'Rock' and opponent == 'Scissors') 
        or (player == 'Paper' and opponent == 'Rock') 
        or (player == 'Scissors' and opponent == 'Paper')):
        return True 

play()

'''Method 2
import random
def rock_paper_scissors(num):
    
    choices = ['Rock','Paper','Scissors']
    
    """Rules:
    Rock smashes scissors.
    Paper covers rock.
    Scissors cut paper."""
    
    while num != 0:
        
        comp_turn = random.choice(choices)
        user_turn = input(f'Select one from {choices}')
        
        if user_turn == 'Rock' and comp_turn == 'Scissors':
            print('Yayy, User wins as rock smashes scissors!!')
        elif user_turn == 'Rock' and comp_turn == 'Paper':
            print('Meh, Computer wins as paper covers rock ')
        
        elif user_turn == 'Paper' and comp_turn == 'Scissors':
            print('Meh, Computer wins as scissors cut paper')
        elif user_turn == 'Paper' and comp_turn == 'Rock':
            print('Yayy, User wins as scissors cut paper!!')
        
        elif user_turn == 'Scissors' and comp_turn == 'Rock':
            print('Meh, Computer wins as scissors cut paper')
        elif user_turn == 'Scissors' and comp_turn == 'Paper':
            print('Yayy, User wins as scissors cut paper!!')
            
        elif ((user_turn == 'Scissors' and comp_turn == 'Scissors') or 
              (user_turn == 'Rock' and comp_turn == 'Rock') or 
              (user_turn == 'Paper' and comp_turn == 'Paper')):
            print("Hehe, nobody wins as both selected same choice!!")
        
        else:
            print(f"You selected {user_turn} - an invalid choice. Please select a choice from {choices}.")
        
            
        num = num - 1

rock_paper_scissors(3)

'''


