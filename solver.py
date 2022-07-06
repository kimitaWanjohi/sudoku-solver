from board import board
import time

#function to display the sudoku grid
def display_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print('_ _ _ _ _ _ _ _ _ _')
            
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print('|', end='')

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j])+ " ", end="")
        
#finding an empty space in the sudoku grid

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) # y, x
                
def check_if_valid(grid, num, pos):
    # for row 
    # looping through the row to check if the el exists except in 
    # the position we plugged it in 
    for i in range(len(grid[0])): 
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    #for column
    # looping through the col to check if the el exists except in 
    # the position we plugged it in 
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
            
    #finding which y and x coordinates for the box
    # and can only be 0, 1, 2 
    # ie the first box coordinates are (0 0)
    box_y = pos[0] // 3 
    box_x = pos[1] // 3 
    
        #for column
    # looping through the box to check if the el exists except in 
    # the position we plugged it in 
    for i in range(box_y*3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    else:
        row , col = empty
    for i in range(1, 10):
        if check_if_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
            	return True
            
            # this wil execute if solve returns false 
            # hense we reset the previous value and try again
            grid[row][col] = 0
            
    return False
     		
 
solve(board)
