class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.sum += val
        self.nums.append(val)
        if len(self.nums) > self.size:
            self.sum -= self.nums.pop(0)
        return self.sum / len(self.nums)


if __name__ == "__main__":
    m = MovingAverage(3)
    param_1 = m.next(1)
    print(param_1)
    param_1 = m.next(10)
    print(param_1)
    param_1 = m.next(3)
    print(param_1)
    param_1 = m.next(5)
    print(param_1)
    