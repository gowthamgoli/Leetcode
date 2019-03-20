from random import randint

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        output = self.nums[:]
        n = len(output)
        for i in range(n-1, -1, -1):
            j = randint(0, i)
            output[i], output[j] = output[j], output[i]
        return output

# Your Solution object will be instantiated and called as such:
obj = Solution([4, 5, 6])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1)
print(param_2)
