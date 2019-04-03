def canJump(nums):
    jump = [False] * len(nums)
    jump[0] = True
    for i in range(0, len(nums)):
        # print(i)
        for j in range(i, -1, -1):
            # print(i, j, jump[j], (i - j), nums[j])
            # print(i, j)
            jump[i] = jump[i] or (jump[j] and (i - j) <= nums[j])
            if jump[i]: break
    
    return jump[-1]

if __name__ == "__main__":
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))
