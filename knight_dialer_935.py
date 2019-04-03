import math
def knightDialer(N):
    rows, cols = 4, 3
    paths = [[[ 0 for j in range(cols) ] for i in range(rows)]  for n in range(N)]
    for n in range(N):
        for i in range(rows):
            for j in range(cols):
                if i == rows - 1 and j in [0, cols - 1]:
                    paths[n][i][j] = 0
                    continue
                
                if n == 0:
                    paths[n][i][j] = 1
                    continue

                neighbors = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
                for (x, y) in neighbors:
                    i_x, j_y = i + x, j + y
                    temp = 0
                    if i_x >= 0 and i_x < rows and j_y >= 0 and j_y < cols: temp = paths[n -1][i_x][j_y]
                    paths[n][i][j] += temp
    return sum(map(sum, paths[N-1])) % int(math.pow(10, 9) + 7)

def knightDialer2(N):
    graph = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    
    def dfs(graph, node, paths, level, N):
        if paths[node][level - 1] != -1:
            return paths[node][level - 1]
        count = 0
        if level == N:
            return 1
        for neighbor in graph[node]:
            count += dfs(graph, neighbor, paths, level + 1, N)
        paths[node][level - 1] = count
        return count

    output = 0
    paths = [ [-1 for j in range(N)] for  j in range(10)]
    for node, _ in graph.items():
        output += dfs(graph, node, paths, 1, N)
    return output % int(math.pow(10, 9) + 7)

if __name__ == "__main__":
    # print(knightDialer2(3))
    # print(knightDialer2(2))
    # print(knightDialer(17))
    # print(knightDialer2(17))
    print(knightDialer2(161))
