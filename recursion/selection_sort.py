from typing import Sequence
from my_max import my_max

def selection_sort(elems: Sequence[int]) -> list[int]:
    if len(elems) == 0: return []
    mx: int = my_max(elems)
    i: int = elems.index(mx)
    return selection_sort(elems[:i] + elems[i+1:]) + [elems[i]]

assert selection_sort([]) == []
assert selection_sort([1]) == [1]
assert selection_sort([20, 10]) == [10, 20]
assert selection_sort([10, 20, 30]) == [10, 20, 30]
assert selection_sort([30, 10, 20]) == [10, 20, 30]
assert selection_sort([30, 20, 10]) == [10, 20, 30]