def containsDuplicate(nums):
    num_map = {}
    for num in nums:
        if num in num_map: return True
        else: num_map[num] = 1
    return False