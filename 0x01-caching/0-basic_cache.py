#!/usr/bin/env python3
""" Basic caching module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a caching system without any limit"""

    def put(self, key, item):
        """Add item to the cache_data dictionary with the given key.
        Args:
            key (str): The key for the item.
            item (Any): The item to store.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item by key from cache_data dictionary.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            Any:value in cache_data linked to key, or None
                 or key doesn't exist in cache_data.
        """
        return self.cache_data.get(key, None)
