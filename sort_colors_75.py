def sortColors(nums):
    k = 3
    map_nums = {}
    for num in nums:
        map_nums[num] = map_nums.get(num, 0) + 1

    index = 0
    for i in range(k):
        if i not in map_nums: continue
        count_i = map_nums[i]
        nums[index:index+count_i] = [i] * count_i
        index += count_i 

if __name__ == '__main__':
    sortColors([2, 2, 2, 1, 1, 1])
