def permute(nums):
    def backtrack(output, permutation, nums):
        if len(permutation) == len(nums):
            # print(permutation)
            output.append(permutation[:])
            return

        for num in nums:
            if num in permutation:
                continue
            permutation.append(num)
            print(permutation)
            backtrack(output, permutation, nums)
            permutation.pop()
            print(permutation)
    output = []
    backtrack(output, [], nums)
    return output

if __name__ == "__main__":
    print(permute([1,2,3]))
