def canJump(nums):
    jump = [False] * len(nums)
    jump[0] = True
    for i in range(0, len(nums)):
        for j in range(i, -1, -1):
            jump[i] = jump[i] or (jump[j] and (i - j) <= nums[j])
            if jump[i]: break
    
    return jump[-1]


def canJump2(nums):
    reach = 0
    n = len(nums)
    i = 0
    while i < n and i <= reach:
        reach = max(reach, i + nums[i])
        i += 1
    return reach >= n - 1

if __name__ == "__main__":
    print(canJump2([2, 3, 1, 1, 4]))
    print(canJump2([3, 2, 1, 0, 4]))
    print(canJump2([0, 2, 3]))
