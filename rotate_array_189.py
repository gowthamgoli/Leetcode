def rotate(nums, k):
    if len(nums) == 0: return nums
    k = k % len(nums)
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
    print(nums)

if __name__ == '__main__':
    rotate([1,2,3,4,5,6,7], 7)
    rotate([-1,-100,3,99], 2)
    rotate([-1], 2)