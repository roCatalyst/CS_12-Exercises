from __future__ import annotations
from typing import Generic, TypeVar
from dataclasses import dataclass
 
 
T = TypeVar('T')
 
@dataclass
class TreeNode(Generic[T]):
    value: T
    children: list[TreeNode[T]]