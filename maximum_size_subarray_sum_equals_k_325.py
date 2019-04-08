def maxSubArrayLen(nums, k):
    s = [0] * len(nums)
    s[0] = nums[0]
    map_sum = {nums[0]: s[0]}
    for i in range(1, len(nums)):
        temp = s[i - 1] + nums[i]
        s[i] = temp
        if temp not in map_sum:
            map_sum[s[i - 1] + nums[i]] = i
    output = 0
    print(s)
    print(map_sum)
    for j in range(len(nums)):
        if s[j] - k in map_sum:
            output = max(output, j - map_sum[s[j] - k])
    return output

if __name__ == "__main__":
    print(maxSubArrayLen([1, -1, 5, -2, 3], 3))
