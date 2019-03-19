def maxSubArray(nums):
    n = len(nums)
    prev_max = nums[0]
    max_so_far = prev_max
    for i in range(1, n):
        prev_max = nums[i] if prev_max < 0 else prev_max + nums[i]
        max_so_far = max(max_so_far, prev_max)
    return max_so_far
    
if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))