from BinaryHeap import BinaryHeap

def findKthLargest(nums, k):
    heap = BinaryHeap()
    heap.build_heap(nums)
    for _ in range(len(nums) - k + 1):
        output = heap.extract_min()
    return output

if __name__ == "__main__":
    print(findKthLargest( [3,2,1,5,6,4], 2))
