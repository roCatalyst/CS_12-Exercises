from insert import insert
from typing import Sequence

def insertion_sort(elems: Sequence[int]) -> list[int]:
    return insert(elems[0], insertion_sort(elems[1:])) if len(elems) > 0 else []

assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([20, 10]) == [10, 20]
assert insertion_sort([10, 20, 30]) == [10, 20, 30]
assert insertion_sort([30, 10, 20]) == [10, 20, 30]
assert insertion_sort([30, 20, 10]) == [10, 20, 30]