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

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    obj = LRUCache(capacity)
    param_1 = obj.get(2)
    obj.put(2,6)
    obj.get(1)
    obj.put(1, 5)
    obj.put(1, 2)
    obj.get(1)
    obj.get(2)
    # print(obj.get(2))
    print(obj)
