#!/usr/bin/env python3
""" LIFO caching module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system with LIFO eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.c_d = self.cache_data
        self.order = []  # List to tak

    def put(self, key, item):
        """Add item to the c_d dictionary with LIFO eviction policy.
        Args:
            key (str): The key for the item.
            item (Any): The item to store.
        If key or item is None, this method does nothing.
        Ifcache exceeds BaseCaching.MAX_ITEMS, most recent item is discarded.
        """
        if key is not None and item is not None:
            # If key is new and cache is at max capacity
            if key not in self.c_d and len(self.c_d) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.c_d[last_key]
                print(f"DISCARD: {last_key}")

            # Add/Update the item in c_d and update the order list
            if key in self.c_d:
                self.order.remove(key)  # Remove key if it already exists
            self.c_d[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve item by key from c_d dictionary.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            Any: The value in c_d linked to key, or None if key is None
                 or key doesn't exist in c_d.
        """
        return self.c_d.get(key, None)
