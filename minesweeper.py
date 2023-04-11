###
### File: minesweeper.py
### Description: Provides a main function and some helper functions 
###              to help students implement a text-based minesweeper
###              game.
###
### DO NOT MODIFY ANY OF THIS FILE 
###

# This imports the functions from utils.
# You should go implement those functions!
from utils import *

def main():
    file_name = input("Enter File Name:\n")
    board = read_file(file_name)
    update_grid(board)
    user_view = make_empty_clone(board)
    count = count_total_moves(board)
    game_status = True
    while game_status:
        print("-" * (3 * len(board[0])))
        print_grid(user_view)
        # NOTE: This assumes that commands from the user are valid.
        command = input("\nWhat is your move?\n").lower()
    
        if command == "exit":
            print("Thank you for playing")
            return
        else:
            dig(board, command, user_view)
        count -= 1
        game_status = determine_game_status(user_view, count)
    print_grid(user_view)
    print("Game Over")
    if count == 0:
        print("You Win!")
    print_grid(board)

def read_file(filename):
    '''
    Takes a given mine csv file and converts it to a 2D list.
    The 2D list that this returns will have one-character strings.
    An 'X' will represent a mine, and a ' ' is a non-mine.
    For example, this function might return a 2D list that liiks like:

    [ [' ', 'X', ' '],
      ['X', ' ', ' '],
      [' ', ' ', 'X'] ]

    Parameters:
    filename:   The name of a csv file to be read.
    '''
    file = open(filename, 'r')
    x = int(file.readline())
    y = int(file.readline())
    grid = [''] * y
    for i in range(y):
        row = file.readline().strip("\n").split(",")
        for j in range(len(row)):
            if int(row[j]) == 1:
                row[j] = "X"
            else:
                row[j] = '0'
        grid[i] = row
    return grid

main()
