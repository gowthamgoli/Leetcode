import bisect
import heapq

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

class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
           return  float((self.large[0] - self.small[0]) / 2.0)
        return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder2()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
# obj.addNum(4)
param_2 = obj.findMedian()
print(param_2)