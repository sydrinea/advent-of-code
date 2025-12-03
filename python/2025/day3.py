from functools import reduce


def choose(bank: list[int], size: int = 2) -> int:
    selection: list[int] = []
    batteries: dict[int, list[int]] = {n: [] for n in bank}
    for index, n in enumerate(bank):
        batteries[n].append(index)
    threshold: int = -1
    for _ in range(0, size):
        for target in reversed(range(1, 10)):
            if target not in batteries.keys():
                continue
            candidates = [*filter(lambda n: n > threshold, batteries[target])]
            if len(candidates) > 0:
                best = min(candidates)
                if len(bank) - best >= size - len(selection):
                    batteries[target].remove(best)
                    selection.append(target)
                    threshold = best
                    break
    return int(reduce(lambda acc, n: acc + str(n), selection, ""))


def solve(banks: list[list[int]], size: int = 2):
    return sum(choose(bank, size) for bank in banks)


with open("input/day3.txt") as f:
    banks = [[int(x) for x in list(line.strip())] for line in f.readlines()]
    print(f"Part 1: {solve(banks)}")
    print(f"Part 2: {solve(banks, size=12)}")
