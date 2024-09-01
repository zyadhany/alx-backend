#!/usr/bin/env python3
"""
    Simple pagination
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
        get index of id from pages
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get pages from database csv file
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()

        ind = index_range(page=page, page_size=page_size)

        if ind[1] > len(data):
            return []

        return data[ind[0]: ind[1]]
