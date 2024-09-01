#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
            get hyper index
        """

        db_data = []

        for key, val in self.indexed_dataset().items():
            db_data.append([key, val])

        st = -1
        mx = -1

        for i in range(len(db_data)):
            if db_data[i][0] >= index and st is -1:
                st = i
            mx = max(mx, db_data[i][0])

        assert isinstance(index, int) and index >= 0 and index <= mx

        data = []
        if st != -1:
            for i in range(page_size):
                if i + st < len(db_data):
                    data.append(db_data[st + i][1])

        next_index = None
        st += page_size
        if st < len(db_data):
            next_index = db_data[st][0]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
