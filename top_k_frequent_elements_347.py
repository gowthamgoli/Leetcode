def topKFrequent(nums, k):
    map_nums = {}
    output = []
    for num in nums:
        map_nums[num] = map_nums.get(num, 0) + 1
    map_count = {}

    for num, count in map_nums.items():
        map_count[count] = map_count.get(count, []) + [num]

    for i in range(len(nums), 0, -1):
        if i not in map_count: continue
        output += map_count[i]
        if len(output) >= k: return output[:k]

if __name__ == "__main__":
    print(topKFrequent([2, 2, 4, 4, 1, 1, 1, 2, 2, 3, 3, 3], 3))
    print(topKFrequent([2, 4, 1, 1, 1, 1, 2, 2, 3], 1))