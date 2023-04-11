###
### File: utils.py
### Author: Dominic Richard
### Description: This program implements the functions
###              for minesweeper.py, determining the board
###              to be displayed and containing the key for
###              which spaces contain mines and which do not.
###              It also determines if the game is over. 
###

# Changes to this file should only be inside function definitions

def find_mine(grid, x, y, position):
    '''
    Determines if a square from a relative position contains a mine. 
    Returns 1 if there is, otherwise returns 0.
    
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    x:          Integer which is the x postiion to be scanned for mines.
    y:          Integer which is the y postiion to be scanned for mines.
    position:        A tuple containing the relative coordinates to scan

    Examples:
    grid = [["X", 0],
            [0, "0"]]
    
    find_mine(grid, 0, 0, (0, 0)))    Returns: 1
    find_mine(grid, 0, 0, (1, 0)))    Returns: 0
    find_mine(grid, 0, 0, (0, 1)))    Returns: 1
    find_mine(grid, 0, 0, (1, 1)))    Returns: 0
    find_mine(grid, 0, 0, (20, 20)))  Returns: 0  
    '''

def count_total_moves(grid):
    '''
    Counts the number of moves that need to be made for the player to
    win the game. (Counts number of squares that are not mines)

    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    '''
    counter = 0
    for line in grid:
        for i in line:
            if i != "X":
                counter += 1
    return counter

def determine_game_status(grid, count):
    '''
    Returns a boolean which is True if the game should continue or 
    False if the game is over. False is returned if a mine has been
    revealed or count is 0 meaning there are no squares without mines
    that are not revealed.
    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    count:      Integer which is the number of mineless squares left to be revealed.
    '''
    for line in grid:
        for i in line:
            if i == "X":
                return False
    if count == 0:
        return False
    return True

def dig(grid, coordinate, user_view):
    '''
    Translates an item at a coordinate on the grid to the correspoinding 
    location on the user_view. 

    Parameters:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    coordinate: A string where the first character is the x-position and the 
                characters that follow makes up the y-position for where to dig. 
                NOTE: The x-position is a letter and the y-position is a number.
    user_view:  2D list containing X's representing mines and numbers which are
                either the number of adjacent X's or 0. Unlike grid, some of the
                values are empty meaning the user has not seen the square.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < len(alphabet):
        if alphabet[i] == coordinate[0]:
            x_coord = i
        i += 1
    if len(coordinate) == 2: 
        y_coord = (len(grid) - 1) - int(coordinate[1])
    if len(coordinate) == 3:
        y_coord = str(coordinate[1] + coordinate[2])
        y_coord = (len(grid) - 1) - int(y_coord)
    user_view[y_coord][x_coord] = grid[y_coord][x_coord]

def update_grid(grid):
    '''
    Populates non-mine squares with the number of adjacent mines.
    Basically, iterate through the grid and replace the ' ' strings with
    a string with a number in it, representing how many mines
    neighbor this location.
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    '''
    i = 0
    while i < len(grid):
        e = 0
        while e < len(grid[i]):
            nearby = 0
            if grid[i][e] != "X":
                if e != len(grid[i]) - 1 and grid[i][e + 1] == "X":
                    nearby += 1
                if e != 0 and grid[i][e - 1] == "X":
                    nearby += 1
                if i != len(grid) - 1 and grid[i + 1][e] == "X":
                    nearby += 1
                if i != len(grid) - 1 and e != len(grid[i]) - 1 and \
                   grid[i + 1][e + 1] == "X":
                    nearby += 1
                if i != len(grid) - 1 and e != 0 and \
                   grid[i + 1][e - 1] == "X":
                    nearby += 1
                if i != 0 and grid[i - 1][e] == "X":
                    nearby += 1
                if i != 0 and e != len(grid[i]) - 1 and \
                   grid[i - 1][e + 1] == "X":
                    nearby += 1
                if i != 0 and e != 0 and grid[i - 1][e - 1] == "X":
                    nearby += 1
                grid[i][e] = str(nearby)
            e += 1
        i += 1
            
def print_grid(grid):
    '''
    Prints out a 2D grid with the y-axis labeled with numbers and the x-axis with letters.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                the number of adjacent X's.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = len(grid) - 1
    for line in grid:
        if len(str(i)) == 2:
            the_str = str(i) + " "
        else:
            the_str = " " + str(i) + " "
        for a in line:
            the_str += "[" + a + "]"
        print(the_str)
        i -= 1
    last_line = "   "
    length = len(grid[i]) - 3 / 3
    i = 0
    while i <= length:
        last_line += " " + alphabet[i] + " "
        i += 1
    print(last_line)

def make_empty_clone(grid):
    '''
    Returns a 2D list which is the same dimensions (rows / columns) as a passed in grid.
    The returned list should contain ' ' strings only
    '''
    new_grid = []
    for line in grid:
        grid_line = []
        for e in line:
            grid_line.append(" ")
        new_grid.append(grid_line)
    return new_grid
        
