def increasingTriplet(nums):

    if len(nums) < 3: return False

    stack = []
    stack.append(nums[0])
    next_greatest = {}


    for i in range(1, len(nums)):
        while stack:
            stack_top = stack[-1]
            if stack_top < nums[i]:
                next_greatest[stack_top] = nums[i]
                stack.pop()
            else:
                break
        stack.append(nums[i])

    print(next_greatest)
            
    for num in nums:
        if num not in next_greatest: continue
        if num in next_greatest and next_greatest[num] in next_greatest:
            return True
    return False

if __name__ == '__main__':
    # print(increasingTriplet([4,1,5,3,2,6,7,0]))
    # print(increasingTriplet([1,5,7]))
    print(increasingTriplet([5,1,5,5,2,5,4]))