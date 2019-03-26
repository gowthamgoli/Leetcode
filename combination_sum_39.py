def combinationSum(candidates, target):
    def dfs(output, candidates, path, target, index, level=0):
        if target == 0:
            output.append(path)
            return True

        for i in range(index, len(candidates)):
            print('|' + '\u2013\u2013\u2013\u2013' * level, path + [candidates[i]], target - candidates[i] )
            if candidates[i] > target: break
            dfs(output, candidates, path + [candidates[i]], target - candidates[i], i, level=level+1)

    output = []
    dfs(output, sorted(candidates), [], target, 0)
    return output

if __name__ == "__main__":
    print(combinationSum([3,6,2,7], 7))
    # print(combinationSum([2,3,5], 8))