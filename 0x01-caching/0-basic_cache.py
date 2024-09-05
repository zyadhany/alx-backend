#!/usr/bin/python3
"""
0-basic_cache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic cach
    """

    def put(self, key, item):
        """
        add ket to cach
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get key from cach
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
