#!/usr/bin/env python
# -*- coding: utf-8 -*

from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class gridM (ABC):
    map : list[list[str]]

    def __getitem__(self, index):
        return self.map[index]

    def display (table: list[list[str]]):
        print("  |  A  |   B  |   C  |   D  |   E  |   F  |   G  |   H  |   I  |   J  |")
        for i in range(10):
            print(i + 1, table[i])

    def displayOnGrid ( table : list[list[str]] ,nb : int , nbletter: int , letter : str ):
        table[nb - 1][nbletter] = letter
