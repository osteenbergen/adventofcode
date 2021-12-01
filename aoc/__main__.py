import sys
from importlib import import_module

if len(sys.argv) != 3:
    print("aoc <year> <day>")
    sys.exit(1)

# Run solution
import_module(f"aoc.year{sys.argv[1]}.day{sys.argv[2]}.solution")
