import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.nums, num)
        self.nums = self.nums[:index]  + [num] + self.nums[index:]

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n//2])
        return float((self.nums[n//2] + self.nums[n//2 - 1] ) / 2)

    def __str__(self):
        return str(self.nums)

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
# obj.addNum(4)
param_2 = obj.findMedian()
print(param_2)