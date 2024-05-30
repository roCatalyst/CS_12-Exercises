from typing import Sequence

def insert(elem: int, sorted_elems: Sequence[int]) -> list[int]:
    if len(sorted_elems) == 0: return [elem]
    if elem > sorted_elems[-1]: return sorted_elems + [elem]
    return insert(elem, sorted_elems[:-1]) + [sorted_elems[-1]]

assert insert(1, []) == [1]
assert insert(5, [10, 20, 30]) == [5, 10, 20, 30]
assert insert(15, [10, 20, 30]) == [10, 15, 20, 30]
assert insert(25, [10, 20, 30]) == [10, 20, 25, 30]
assert insert(35, [10, 20, 30]) == [10, 20, 30, 35]

