with open("input/day5.txt") as f:
    lines = f.read()
    ranges, ids = [section.split("\n") for section in lines.split("\n\n")]
    count = 0
    for id in ids:
        for r in ranges:
            lower, upper = [int(half) for half in r.split("-")]
            if lower <= int(id) <= upper:
                count += 1
                break
    print(f"Part 1: {count}")
