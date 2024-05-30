from typing import Sequence, TypeVar
T = TypeVar('T')

def is_member(elem: T, elems: Sequence[T]) -> bool:
    return (elems[-1] == elem) or is_member(elem, elems=elems[:-1]) if len(elems) > 0 else False

assert is_member(0, []) == False
assert is_member(0, [0]) == True
assert is_member(0, [1,2]) == False
assert is_member('c', ['a', 'b', 'c']) == True