def rob(nums):
    n = len(nums)
    if n == 0: return 0
    prev_prev_max = 0
    prev_max = 0
    for i in range(n):
        current_max = max(prev_prev_max + nums[i], prev_max)
        prev_prev_max, prev_max  = prev_max, current_max 
    return current_max

if __name__ == '__main__':
    print(rob([1,2,3,1]))
    print(rob([2,7,9,3,1]))