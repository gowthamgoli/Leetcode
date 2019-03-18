def twoSum(numbers, target):
    lptr = 0
    rptr = len(numbers) - 1
    while lptr < rptr:
        if numbers[lptr] + numbers[rptr] > target: rptr -= 1
        elif numbers[lptr] + numbers[rptr] < target: lptr += 1
        else: return[lptr+1, rptr+1]

if __name__ == '__main__':
    indices = twoSum([2,7,11,15], 9)
    print(indices)
    