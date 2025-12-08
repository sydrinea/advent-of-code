from functools import cache


def start(G: list[list[str]]):
    return next(
        filter(
            lambda col: G[0][col] == "S",
            [col for col in range(0, len(G[0]))],
        )
    )


def partOne(G: list[list[str]]) -> int:
    S, beams = start(G), [False for _ in range(0, len(G[0]))]
    beams[S] = True
    splits = 0
    for r in G[1:]:
        scratch = beams.copy()
        for c in range(0, len(r)):
            if r[c] == "^" and beams[c]:
                splits += 1
                scratch[c] = False
                for d in [-1, 1]:
                    if 0 <= c + d <= len(r):
                        scratch[c + d] = True
        beams = scratch
    return splits


def partTwo(G: list[list[str]]):
    @cache
    def solve(position: tuple[int, int]) -> int:
        r, c = position
        # if we are at the end, this concludes the timeline
        if not (0 <= r < len(G) and 0 <= c < len(G[r])):
            return 1
        return (
            solve((r + 1, c))
            if G[r][c] == "."
            else solve((r + 1, c - 1)) + solve((r + 1, c + 1))
        )

    return solve((0, start(G)))


with open("input/day7.txt") as f:
    G = [list(line) for line in f.read().splitlines()]
    print(f"Part 1: {partOne(G)}")
    print(f"Part 2: {partTwo(G)}")
