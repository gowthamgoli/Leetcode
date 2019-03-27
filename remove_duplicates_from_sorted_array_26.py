def removeDuplicates(nums):
    if len(nums) == 0: return 0
    i, j = 0, 0
    for j in range(len(nums)):
        if nums[i] == nums[j]: continue
        i += 1
        nums[i] = nums[j]
    print(nums[: i + 1])
    return i + 1

if __name__ == '__main__':
    # print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    # print(removeDuplicates([1, 2, 3, 4]))
    # print(removeDuplicates([1, 1]))
    print(removeDuplicates([]))