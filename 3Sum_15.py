def threeSum(nums):
    def twoSum(nums, left, right, target, result):
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([-target, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: 
                    left += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    
    output = []
    if len(nums) < 3: return output
    nums = sorted(nums)
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        target = 0 - nums[i]
        left = i + 1
        right = len(nums) - 1
        twoSum(nums, left, right, target, output)
    # print(output)
    return output

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([-1, 0, 1]))
    print(threeSum([-2,0,0,2,2]))
