class DoubleLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.mru += 1
        self.cache[key]['time'] = self.mru
        return self.cache[key]['value']

    def put(self, key: int, value: int) -> None:
        self.mru += 1
        if key in self.cache:
            self.cache[key]['value'] = value
            self.cache[key]['time'] = self.mru

        if len(self.cache) < self.capacity:
            self.cache[key] = {
                'value': value,
                'time': self.mru
            }
            return
        
        temp = sorted(self.cache.items(), key=lambda k: k[1]['time'])
        lru_key = temp[0][0]
        del self.cache[lru_key]
        self.cache[key] = {
            'value': value,
            'time': self.mru
        }

    def __str__(self):
        return f'{self.cache} \n {self.mru}'

class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedList(-1, -1)
        self.tail = DoubleLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            # n = DoubleLinkedList(key, self.cache[key].val)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        n = DoubleLinkedList(key, value)
        self._add(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            n = self.head.next
            del self.cache[n.key]
            self._remove(n)

    def _add(self, n):
        temp = self.tail.prev
        temp.next = n
        n.prev = temp
        n.next = self.tail
        self.tail.prev = n

    def _remove(self, n):
        n_prev = n.prev
        n_next = n.next
        n_prev.next = n_next
        n_next.prev = n_prev

    def __str__(self):
        return f'{self.cache}'

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    obj = LRUCache2(capacity)
    param_1 = obj.get(2)
    obj.put(1,1)
    obj.put(2,2)
    obj.get(1)
    obj.put(3,3)
    print(obj.get(2))
    # obj.put(1, 5)
    # obj.put(1, 2)
    # obj.get(1)
    # obj.get(2)
    # print(obj)
