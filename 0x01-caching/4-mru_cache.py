#!/usr/bin/python3
"""
4-mru_cache.py
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
        if not key or not item:
            return

        if key in self.cache_data:
            for i in range(len(self.key_qeue)):
                if self.key_qeue[i] == key:
                    del self.key_qeue[i]
                    break
        else:
            if self.size == self.MAX_ITEMS:
                rem_key = self.key_qeue[-1]
                del self.key_qeue[-1]
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
        for i in range(len(self.key_qeue)):
            if self.key_qeue[i] == key:
                del self.key_qeue[i]
                self.key_qeue.append(key)
                break
        return self.cache_data[key]
