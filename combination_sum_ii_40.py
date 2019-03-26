def combinationSum2(candidates, target):

    def dfs(candidates, target, path, index, level=0):
        if target == 0:
            output.append(path)
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]: continue
            print('|' + '\u2014' * 4 * level, path + [candidates[i]], target - candidates[i])
            if candidates[i] > target: break
            dfs(candidates, target - candidates[i], path + [candidates[i]], i + 1, level=level+1)

    output = []
    dfs(sorted(candidates), target, [], 0)
    return output

if __name__ == "__main__":
    print(combinationSum2([10,1,2,7,6,1,5], 8))