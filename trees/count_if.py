from TreeNode import TreeNode
from typing import Callable, TypeVar
T = TypeVar('T')

def count_if(pred: Callable[[T], bool], root: TreeNode) -> int:
    if pred(root.value):
        return 1 + sum(count_if(pred, child) for child in root.children)
    return sum(count_if(pred, child) for child in root.children)

def is_odd(val: int) -> bool:
    return (val%2) == 1

assert count_if(is_odd, TreeNode(1, [])) == 1
assert count_if(is_odd, TreeNode(2, [])) == 0
assert count_if(is_odd, TreeNode(1, [TreeNode(2, [])])) == 1
assert count_if(is_odd, TreeNode(1, [TreeNode(3, [])])) == 2