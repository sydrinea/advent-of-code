import numpy as np
from functools import reduce


def accumulator(acc: int, n: int, i: int, ops: list[str]):
    return acc + n if ops[i] == "+" else acc * n


def partOne(lines: list[str]) -> int:
    G = [line.split() for line in lines]
    problems, ops = np.array(G[0 : len(G) - 1], int).T, G[-1]
    return sum(
        reduce(
            lambda acc, n: accumulator(acc, n, i, ops),
            problem[1:],
            problem[0],
        )
        for i, problem in enumerate(problems)
    )


def partTwo(lines: list[str]) -> int:
    rows = [
        row + [" ", " ", " ", " "]
        for row in [list(line.rstrip()) for line in lines[0 : len(lines) - 1]]
    ]
    ops = lines[-1].split()
    cursor, problem, result = 0, 0, 0
    while 0 <= problem < len(ops):
        l = 0
        for row in rows:
            for i in range(cursor, len(row)):
                if row[i] == " ":
                    l = max(l, i - cursor)
                    break
        nums: list[int] = []
        for i in range(cursor, cursor + l):
            n = ""
            for j in range(0, len(rows)):
                n += rows[j][i]
            nums.append(int(n))
        result += reduce(
            lambda acc, n: accumulator(acc, n, problem, ops),
            nums[1:],
            nums[0],
        )
        cursor += l + 1
        problem += 1
    return result


with open("input/day6.txt") as f:
    lines = f.readlines()
    print(f"Part 1: {partOne(lines)}")
    print(f"Part 2: {partTwo(lines)}")
