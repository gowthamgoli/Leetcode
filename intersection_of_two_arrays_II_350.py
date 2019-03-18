def intersect(nums1, nums2):
    output = []
    map_nums1 = {}
    for num in nums1:
        map_nums1[num] = 1 + map_nums1.get(num, 0) 
    for num in nums2:
        if num in map_nums1 and map_nums1[num] > 0:
            output.append(num)
            map_nums1[num] -= 1
    return output

if __name__ == '__main__':
    print(intersect([1,2,2,1], [2,2]))
    print(intersect([4,9,5], [9,4,9,8,4]))
