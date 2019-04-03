def spiralOrder(matrix):
    def spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, direction, i, j):
        if row_start < 0 or row_end >= len(matrix) or col_start < 0 or col_end >= len(matrix[0]): return
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]): return

        if matrix[i][j] == '#': return
        output.append(matrix[i][j])
        matrix[i][j] = '#'
        if direction == 'right':
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'right', i, j + 1)
        elif direction == 'down':
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'down', i + 1, j)
        elif direction == 'left':
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'left', i, j - 1)
        elif direction == 'top':
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'top', i - 1, j)

        if i == row_start and j == col_end:
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'down', i + 1, j)
        elif i == row_end and j == col_end:
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'left', i, j - 1)
        elif i == row_end and j == col_start:
            spiralOrder_helper(matrix, output, row_start, row_end, col_start, col_end, 'top', i - 1, j)
        elif i == row_start + 1 and j == col_start: 
            spiralOrder_helper(matrix, output, row_start + 1, row_end - 1, col_start + 1, col_end - 1, 'right', i, j + 1)
        
    output = []
    if len(matrix) == 0: return output
    spiralOrder_helper(matrix, output, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, 'right', 0, 0)
    return output

if __name__ == "__main__":
    # print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    # print(spiralOrder([[1,2,3],[4,5,6]]))
    # print(spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))
    print(spiralOrder([[1]]))