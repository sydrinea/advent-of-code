from itertools import product


def rectArea(a: list[int], b: list[int]) -> int:
    return abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)


def partOne(coordinates: list[list[int]]):
    return max(rectArea(list(a), list(b)) for a, b in product(coordinates, coordinates))


with open("input/day9.txt") as f:
    coordinates = [[int(c) for c in line.split(",")] for line in f.read().splitlines()]
    print(f"Part 1: {partOne(coordinates)}")
