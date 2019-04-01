def searchRange(nums, target):
    def search_start(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                index = mid
                right = mid - 1
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return index

    def search_end(nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                index = mid
                left = mid + 1
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return index
    start = search_start(nums, target)
    end = search_end(nums, target)

    return [start, end]

if __name__ == "__main__":
    searchRange([], 8)