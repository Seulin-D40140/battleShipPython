#!/usr/bin/env python
# -*- coding: utf-8 -*

from typing import ClassVar , List , Tuple
from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class gridM (ABC):
    map : list[list[str]]

    # @classmethod
    # def shipLenght(cls) ->int:
    #     return len(cls.position)