#!/usr/bin/env python3
"""
Simple helper function for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate first and last index for a specific page in pagination.

    Args:
        page (int): The page number, starting from 1.
        page_size (int): total number of items to display on each page.
    Returns:
        Tuple[int, int]: A tuple containing the first and last indexes
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index
