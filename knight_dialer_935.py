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

if __name__ == "__main__":
    # print(knightDialer(3))
    # print(knightDialer(2))
    # print(knightDialer(1))
    print(knightDialer(161))
