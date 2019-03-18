def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        num1, nums2 = nums2, nums1
    x = len(nums1)
    y = len(nums1)
    low = 0
    high = x
    
    while low <= high:
        partition_x = int((low + high + 1) / 2)
        partition_y = int((x + y + 1) / 2) - partition_x
        max_left_x = nums1[partition_x - 1] if partition_x > 0 else float('-inf')
        max_left_y = nums2[partition_y - 1] if partition_y > 0 else float('-inf')

        min_right_x = float('inf')  if partition_x == x else nums1[partition_x]
        min_right_y = float('inf')  if partition_y == y else nums2[partition_y]

        while low <= high:
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return max(max_left_x, max_left_y)
            
            if max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
     

if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([900], [10, 13, 14]))