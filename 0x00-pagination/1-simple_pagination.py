#!/usr/bin/env python3
""" Simple pagination
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves the correct page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]:requested page of data,or an empty list if out of range
        """
        assert isinstance(page, int) and page > 0, "must be a pos int"
        assert isinstance(page_size, int) and page_size > 0, "must be pos int"

        start, end = index_range(page, page_size)  # Determine range for page
        if start >= len(self.dataset()):  # if start ind is dataset
            return []

        return self.dataset()[start:end]  # Return the selected slice


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indexes for a pagination range.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    return (page - 1) * page_size, page * page_size
