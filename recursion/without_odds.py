from typing import Sequence

def without_odds(elems: Sequence[int]) -> list[int]:
    if len(elems) == 0:
        return []
    
    if elems[0] % 2 == 0:
        return [elems[0]] + without_odds(elems[1:])
    return without_odds(elems[1:])

assert without_odds([]) == []
assert without_odds([1]) == []
assert without_odds([2]) == [2]
assert without_odds([1, 2]) == [2]
assert without_odds([2, 1]) == [2]
assert without_odds([1, 3, 5]) == []
assert without_odds([1, 2, 3, 4, 5]) == [2, 4]
