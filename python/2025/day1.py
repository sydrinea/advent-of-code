def single(ops: list[tuple[str, int]]) -> int:
    dial, password = 50, 0
    for (dir, n) in ops:
        dial += -n if dir == 'L' else n
        dial %= 100
        if dial == 0: password += 1
    return password

def any(ops: list[tuple[str, int]]) -> int:
    dial, password = 50, 0
    for (dir, n) in ops:
        for _ in range(0, abs(n)):
            dial += -1 if dir == 'L' else 1
            dial %= 100
            if dial == 0: password += 1
    return password

with open("input/day1.txt") as f:
    ops = [(x[0], int(str(x[1:]).strip())) for x in f.readlines()]
    print(f'Part 1: {single(ops)}')
    print(f'Part 2: {any(ops)}')
