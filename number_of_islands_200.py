def numIslands(grid):
    
    def dfs(grid, visited, i, j):
        visited[i][j] = True
        row_num = [-1, 0, 0, 1]
        col_num = [0, -1, 1, 0]

        for k in range(4):
            neibhor_i = i + row_num[k]
            neibhor_j = j + col_num[k]
            if neibhor_i >=0 and neibhor_i < len(grid) and neibhor_j >= 0 and neibhor_j < len(grid[0]) and not visited[neibhor_i][neibhor_j] and grid[neibhor_i][neibhor_j] == '1':
                dfs(grid, visited, neibhor_i, neibhor_j)
 
    count = 0
    visited = [ [False for j in range(len(row))] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == '1':
                dfs(grid, visited, i, j)
                count += 1
    
    return count

if __name__ == '__main__':
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))