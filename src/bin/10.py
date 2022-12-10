def part1():
    with open("./input/10") as f:
        ops = [
            (t[0], int(t[1])) if len(t) == 2 else (t[0], 0)
            for t in [tuple(l.rstrip().split()) for l in f.readlines()]
        ]

    x = 1
    xhist = [(1, 0)]
    cycles = 0
    for ins, v in ops:
        if ins == "noop":
            cycles += 1
            xhist.append((x, x * cycles))
        else:
            cycles += 1
            xhist.append((x, x * cycles))
            cycles += 1
            xhist.append((x, x * cycles))
            x += v
    s = 0
    for nth in [20, 60, 100, 140, 180, 220]:
        s += xhist[nth][1]
    print(s)


def part2():
    with open("./input/10") as f:
        ops = [
            (t[0], int(t[1])) if len(t) == 2 else (t[0], 0)
            for t in [tuple(l.rstrip().split()) for l in f.readlines()]
        ]

    x = 1
    xhist = [(1, 0)]
    cycles = 0
    for ins, v in ops:
        if ins == "noop":
            cycles += 1
            xhist.append((x, x * cycles))
        else:
            cycles += 1
            xhist.append((x, x * cycles))
            cycles += 1
            xhist.append((x, x * cycles))
            x += v
    c = 0
    row = ""
    for cycle in xhist[1:]:
        x = cycle[0]
        sprite = [x - 1, x, x + 1]
        row += "#" if c in sprite else "."
        c += 1
        if c % 40 == 0:
            print(row)
            row = ""
            c = 0


part1()
part2()
