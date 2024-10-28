#!/usr/bin/env python3
""" Simple pagination with hypermedia metadata
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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
            List[List]:requested page of data, or empty list if out of range.
        """
        assert isinstance(page, int) and page > 0, "must be a pos int"
        assert isinstance(page_size, int) and page_size > 0, "must be pos int"

        start, end = index_range(page, page_size)  # Determine range for page
        if start >= len(self.dataset()):  # if start index is beyond dataset
            return []

        return self.dataset()[start:end]  # Return the selected slice

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retrieves hypermedia pagination details for the dataset page.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with pagination details and data.
        """
        data = self.get_page(page, page_size)  # Get the current page data
        total_items = len(self.dataset())  # Total numb of items in dataset
        total_pages = math.ceil(total_items / page_size)  # Calcul total page

        # Calculate previous and next page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Build and return the pagination dictionary
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indexes for a pagination range.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    return (page - 1) * page_size, page * page_siz
