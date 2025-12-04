directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def accessible(G: list[list[str]]):
    def inside(adj: tuple[int, int]):
        return 0 <= r + adj[0] < len(G) and 0 <= c + adj[1] < len(G[r])

    result: set[tuple[int, int]] = set()
    for r, c in [(r, c) for r in range(0, len(G)) for c in range(0, len(G[r]))]:
        if G[r][c] == "@":
            count = sum(
                int(G[r + dr][c + dc] == "@") for dr, dc in filter(inside, directions)
            )
            if count < 4:
                result.add((r, c))
    return result


def remove(G: list[list[str]]) -> int:
    removed, rolls = 0, accessible(G)
    while len(rolls) > 0:
        for r, c in rolls:
            G[r][c] = "."
        removed += len(rolls)
        rolls = accessible(G)
    return removed


with open("input/day4.txt") as f:
    G = [list(line.strip()) for line in f.readlines()]
    print(f"Part 1: {len(accessible(G))}")
    print(f"Part 2: {remove(G)}")
