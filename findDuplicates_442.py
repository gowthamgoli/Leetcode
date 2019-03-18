def findDuplicates(nums):
    duplicates = []
    for i, _ in enumerate(nums):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0: nums[idx] = -nums[idx]
        else: duplicates.append(idx + 1)
    return duplicates

if __name__ == '__main__':
    duplicates = findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print(duplicates)