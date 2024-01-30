#!/usr/bin/env
"""helper function for pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves index range
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
