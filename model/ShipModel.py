#!/usr/bin/env python
# -*- coding: utf-8 -*
from typing import ClassVar , List , Tuple
from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class ship (ABC):
    name : str
    position : list[str]
    isActive : int

    def shipLength(self) -> int:
        return len(self.position)