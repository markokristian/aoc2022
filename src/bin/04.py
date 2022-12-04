def part1():
    def is_overlap(a, b):
        return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])

    with open("./input/04") as f:
        pairs = [l.rstrip().split(",") for l in f.readlines()]
        pairs = [(p[0].split("-"), p[1].split("-")) for p in pairs]
        pairs = [
            ((int(p[0][0]), int(p[0][1])), (int(p[1][0]), int(p[1][1]))) for p in pairs
        ]
    overlap = 0
    for pair in pairs:
        a, b = pair
        if is_overlap(a, b):
            overlap += 1
    print(overlap)


def part2():
    def is_overlap(a, b):
        r1 = set(list(range(a[0], a[1] + 1)))
        r2 = set(list(range(b[0], b[1] + 1)))
        return len(r1.intersection(r2)) > 0

    with open("./input/04") as f:
        pairs = [l.rstrip().split(",") for l in f.readlines()]
        pairs = [(p[0].split("-"), p[1].split("-")) for p in pairs]
        pairs = [
            ((int(p[0][0]), int(p[0][1])), (int(p[1][0]), int(p[1][1]))) for p in pairs
        ]
    overlap = 0
    for pair in pairs:
        a, b = pair
        if is_overlap(a, b):
            overlap += 1
    print(overlap)


part1()
part2()
