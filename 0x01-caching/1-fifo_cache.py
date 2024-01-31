#!/usr/bin/python3
"""fifo cache module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Base cache class."""
    def __init__(self):
        """initializing class instance."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add item to cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard_key = self.keys[0]
                del self.cache_data[discard_key]
                del self.keys[0]
                print('DISCARD: {}'.format(discard_key))

    def get(self, key):
        """gets an item from cache."""
        item = self.cache_data.get(key)
        if key is not None and item is not None:
            return item
        return None
