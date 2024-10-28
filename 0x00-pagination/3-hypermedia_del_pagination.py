#!/usr/bin/env python3
"""
hypermedia pagination
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
        """Creates a dict of dataset indexed by position to handle deletions.

        Returns:
            Dict[int, List]:Dict with original ind as key and row as value.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """
        Provides a deletion-resilient pagination.

        Args:
            index (int): The starting index for the current page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination details.
        """
        assert isinstance(index, int) and 0 <= index, "be a non-negative int."
        assert isinstance(page_size, int) and page_size > 0, "must be a pos int"

        indexed_data = self.indexed_dataset()
        csv_size = len(indexed_data)
        assert index < csv_size, "Index out of range."

        data = []
        current_index = index
        items_collected = 0

        # Collect `page_size` items, skipping deletentries if necessary
        while items_collected < page_size and current_index < csv_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        # `next_index` will be next valid index after last item in page
        next_index = current_index if current_index < csv_size else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }