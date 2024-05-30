from typing import Sequence
import math

def my_max(elems: Sequence[int]) -> int:
    if len(elems) == 0:
        return -math.inf
    others: int = my_max(elems[1:])
    if elems[0] > others: return elems[0]
    return others

my_max([1]) == 1
my_max([20, 10]) == 20
my_max([10, 20, 30]) == 30
my_max([30, 10, 20]) == 30
my_max([30, 20, 10]) == 30