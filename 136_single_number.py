def singleNumber(nums):
    output = 0
    for num in nums:
        output = num ^ output
    return output