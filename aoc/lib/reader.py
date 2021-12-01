from pathlib import Path
from typing import Any, Callable, List


def input_by_line(
    year: int, day: int, name: str = None, convert: Callable[[str], Any] = None
) -> List[Any]:
    """
    Read input file to a list

    args:
        year: Year
        day: Day number
        name: Optional filename, default "input"
        convert: Optional conversion function
    """
    if name is None:
        name = "input"
    text = Path(f"./aoc/year{year}/day{day}/{name}.txt").read_text()
    lines = text.strip().splitlines()
    if not convert:
        return lines
    return [convert(line) for line in lines]
