def subsets(nums):
    def backtrack(output, nums, subset, start):
        output.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(output, nums, subset, i + 1)
            subset.pop()

    output = []
    backtrack(output, nums, [], 0)
    return output

if __name__ == "__main__":
    print(subsets([1,2,3]))