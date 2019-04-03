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

def sortColors2(nums):
    left, index, right = 0, 0, len(nums) -1
    while index <= right:
        if nums[index] == 0:
            nums[left], nums[index] = nums[index], nums[left]
            index += 1
            left += 1
        elif nums[index] == 2: 
            nums[right], nums[index] = nums[index], nums[right]
            right -= 1
        else:
            index += 1
    print(nums)

if __name__ == '__main__':
    # sortColors2([2, 0, 2, 1, 1, 0, 1])
    # sortColors2([2,1,1,1])
    sortColors2([2,0,1])
