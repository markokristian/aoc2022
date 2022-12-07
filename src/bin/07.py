from collections import defaultdict


def part1():
    with open("./input/07") as f:
        lines = [l.rstrip() for l in f.readlines()]

    szs = defaultdict(lambda: 0)
    current = ["/"]
    for line in lines[1:]:
        s = line.split()
        if s[1] == "cd" and s[2] != "..":
            current.append(s[2])
        elif s[1] == "cd" and s[2] == "..":
            current.pop()
        elif s[1] == "ls" or s[0] == "dir":
            pass
        else:
            size = int(s[0])
            absolute = ""
            for dir in current:
                absolute += dir
                szs[absolute] += size
    sum = 0
    for k, v in szs.items():
        if v <= 100_000:
            sum += v
    print(sum)


def part2():
    with open("./input/07") as f:
        lines = [l.rstrip() for l in f.readlines()]

    szs = defaultdict(lambda: 0)
    current = ["/"]
    for line in lines[1:]:
        s = line.split()
        if s[1] == "cd" and s[2] != "..":
            current.append(s[2])
        elif s[1] == "cd" and s[2] == "..":
            current.pop()
        elif s[1] == "ls" or s[0] == "dir":
            pass
        else:
            size = int(s[0])
            absolute = []
            for dir in current:
                absolute.append(dir)
                szs["/".join(absolute)] += size

    free = 70_000_000 - szs["/"]
    candidates = {key: szs[key] for key in szs if szs[key] > 30_000_000 - free}
    print(candidates[min(candidates, key=candidates.get)])


part1()
part2()
