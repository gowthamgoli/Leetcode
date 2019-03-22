from pprint import pformat

def setZeroes(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:  
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(len(matrix[row])):
            matrix[row][j] = 0
    
    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0
    
if __name__ == '__main__':
    matrix = [
        [0,1,2,0],
        [3,0,5,2],
        [1,3,1,5]
    ]
    setZeroes(matrix)
    print(pformat(matrix))
