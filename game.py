# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:43:21 2021

@author: namis
"""
from player import RandomComputerUser, HumanPlayer

class TicTacToe:
# This class is basically for designing and playing mechanisms 
    def __init__(self):
        self.board = ['' for _ in range(9)] #this is for 3x3 board by making a list having indices of each position
        self.current_winner = None #to keep a track of current winner, currently it is none 
            
    
    def print_board(self):
        for i in range(3):
            for row in [self.board[i*3:(i+1)*3]]:
                print('|' + '|'.join(row) + '|')
    
    @staticmethod 
    def print_board_nums():
        # This is a static method because it is not related to any of our methods 
        # We don't have to use self here 
        # Also, this method tells us that which number is for which spot 
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range (3)]

        for row in number_board:
                print('|' + '|'.join(row) + '|')
       
    def available_moves(self):
        # This basically returns the list of non empty indices
        moves = []
        for (i,spot) in enumerate (self.board):
        # enumerate will create a list and assign tuples of (index,value) at that index
        # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
            if spot == '':
                moves.append(i)
        return moves                       

    def make_move(self,square,letter):
        if self.board[square] == '':
            self.board[square] = letter
            
            if self.winner(square,letter):
                self.current_winner = letter
                
            return True
        return False 
    
    def empty_squares(self):
        return '' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    # return self.board.count(" ")
    
    def winner(self, square, letter):
    #winner if 3 in a row anywhere... we have to check all of these
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True 
        
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 
        
        #check diagonal
        #but only if the square is an even number (0,2,4,6,8)
        #these are the only moves possible to win the diagonal 
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True 
            
        return False
            
def play(game,x_player,o_player,print_game = True):
    # This class is for playing the game 
        if print_game:
            game.print_board_nums()
        
        letter = 'X' #starting letter
        while game.empty_squares():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            
            if game.make_move(square,letter):
                if print_game:
                    print(letter + f' makes the move to square {square}')
                    game.print_board()
                    print("")
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!!')
                return letter
            
# Now we will alternate letters after we made the move 
            letter = 'O' if letter =='X' else 'X'
        
        if print_game:
            print("It's a tie")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerUser('O')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)    