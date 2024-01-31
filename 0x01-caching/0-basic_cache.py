#!/usr/bin/python3
"""basic cache module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Base cache class."""

    def put(self, key, item):
        """add item to cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item from cache."""
        item = self.cache_data.get(key)
        if key is not None and item is not None:
            return item
        return None
