#!/usr/bin/env python3
""" LFU caching module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a caching system with LFU eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.c_d = self.cache_data  # Renaming cache_data to c_d for use
        self.frequency = {}  # Dictionary to store access frequency
        self.order = []  # List to track the order of keys for LRU

    def put(self, key, item):
        """Add item to the c_d dictionary with LFU eviction policy.
        Args:
            key (str): The key for the item.
            item (Any): The item to store.
        If key or item is None, this method does nothing.
        If cache exceeds BaseCaching.MAX_ITEMS,least frequently discarded.
        If multiple items have the same frequency,least recently discarded.
        """
        if key is None or item is None:
            return

        # Check if the item exists and update it
        if key in self.c_d:
            self.c_d[key] = item
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return

        # If cache is at max capacity, discard LFU (and LRU within LFU)
        if len(self.c_d) >= BaseCaching.MAX_ITEMS:
            # Find the least frequency
            min_f = min(self.frequency.values())
            # Collect keys with the least frequency
            lfu_k = [k for k, freq in self.frequency.items() if freq == min_f]
            # Determine the least recently used key among the LFU keys
            lru_key = next(k for k in self.order if k in lfu_k)
            self.order.remove(lru_key)
            del self.c_d[lru_key]
            del self.frequency[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new key-value pair and update frequency/order
        self.c_d[key] = item
        self.frequency[key] = 1
        self.order.append(key)

    def get(self, key):
        """Retrieve item by key from c_d dictionary.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            Any: value in c_d linked to key, or None
                 or key doesn't exist in c_d.
        """
        if key in self.c_d:
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.c_d[key]
        return None
