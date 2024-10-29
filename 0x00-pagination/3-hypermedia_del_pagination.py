#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset if not already loaded.
        Returns:
            List[List]: Cached dataset excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates a dict of dataset ind by position to handle deletions.
        Returns:
            Dict[int, List]: Dict with original ind as key and row as val.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
        self, start_index: int = 0, items_per_page: int = 10
    ) -> Dict[str, Any]:
        """Provides a deletion-resilient pagination.

        Args:
            start_index (int): The starting index for the current page.
            items_per_page (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination details.
        """
        assert isinstance(start_index, int) and start_index >= 0, (
            "Starting index must be a non-negative integer."
        )
        assert isinstance(items_per_page, int) and items_per_page > 0, (
            "Items per page must be a positive integer."
        )

        indexed_data = self.indexed_dataset()
        page_data = []
        iterator_index = start_index

        # Gather items until we fill the page size or exhaust the dataset
        while len(page_data) < items_per_page and
        iterator_index < len(indexed_data):
            if iterator_index in indexed_data:
                page_data.append(indexed_data[iterator_index])
            iterator_index += 1

        # Prepare the result dictionary
        following_index = (
            iterator_index if iterator_index < len(indexed_data) else None
        )
        return {
            "start_index": start_index,
            "following_index": following_index,
            "items_per_page": len(page_data),
            "page_data": page_data,
        }
