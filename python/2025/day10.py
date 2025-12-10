from z3 import Int, Solver, sat, ArithRef  # type: ignore
from collections import deque


def parse(l: list[str], s: str):
    return [[int(n) for n in el.strip(s).split(",")] for el in l]


def buttonToVector(N: int, l: list[str], s: str):
    buttons: list[list[int]] = []
    for el in l:
        button = [0 for _ in range(0, N)]
        i = el.strip(s).split(",")
        for n in i:
            button[int(n)] = 1
        buttons.append(button)
    return buttons


def apply(schematic: list[bool], button: list[int]):
    scratch = schematic.copy()
    for i in button:
        scratch[i] = not schematic[i]
    return scratch


def partOne(schematic: list[bool], buttons: list[list[int]], joltages: list[int]):
    Q: deque[tuple[list[bool], list[list[int]]]] = deque(
        [([False for _ in range(0, len(schematic))], [])]
    )
    seen: set[str] = set()
    while Q:
        state, sequence = Q.popleft()
        if state == schematic:
            return len(sequence)
        if str(state) in seen:
            continue
        seen.add(str(state))
        for button, next in [(button, apply(state, button)) for button in buttons]:
            Q.append((next, sequence + [button]))
    return 10**32


def once(joltages: list[int], buttons: list[list[int]], bound: int) -> tuple[int, bool]:
    xs: list[ArithRef] = []
    for i in range(0, len(buttons)):
        xs.append(Int(f"x{i}"))
    s = Solver()
    for x in xs:
        s.add(x >= 0)  # type: ignore
    s.add(sum(xs) <= bound)  # type: ignore
    for col in range(0, len(joltages)):
        relevant: list[ArithRef] = []
        for row in range(0, len(buttons)):
            if buttons[row][col] == 1:
                relevant.append(xs[row])
        s.add(sum(relevant) == joltages[col])  # type: ignore
    v = s.check()  # type: ignore
    if v == sat:
        m = s.model()  # type: ignore
        return sum(m[x].py_value() for x in xs), True  # type: ignore
    return 10**32, False


def partTwo(line: list[str], joltages: list[int]):
    buttons = buttonToVector(len(joltages), line[1 : len(line) - 1], "()")
    current, solved = once(joltages, buttons, 10**32)
    best = current
    while True:
        next, solved = once(joltages, buttons, current - 1)
        best = min(current, next)
        current = next
        if not solved:
            return best


with open("input/day10.txt") as f:
    lines = [line.split(" ") for line in f.read().splitlines()]
    pressesI, pressesJ = 0, 0
    for line in lines:
        schematic, buttons, joltages = (
            [c == "#" for c in line[0][1 : len(line[0]) - 1]],
            parse(line[1 : len(line) - 1], "()"),
            parse([line[-1]], "{{}}")[0],
        )
        pressesI += partOne(schematic, buttons, joltages)
        pressesJ += partTwo(line, joltages)
    print(f"Part 1: {pressesI}")
    print(f"Part 2: {pressesJ}")
