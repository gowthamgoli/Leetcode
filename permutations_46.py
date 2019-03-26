def permute(nums):
    def backtrack(output, permutation, nums):
        if len(permutation) == len(nums):
            output.append(permutation[:])
            return

        for num in nums:
            if num in permutation:
                continue
            permutation.append(num)
            backtrack(output, permutation, nums)
            permutation.pop()
    output = []
    backtrack(output, [], nums)
    return output

def permute2(nums):
    def dfs(output, nums, path, avail):
        if len(path) == len(nums):
            output.append(path)
            return
        for i in range(len(avail)):
            dfs(output, nums, path + [avail[i]], avail[:i] + avail[i+1:])

    output = []
    dfs(output, nums, [], nums[:])
    return output

if __name__ == "__main__":
    print(permute2([1,2,3]))
