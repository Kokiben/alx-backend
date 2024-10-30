#!/usr/bin/env python3
""" FIFO caching module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system with FIFO eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.order = []  # List to track the order of keys for FIFO eviction

    def put(self, key, item):
        """Add item to the cache_data dictionary with FIFO eviction policy.
        Args:
            key (str): The key for the item.
            item (Any): The item to store.
        If key or item is None, this method does nothing.
        If the cache exceeds BaseCaching.MAX_ITEMS, the oldest item is discarded.
        """
        if key is not None and item is not None:
            # If key is new and cache is at max capacity, discard oldest entry
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)  # Get and remove the first inserted key
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add/Update the item in cache_data and update the order list
            if key in self.cache_data:
                self.order.remove(key)  # Remove key if it already exists to update position
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve item by key from cache_data dictionary.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            Any: The value in cache_data linked to key, or None if key is None
                 or key doesn't exist in cache_data.
        """
        return self.cache_data.get(key, None)
