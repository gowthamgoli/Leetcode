def findRelativeRanks(nums):
    ranks = [0] * len(nums)
    sorted_ranks = [(nums[i], i) for i in sorted(range(len(nums)), key=lambda k: nums[k], reverse=True)]
    for i, entry in enumerate(sorted_ranks):
        if i == 0: ranks[entry[1]] = 'Gold Medal'
        elif i == 1: ranks[entry[1]] =  'Silver Medal'
        elif i == 2: ranks[entry[1]] =  'Bronze Medal'
        else: ranks[entry[1]] = str(i + 1)
    return ranks

if __name__ == '__main__':
    ranks = findRelativeRanks([10,3,4,1,2])
    print(ranks)