def searchMatrix(matrix, target):
    row, col = 0, len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        cell = matrix[row][col]
        if cell == target: return True

        if target > cell: row += 1
        else: col -= 1
    return False

if __name__ == "__main__":
    print(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
