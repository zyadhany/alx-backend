#!/usr/bin/python3
"""
0-basic_cache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
