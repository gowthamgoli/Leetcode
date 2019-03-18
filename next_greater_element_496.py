def nextGreaterElement(nums1, nums2):
    result = [0] * len(nums1)
    stack = []
    map_nums2 = {}
    for num in nums2:
        while len(stack) > 0 and stack[-1] < num:
           map_nums2[stack.pop()] = num
        stack.append(num)
    for i, num in enumerate(nums1):
        result[i] = map_nums2.get(num, -1)
    return result

if __name__ == '__main__':
    result = nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(result)
    result = nextGreaterElement([2, 4], [1, 2, 3, 4])
    print(result)
    result = nextGreaterElement([7, 5, 4, 3, 2, 1, 6], [7, 5, 4, 3, 2, 1, 6])
    print(result)