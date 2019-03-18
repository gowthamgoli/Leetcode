import math

def isValidSudoku(board):
    rows, cols = 9, 9
    grid = int(math.sqrt(rows))

    for i, row in enumerate(board):
        map_row = {}
        for cell in row:
            if cell in map_row:  return False
            elif cell != '.' : map_row[cell] = 1

    for j in range(cols):
        map_col = {}
        for i in range(rows):
            cell = board[i][j]
            if cell in map_col: return False
            elif cell != '.' : map_col[cell] = 1

    
    for i in range(0, rows, 3):
        for j in range(0, cols, 3):
            map_grid = {}
            for row in range(i, i + grid):
                for col in range(j, j + grid):
                    cell = board[row][col]
                    if cell in map_grid: return False
                    elif cell != '.' : map_grid[cell] = 1
    return True

if __name__ == '__main__':
    isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".","7",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

