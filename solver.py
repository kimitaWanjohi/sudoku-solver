from board import board

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
            
            grid[row][col] = 0
            
    return False

def check_if_valid(grid, num, pos):
    # for row
    for i in range(len(grid[0])):  
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    #for column
        
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    box_y = pos[0] // 3
    box_x = pos[1] // 3

    for i in range(box_y*3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True
print(solve(board))
print(display_board(board))
