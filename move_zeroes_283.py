def moveZeros(nums):
    i = 0
    j = 0
    while j < len(nums):
        if i == j and nums[i] != 0:
            i += 1
            j += 1
            continue
        while j < len(nums) and nums[j] == 0 :
            j += 1
        # if j >= len(nums): break
        if j == len(nums): break
        nums[i], nums[j] = nums[j], nums[i]
    
        i += 1
    print(nums)

if __name__ == '__main__':
    moveZeros([0,1,0,3,12])
    moveZeros([0,1,2,3,4,0])
    moveZeros([1,5,0,1,0,0,9])