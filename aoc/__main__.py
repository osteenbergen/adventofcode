import sys
from importlib import import_module

if len(sys.argv) != 2:
    print("aoc <day>")
    sys.exit(1)

# Run solution
import_module(f"aoc.days.day{sys.argv[1]}.solution")
