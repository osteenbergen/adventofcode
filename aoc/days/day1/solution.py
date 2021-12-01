from typing import List

from aoc.lib.reader import input_by_line

data: List[int] = input_by_line(day=1, convert=int)

previous: int = 0
increases: int = 0
for depth in data:
    if previous == 0:
        previous = depth
        continue
    if previous < depth:
        increases += 1
    previous = depth

print(f"Part 1: {increases}")

window: List[int] = []
increases = 0
for depth in data:
    window.append(depth)
    length: int = len(window)
    if length < 4:
        continue
    if length > 4:
        window.pop(0)

    if sum(window[:3]) < sum(window[1:4]):
        increases += 1

print(f"Part 2: {increases}")
