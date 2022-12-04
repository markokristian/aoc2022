def part1():
    with open("./input/03") as f:
        sacks = [l for l in f.readlines()]
    psum = 0
    for sack in sacks:
        n = len(sack)
        a = set(sack[0 : n // 2])
        b = set(sack[n // 2 :])
        for c in a.intersection(b):
            psum += ord(c) - 38 if c.isupper() else ord(c) - 96
    print(psum)


def part2():
    with open("./input/03") as f:
        sacks = [l.rstrip() for l in f.readlines()]
    psum = 0

    def prio(sets):
        psum = 0
        for c in set.intersection(*sets):
            psum += ord(c) - 38 if c.isupper() else ord(c) - 96
        return psum

    for k in range(0, len(sacks), 3):
        psum += prio([set(sacks[k]), set(sacks[k + 1]), set(sacks[k + 2])])
    print(psum)


part1()
part2()
