#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate first and last indexes for a pagination range based on page num
    and num of items per page (page_size).
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        Tuple[int, int]:tuple containing first index and last index for requested page.
    """
    first_index = (page - 1) * page_size  # Calculate first index for the given page
    last_index = first_index + page_size  # Calculate last index based on first index
    return first_index, last_index
