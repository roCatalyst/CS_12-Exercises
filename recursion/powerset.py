from typing import Sequence, TypeVar
T = TypeVar('T')

def helper(elems: Sequence[T], i: int) -> list[list[T]]:
    if i == 1 << len(elems): return []

    curr: list[T] = []
    for bit in range(len(elems)):
        if (i & (1<<bit)):
            curr.append(elems[bit])
    return [curr] + helper(elems, i+1)

def powerset(elems: Sequence[T]) -> list[list[T]]:
    ret: list[list[T]] = helper(elems, 0)
    return ret

powerset([]) == [[]]
powerset(['a']) == [[], ['a']]
powerset(['a', 'b']) == [[], ['a'], ['b'], ['a', 'b']]
powerset(['a', 'b', 'c']) == [[], ['a'], ['b'], ['c'], ['a', 'b'], ['b', 'c'], ['a', 'c'], ['a', 'b', 'c']]