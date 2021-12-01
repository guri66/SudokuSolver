N = 9

# Arbitrary sudoku grid, you can choose your own
grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def printGrid(grid):
    for row in range(N):
        if row%3 == 0 and row != 0:
            print('- - - - - - - - - - -')
        for col in range(N):
            if col%3 == 0 and col != 0:
                print('|', end= ' ')
            print(grid[row][col], end=' ')
        print('')

# printGrid(grid)

def anyEmptyLoc(grid, l):
    for row in range(N):
        for col in range(N):
            if (grid[row][col] == 0):
                l[0] = row
                l[1] = col   # Empty location is stored in l
                return True  
    return False   # No empty location

# print(anyEmptyLoc(grid, l))
# print(l)

# check if my number is valid in a 
# specific location: grid[row][col]
def isValidNumber(grid, row, col, num):
    for j in range(N):
        if(grid[row][j] == num):
            return False
    for i in range(N):
        if(grid[i][col] == num):
            return False
    row = row - row%3
    col = col - col%3
    for i in range(3):
        for j in range(3):
            if(grid[row + i][col + j] == num):
                return False
    # num is valid in location
    # grid[row][col] = num
    return True

# solveSudoku is a boolean function
def solveSudoku(grid):
    l = [0, 0]
    if(not anyEmptyLoc(grid, l)):
        return True

    # Assign the empty location to row, col
    row = l[0]
    col = l[1]
    for num in range(1,10):
        if isValidNumber(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid):
                return True
            grid[row][col] = 0
    return False

printGrid(grid)
if solveSudoku(grid):
    print('\n' + 'Solution of this sudoku game exists below: ' + '\n')
    printGrid(grid)
else:
    print('No solution exists')
