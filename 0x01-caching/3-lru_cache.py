#!/usr/bin/env python3
""" LRU caching module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a caching system with LRU eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.c_d = self.cache_data
        self.access_order = []  # List to track order access for LRU

    def put(self, key, item):
        """Add item to the c_d dictionary with LRU eviction policy.
        Args:
            key (str): The key for the item.
            item (Any): The item to store.
        If key or item is None, this method does nothing.
        If cache exceeds BaseCaching.MAX_ITEMS,least recently discarded.
        """
        if key is not None and item is not None:
            # If key is new and cache is at max capacity, discard LRU entry
            if key not in self.c_d and len(self.c_d) >= BaseCaching.MAX_ITEMS:
                lru_key = self.access_order.pop(0)  # Get and remove
                del self.c_d[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add/Update the item in c_d and update access order
            if key in self.c_d:
                self.access_order.remove(key)  # Remove
            self.c_d[key] = item
            self.access_order.append(key)  # Mark as recently

    def get(self, key):
        """Retrieve item by key from c_d dictionary.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            Any:value in c_d linked to key, or None if key
                 or key doesn't exist in c_d.
        """
        if key in self.c_d:
            # Update access order to mark key as recently used
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.c_d[key]
        return None
