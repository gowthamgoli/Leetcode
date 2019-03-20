class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        stack = []
        min_stack = []

    def push(self, x):
        self.stack.append(x)
        n = len(self.min_stack)
        if n == 0:
            self.min_stack.append(x)
            return
        if x <= self.min_stack[n - 1]:
            self.min_stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()