#!/usr/bin/env python
# -*- coding: utf-8 -*
from typing import ClassVar , List , Tuple
from dataclasses import dataclass
from abc import ABC , abstractmethod
from urllib.parse import SplitResult


@dataclass
class ship (ABC):
    name : str
    position : list[str]
    isActive : int

    def shipLength(self) -> int:
        return len(self.position)

    def shipTouchOrNot (nb : int) -> str :
        resuult = ''
        if nb == 1:
            resuult = "toucher ! "
        elif nb == 0:
            resuult = "deja shooter ici !! "
        else:
            resuult = "looper !!"
        return resuult