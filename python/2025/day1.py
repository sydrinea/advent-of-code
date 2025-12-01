def part1(ops: list[tuple[str, int]]) -> int:
    dial = 50
    password = 0
    for (dir, n) in ops:
        if dir == 'L': dial -= n
        elif dir == 'R': dial += n
        dial %= 100
        if dial == 0: password += 1
    return password

def part2(ops: list[tuple[str, int]]) -> int:
    dial = 50
    password = 0
    for (dir, n) in ops:
        for _ in range(0, abs(n)):
            if dir == 'L': dial -= 1
            elif dir == 'R': dial += 1 
            dial %= 100
            if dial == 0: password += 1
    return password

with open("input/day1.txt") as f:
    ops = [(x[0], int(str(x[1:]).strip())) for x in f.readlines()]
    print(f'Part 1: {part1(ops)}')
    print(f'Part 2: {part2(ops)}')
