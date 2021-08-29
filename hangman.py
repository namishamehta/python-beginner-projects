# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:29:12 2021

@author: namis
"""

import random
import string 
from words import word_list 

# finding a valid word from a list of random words
def valid_word(word_list):
    word = random.choice(word_list)
    while ('-' in word or ' ' in word):
        word = random.choice(word_list)
    return (word.upper())

def hangman():
    # set of words in the word selected by computer randomly
    word = valid_word(word_list)
    word_letter = set(word)
    
    # set of alphabets in the english language. 
    alphabets = set(string.ascii_uppercase)
    
    # set of alphabets that the user has guessed. 
    used_alphabets = set()
    
    print(f"The word you've to guess has {len(word_letter)} letters")
    
    lives = 6
    
    while len(word_letter) > 0 and lives > 0:
        
        print(f"Heyy, you have {lives} lives left now!!")
        #what the guessed letters are. 
        print("You've guessed these letters already",sorted(used_alphabets))
        
        #what the current word is i.e. W _ R D
        letter_list = [letter if letter in used_alphabets else "_" for letter in word]
        print("Current word is:",''.join(letter_list))
        
        #taking input from user 
        user_input = input("Enter your guess:").upper()
    
        if user_input in alphabets - used_alphabets:
            used_alphabets.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                lives = lives - 1 
                print("Letter is not in word")
                
        elif user_input in used_alphabets:
            print("You've already used it!")
        else:
            print("Please enter valid alphabets")
    
    if lives == 0:
        print(f"Sorry, your lives are over! The correct word is {word}")
    else:
        print(f"Yayy, you've guesses the word {word} right!")

hangman()            
        
        

    