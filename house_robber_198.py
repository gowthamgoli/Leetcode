def rob(nums):
    n = len(nums)
    if n == 0: return 0
    p = [0] * (n + 1)
    p[0], p[1] = 0, nums[0]
    for i in range(2, n + 1):
        p[i] = max(p[i-2] + nums[i - 1], p[i - 1])
    # print(p)
    return p[n]

if __name__ == '__main__':
    print(rob([1,2,3,1]))
    print(rob([2,7,9,3,1]))