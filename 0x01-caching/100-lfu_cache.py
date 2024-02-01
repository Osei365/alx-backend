#!/usr/bin/python3
"""lfu cache module """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Base cache class."""
    def __init__(self):
        """initializing class instance."""
        super().__init__()
        self.keys = []
        self.counter = {}

    def put(self, key, item):
        """add item to cache."""
        if key is not None and item is not None:

            if key in self.cache_data:
                self.keys.remove(key)
                self.counter[key] += 1
            else:
                self.counter[key] = 0
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                vl = [self.counter[it] for it in self.counter if it != key]
                mv = min(vl)
                mk = [itm for itm in self.counter if self.counter[itm] == mv]
                if len(mk) > 1:
                    lru_imp = [self.keys.index(idx) for idx in mk]
                    discard_key = self.keys[min(lru_imp)]
                else:
                    discard_key = mk[0]
                del self.cache_data[discard_key]
                self.keys.remove(discard_key)
                self.counter.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))

    def get(self, key):
        """gets an item from cache."""
        item = self.cache_data.get(key)
        if key is not None and item is not None:
            self.keys.remove(key)
            self.keys.append(key)
            self.counter[key] += 1
            return item
        return None
