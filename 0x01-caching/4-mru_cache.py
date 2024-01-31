#!/usr/bin/python3
"""mru cache module """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Base cache class."""
    def __init__(self):
        """initializing class instance."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add item to cache."""
        if key is not None and item is not None:

            if key in self.cache_data:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discard_id = len(self.keys) - 2
                discard_key = self.keys[discard_id]
                del self.cache_data[discard_key]
                del self.keys[discard_id]
                print('DISCARD: {}'.format(discard_key))

    def get(self, key):
        """gets an item from cache."""
        item = self.cache_data.get(key)
        if key is not None and item is not None:
            self.keys.remove(key)
            self.keys.append(key)
            return item
        return None
