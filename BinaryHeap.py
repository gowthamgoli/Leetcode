class BinaryHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, x):
        n = self.size - 1
        self.heap.append(x)
        self.size += 1
        i = n
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def extract_min(self):
        n = self.size - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        minimum = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return minimum

    def heapify(self, i):
        n = self.size - 1
        while i <= (n - 1) // 2:
            minimum = i
            if self.heap[2*i + 1] < self.heap[i]: minimum = 2*i + 1
            if 2*i + 2 <= n and  self.heap[2*i + 2] < self.heap[minimum]: minimum = 2*i + 2
            if minimum == i: break
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            i = minimum

    def build_heap(self, x):
        self.heap = x
        self.size = len(x)
        i = (self.size - 1) // 2
        while i >= 0:
            self.heapify(i)
            i -= 1

    def sort(self):
        output = []
        while self.heap:
            output.append(self.extract_min())
        return output

    def get_min(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

heap = BinaryHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)
# print(heap)
# print(heap.get_min())
# heap.extract_min()
# print(heap)
# heap.extract_min()
# print(heap)
# heap.extract_min()
# print(heap)
# heap.extract_min()
# print(heap)

heap.build_heap([])
print(heap)
print(heap.sort())