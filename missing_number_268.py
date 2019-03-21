def missingNumber(nums):
    n = len(nums)
    sum_n = int ((n * (n + 1)) / 2)
    sum_nums = sum(nums)
    return sum_n - sum_nums

def missingNumber2(nums):
    xor = 0
    n = len(nums)
    for i in range(len(nums)):
        xor = xor ^ i ^ nums[i] 
    return xor ^ n

if __name__ == '__main__':
    print(missingNumber([9,6,4,2,3,5,7,0,1]))
    print(missingNumber2([9,6,4,2,3,5,7,8,1]))