def PredictTheWinner(nums):
    def PredictTheWinner_helper(nums, i, j, total):
        if i > j: return 0
        if total[i][j] != - 1: return total[i][j]
        if i == j:
            return nums[i]
        if j == i + 1:
            return max(nums[i], nums[j])

        picked_i = min( PredictTheWinner_helper(nums, i + 2, j, total), PredictTheWinner_helper(nums, i + 1, j - 1, total) ) + nums[i]
        picked_j = min( PredictTheWinner_helper(nums, i + 1, j - 1, total), PredictTheWinner_helper(nums, i, j - 2, total) ) + nums[j]
        total[i][j] = max(picked_i, picked_j)
        return total[i][j]

    n = len(nums)
    total = [[-1 for j in range(n)] for i in range(n)]
    total = PredictTheWinner_helper(nums, 0, n - 1, total)
    return 2 * total >= sum(nums)

if __name__ == "__main__":
    print(PredictTheWinner([1,5,2]))
    print(PredictTheWinner([1,5,233, 7]))