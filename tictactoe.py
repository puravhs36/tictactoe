# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:04:03 2018

@author: Purav Shah
"""
game_board = [i+1 for i in range(9)]

def print_board(game_board):
    row1 = '| {} | {} | {} |'.format(game_board[0],game_board[1],game_board[2])
    row2 = '| {} | {} | {} |'.format(game_board[3],game_board[4],game_board[5])
    row3 = '| {} | {} | {} |'.format(game_board[6],game_board[7],game_board[8])
    print(row1)
    print(row2)
    print(row3)

def is_avail(game_board,move,y):
    x = move
    if int(move) > 9 or int(move) < 1:
        moves = input('Please enter a number in 1-9: ')
        return is_avail(game_board,moves,y)
    elif x in y:
        movea = input('Sorry! Block already occupied... choose again: ')
        return is_avail(game_board,movea,y)
    else:
        y.append(x)
        return x,y
def is_win(game_board,elem):
    for x in [0,3,6]:    
        if game_board[x] == game_board[x+1] == game_board[x+2] == elem:
            return 0
        else:
            pass
    for x in [0,1,2]:
        if game_board[x] == game_board[x+3] == game_board[x+6] == elem:
             return 0
        else:
            pass
    if game_board[0] == game_board[4] == game_board[8] == elem:
        return 0
    elif game_board[2] == game_board[4] == game_board[6] == elem: 
        return 0
    else:
        pass
    return 1

        
def board_reset(game_board): 
    for x in range(9):
        game_board[x] = x+1
    print_board(game_board)      
while(True):
    start = input("Do you want to start a new game?(y/n): ").lower()
    game = 9 
    if start == 'y':
        board_reset(game_board)
        y = []
        while(game>=1):
            elem = 'X'
            movex = input("Where would you like to put the X?: ") 
            move,y = is_avail(game_board,movex,y)
            print(move)
            game_board[int(move) - 1] = elem
            print_board(game_board)
            check = is_win(game_board,elem)
            if check == 0:
                print('Congratulations! X wins')
                print('Game Over')
                break
            if game != 1:
                game = game - 1
            else:
                print('Match Draw')
                break
            elem = 'O'
            moveo = input("Where would you like to put the O?: ")
            move,y = is_avail(game_board,moveo,y)
            game_board[int(move) - 1] = elem
            print_board(game_board)
            check1 = is_win(game_board,elem)
            if check1 == 0:
                print('Congratulations! O wins')
                print('Game Over')
                break
            game = game - 1
    else:
        clo = input('Are you sure you want to exit?(y/n): ')
        if clo == 'y':
            print('Game Over')
            break

    
        
