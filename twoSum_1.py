def twoSum(nums, target):
    indices = []
    map_indices = {num: i for i, num in enumerate(nums)}
    for i, num in enumerate(nums):
        b = target - num
        if b in map_indices and map_indices[b] != i:
            indices = [i, map_indices[b]]
            return indices
    return indices


if __name__ == '__main__':
    indices = twoSum([2,7,11,15], 9)
    print(indices)
