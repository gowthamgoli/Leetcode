def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = ([0] if obstacleGrid[0][0] == 1 else [1]) + [0] * (n - 1)
    for i in range(1, n):
        dp[i] = dp[i - 1] if obstacleGrid[0][i] == 0 else 0
    for i in range(1, m):
        for j in range(0, n):
            if obstacleGrid[i][j] == 1: dp[j] = 0
            elif j >= 1: dp[j] = dp[j] + dp[j - 1]
    return dp[n-1]

if __name__ == "__main__":
    print(uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
