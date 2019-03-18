from bisect import bisect_right

def threeSumClosest(nums, target):
    def get_closest(nums, low, high, find):
        arr = nums[low: high + 1]
        # print(arr, find)
        ind = bisect_right(arr, find)
        # print(ind)
        if ind < len(arr) and arr[ind] == find: return arr[ind]
        if ind == 0: return arr[0]
        elif ind == len(arr): return arr[len(arr) - 1]
        else: 
            return arr[ind -1] if abs(find - arr[ind -1]) < abs(find - arr[ind]) else arr[ind]
            
    output = []
    nums = sorted(nums)
    print(nums)
    current_min = 1 << 31
    for i in range(0, len(nums)-2):
        # print(f'{i}')
        for j in range(i + 1, len(nums) - 1):
            remainder = target - (nums[i] + nums[j])
            # print((nums[i], nums[j], remainder))
            num = get_closest(nums, j + 1, len(nums) - 1, remainder)

            # print((nums[i], nums[j], remainder, nums[j+1: len(nums)]), num)
            if abs(remainder - num) < current_min:
                current_min = abs(remainder - num)
                output = nums[i] +  nums[j] + num
    print(output)
    return output

if __name__ == '__main__':
    threeSumClosest([-1,2,1,-4], 1)
    threeSumClosest([-3, 5, 6, -1, 2, 1, -4, 3], 1)