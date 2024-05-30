from typing import Sequence, TypeVar
T = TypeVar('T')

def reverse(elems: Sequence[T]) -> list[T]:
    return [ elems[-1] ] + reverse(elems[:-1]) if len(elems) > 0 else []

assert reverse([]) == []
assert reverse([1]) == [1]
assert reverse([1,2]) == [2,1]
assert reverse([1,2,3]) == [3,2,1]