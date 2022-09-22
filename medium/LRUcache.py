class LRUCache:
    lru = {}
    capacity = 0
    recent_key = []
    putCt = 0
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            return self.lru[key] 
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.putCt >= self.capacity:
            del self.lru[self.recent_key.pop()]
            self.lru[key] = value
        else:
            try:
                self.lru[key]
            except:
                self.putCt += 1
            self.recent_key.append(key)
            self.lru[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)