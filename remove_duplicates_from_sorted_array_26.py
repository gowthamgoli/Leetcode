def removeDuplicates(nums):
    if len(nums) == 1: return 1
    i = 0
    j = 1
    while i < len(nums) and j < len(nums):
        while j < len(nums) and nums[i] == nums[j]:
            j += 1
        if j == len(nums): break
        nums[i + 1], nums[j] = nums[j], nums[i + 1]
        i += 1
        j += 1
    nums = nums[0: i + 1]
    print(nums)
    return len(nums)

if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(removeDuplicates([1, 2, 3, 4]))
    print(removeDuplicates([1, 2]))
    print(removeDuplicates([1, 1]))