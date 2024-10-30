#!/usr/bin/env python3
""" FIFO caching module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system with FIFO eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.c_d = self.cache_data
        self.order = []  # List to track order of keys for FIFO eviction

    def put(self, key, item):
        """Add item to the c_d dictionary with FIFO eviction policy.

        Args:
            key (str): The key for the item.
            item (Any): The item to store.

        If key or item is None, this method does nothing.
        If cache exceeds BaseCaching.MAX_ITEMS,oldest item is discarded.
        """
        if key is not None and item is not None:
            # If key is new cache is at max capacity, discard oldest entry
            if key not in self.c_d and len(self.c_d) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)  # Get and remove
                del self.c_d[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add/Update the item in c_d and update the order list
            if key in self.c_d:
                self.order.remove(key)  # Remove
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
