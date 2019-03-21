class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def __str__(self):
        return f"{self.stack} | {self.min_stack}"

    def push(self, x):
        self.stack.append(x)
        n = len(self.min_stack)
        if n == 0:
            self.min_stack.append(x)
            return
        if x <= self.min_stack[n - 1]:
            self.min_stack.append(x)

    def pop(self):
        x = self.stack.pop()
        if self.min_stack and x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
        
# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(-3)
print(minStack)
print(minStack.getMin())
minStack.pop()
print(minStack)
print(minStack.top())
print(minStack)
print(minStack.getMin())
