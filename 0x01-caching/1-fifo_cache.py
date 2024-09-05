#!/usr/bin/python3
"""
1-fifo_cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    cach class
    """

    def __init__(self):
        """
        intial function to run.
        """
        super().__init__()
        self.key_qeue = []
        self.size = 0

    def put(self, key, item):
        """
        add new key to cach
        """
        if not key or not item or key in self.cache_data:
            return

        if self.size == self.MAX_ITEMS:
            rem_key = self.key_qeue[0]
            del self.key_qeue[0]
            del self.cache_data[rem_key]
            self.size -= 1
            print("DISCARD:", rem_key)

        self.size += 1
        self.cache_data[key] = item
        self.key_qeue.append(key)

    def get(self, key):
        """
        get data of key from cach
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
