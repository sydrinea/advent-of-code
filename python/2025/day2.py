from collections.abc import Callable


def partOne(n: str):
    return n[0 : len(n) // 2] == n[len(n) // 2 :]


def partTwo(n: str):
    for div in filter(lambda div: len(n) % div == 0, range(2, len(n) + 1)):
        step = len(n) // div
        nums = set([n[i : i + step] for i in range(0, len(n), step)])
        if len(nums) == 1:
            return True
    return False


def solve(inp: str, fn: Callable[[str], bool] = partOne):
    ranges = [[*map(int, x.split("-"))] for x in inp.split(",")]
    return sum(n if fn(str(n)) else 0 for (lo, hi) in ranges for n in range(lo, hi + 1))


with open("input/day2.txt") as f:
    inp = f.read().strip()
    print(f"Part 1: {solve(inp)}")
    print(f"Part 2: {solve(inp, fn=partTwo)}")
