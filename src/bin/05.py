import re
from collections import defaultdict


def part1():
    with open("./input/05") as f:
        lines = [l.rstrip() for l in f.readlines()]

    stacks = defaultdict(lambda: [])
    pattern = re.compile("\[[A-Z]\]")
    for line in lines:
        if not line:
            break
        for m in pattern.finditer(line):
            idx = 1 if m.start() == 0 else (m.start() // 4) + 1
            stacks[idx].insert(0, m.group().replace("[", "").replace("]", ""))

    pattern = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    for line in lines:
        gs = re.search(pattern, line)
        if not gs:
            continue
        n, source, dest = gs.groups()
        n, source, dest = int(n), int(source), int(dest)
        for _ in range(0, n):
            item = stacks[source].pop()
            stacks[dest].append(item)
        stacks

    s = ""
    for idx in range(1, len(stacks) + 1):
        s += stacks[idx].pop()
    print(s)


def part2():
    with open("./input/05") as f:
        lines = [l.rstrip() for l in f.readlines()]

    stacks = defaultdict(lambda: [])
    pattern = re.compile("\[[A-Z]\]")
    for line in lines:
        if not line:
            break
        for m in pattern.finditer(line):
            idx = 1 if m.start() == 0 else (m.start() // 4) + 1
            stacks[idx].insert(0, m.group().replace("[", "").replace("]", ""))

    pattern = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    for line in lines:
        gs = re.search(pattern, line)
        if not gs:
            continue
        n, source, dest = gs.groups()
        n, source, dest = int(n), int(source), int(dest)
        items = []
        for _ in range(0, n):
            items.append(stacks[source].pop())
        items.reverse()
        stacks[dest].extend(items)
        stacks

    s = ""
    for idx in range(1, len(stacks) + 1):
        s += stacks[idx].pop()
    print(s)


part1()
part2()
