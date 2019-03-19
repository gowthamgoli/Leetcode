def climbStairs(n):
    nums = [0] * (n + 1)
    nums[1] = 1
    nums[0] = 1
    for i in range(2, len(nums)):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[n]

def climbStairs2(n):
    # basically a fibonacci series
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
  
if __name__ == '__main__':
    print(climbStairs(4))