#!/usr/bin/python3
"""
100-lfu_cache.py
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
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
            cnt = 0
            for i in range(len(self.key_qeue)):
                if self.key_qeue[i][0] == key:
                    cnt = self.key_qeue[i][1]
                    del self.key_qeue[i]
                    break
            self.cache_data[key] = item
            self.key_qeue.append([key, cnt + 1])
        else:
            if self.size == self.MAX_ITEMS:

                mn = 0
                at = -1
                rem_key = None

                for i in range(self.key_qeue):
                    if self.key_qeue[i][1] < mn:
                        at = i
                        mn = self.key_qeue[i][1]
                        rem_key = self.key_qeue[i][0]

                del self.key_qeue[at]
                del self.cache_data[rem_key]
                self.size -= 1
                print("DISCARD:", rem_key)
            self.size += 1
            self.cache_data[key] = item
            self.key_qeue.append([key, 1])

    def get(self, key):
        """
        get data of key from cach
        """
        if not key or key not in self.cache_data:
            return None
        for i in range(len(self.key_qeue)):
            if self.key_qeue[i][0] == key:
                re = self.key_qeue[i]
                re[1] += 1
                del self.key_qeue[i]
                self.key_qeue.append(re)
                break
        return self.cache_data[key]
