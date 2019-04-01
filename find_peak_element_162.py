def findPeakElement(nums):    
    left, right = 0, len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: return mid
        
        if nums[mid] < nums[mid+1]: left = mid + 1
        elif nums[mid] < nums[mid-1]: right = mid - 1

    return left if nums[left] > nums[right] else right

if __name__ == "__main__":
    # print(findPeakElement([1,2,3,1]))
    # print(findPeakElement([1,2,3]))
    print(findPeakElement([3,2,1]))