import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.nums = []        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict: return False
        self.nums.append(val)
        self.dict[val] = len(self.nums) - 1
        return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict: return False
        index = self.dict[val]
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.dict[self.nums[index]] = index
        self.nums.pop()
        del self.dict[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.nums) == 0: return None
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]
    
    def __str__(self):
        return f'{self.dict}\n{self.nums}'

if __name__ == "__main__":
    # Init an empty set.
    randomSet = RandomizedSet()

    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1)

    # Returns false as 2 does not exist in the set.
    randomSet.remove(2)

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2)

    # getRandom should return either 1 or 2 randomly.
    print(randomSet.getRandom())

    # Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1)

    # 2 was already in the set, so return false.
    randomSet.insert(2)

    # Since 2 is the only number in the set, getRandom always return 2.
    print(randomSet)
    print(randomSet.getRandom())
