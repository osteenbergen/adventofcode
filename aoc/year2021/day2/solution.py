from dataclasses import dataclass
from typing import List, TypeVar

from aoc.lib.reader import input_by_line

TInstruction = TypeVar("TInstruction", bound="Instruction")


@dataclass
class Instruction:
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"
    action: str
    amount: int

    @classmethod
    def from_line(cls, line: str) -> TInstruction:
        parts = line.split(" ")
        return cls(action=parts[0], amount=int(parts[1]))


class Submarine:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0

    def execute(self, inst: Instruction) -> None:
        if inst.action == Instruction.FORWARD:
            self.horizontal += inst.amount
        elif inst.action == Instruction.DOWN:
            self.depth += inst.amount
        elif inst.action == Instruction.UP:
            self.depth -= inst.amount

    def __str__(self):
        return f"{self.__class__.__name__}(h:{self.horizontal}, d:{self.depth})"


class SubmarineV2(Submarine):
    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

    def execute(self, inst: Instruction) -> None:
        if inst.action == Instruction.FORWARD:
            self.horizontal += inst.amount
            self.depth += inst.amount * self.aim
        elif inst.action == Instruction.DOWN:
            self.aim += inst.amount
        elif inst.action == Instruction.UP:
            self.aim -= inst.amount


data: List[int] = input_by_line(year=2021, day=2, convert=Instruction.from_line)

sub = Submarine()
sub2 = SubmarineV2()
for inst in data:
    sub.execute(inst)
    sub2.execute(inst)
print("Part 1:", sub, sub.horizontal * sub.depth)
print("Part 2:", sub2, sub2.horizontal * sub2.depth)
