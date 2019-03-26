def subsetsWithDup(nums):

    def dfs(output, nums, path, index):
        output.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]: continue
            dfs(output, nums, path + [nums[i]], i + 1)

    output = []
    dfs(output, sorted(nums), [], 0)
    return output

if __name__ == "__main__":
    print(subsetsWithDup([4,4,4,1,4]))
    