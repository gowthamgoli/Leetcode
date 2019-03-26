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

def subsets2(nums):
    def dfs(output, nums, path, index):
        output.append(path)
        for i in range(index, len(nums)):
            dfs(output, nums, path + [nums[i]], i + 1)

    output = []
    dfs(output, nums, [], 0)
    return output

if __name__ == "__main__":
    print(subsets2([1,2,3,4]))