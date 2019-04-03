def uniquePaths(m, n):
    paths = [[0 for j in range(m)] for i in range(n)]     
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                paths[i][j] = 1
            else:
                paths[i][j] = paths[i - 1][j] + paths[i][j-1]
    return paths[n-1][m-1]

if __name__ == "__main__":
    print(uniquePaths(3, 2))    
    print(uniquePaths(7, 3))    