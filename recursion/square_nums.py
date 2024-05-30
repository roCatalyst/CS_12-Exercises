from typing import Sequence

def square_nums(elems: Sequence[int]) -> list[int]:
    return [ elems[0]**2 ] + square_nums(elems[1:]) if len(elems) > 0 else []

assert square_nums([]) == []
assert square_nums([1]) == [1]
assert square_nums([1, 2]) == [1,4]
assert square_nums([1,2,3]) == [1,4,9]