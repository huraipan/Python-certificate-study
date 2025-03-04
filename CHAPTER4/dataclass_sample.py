# -*- coding: utf-8 -*-
"""dataclass_sample.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jRyzyjErBXFlskZpymjHGVoJsyJmTgxd
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    address: str

@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int
    address: str

@dataclass
class User2:
    name: str
    age: int
    address: str
    active: bool = False