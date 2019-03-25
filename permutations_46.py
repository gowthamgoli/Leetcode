def permute(nums):

    def backtrack(output, permutation, nums):
        print(permutation)
        if len(permutation) == len(nums):
            output.append(permutation)
            return
        
        for num in nums:
            if num not in permutation: permutation.append(num)
            backtrack(output, permutation, nums)
            permutation.pop()

    output = []
    permutation = []
    backtrack(output, permutation, nums)
    print(output)
    return

if __name__ == "__main__":
    print(permute([1,2,3]))