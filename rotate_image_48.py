def rotate1(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        for j in range(n):
            row[j], row[~j] = row[~j], row[j]

    # print(matrix)

def rotate2(matrix):
    n = len(matrix)
    for i in range(n//2):
        matrix[i], matrix[~i] = matrix[~i], matrix[i]
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

if __name__ == '__main__':
    rotate2([[1,2,3],[4,5,6],[7,8,9]])