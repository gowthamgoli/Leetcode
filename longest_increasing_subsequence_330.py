def lengthOfLIS(nums):
    if len(nums) == 0: return 0
    l = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            l[i] = max(l[i], 1 + l[j] if nums[j] < nums[i] else l[i])
    return max(l)

if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))