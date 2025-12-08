import numpy as np
from itertools import product
from collections import defaultdict, deque

N = 1000


def parse(lines: list[str]):
    return [np.array([int(c) for c in line.split(",")]) for line in lines]


def distance(pair: tuple[np.ndarray, np.ndarray]):
    a, b = pair
    return np.linalg.norm(a - b)


def connected(G: dict[str, set[str]]):
    V: deque[str] = deque(G.keys())
    seen: set[str] = set()
    CC: list[set[str]] = []
    while V:
        o = V.popleft()
        Q: deque[str] = deque([o])
        C: set[str] = set()
        while Q:
            c = Q.popleft()
            if c in seen:
                continue
            seen.add(c)
            C.add(c)
            for neighbor in G[c]:
                Q.append(neighbor)
        CC.append(C)
    return sorted(len(C) for C in CC)


with open("input/day8.txt") as f:
    junctions = parse(f.read().splitlines())
    P = sorted([*product(junctions, junctions)], key=distance)
    G: dict[str, set[str]] = defaultdict(set)
    connections, partOne, partTwo = 0, 0, 0
    for a, b in P:
        if not (a == b).all() and not str(b) in G[str(a)]:
            G[str(a)].add(str(b))
            G[str(b)].add(str(a))
            connections += 1
        sizes = connected(G)
        if connections == N:
            partOne = sizes[-1] * sizes[-2] * sizes[-3]
        if len(sizes) > 0 and sizes[-1] == len(junctions):
            partTwo = a[0] * b[0]
            break
    print(f"Part 1: {partOne}")
    print(f"Part 2: {partTwo}")
