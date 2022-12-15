import ast
from functools import cmp_to_key


def read_input():
    with open("./input/13") as f:
        pairs = [tuple(l.split("\n")) for l in f.read().split("\n\n")]
        for p in pairs:
            yield (ast.literal_eval(p[0]), ast.literal_eval(p[1]))


def compare(l, r):
    l_islist = type(l) == list
    r_islist = type(r) == list
    if l_islist and r_islist:
        if not len(l) + len(r):
            return 0
        if not len(l):
            return -1
        if not len(r):
            return 1
        v1, v2 = l[0], r[0]
        cmp = compare(v1, v2)
        if not cmp:
            return compare(l[1:], r[1:])
        else:
            return cmp
    if not l_islist and r_islist:
        return compare([l], r)
    if l_islist and not r_islist:
        return compare(l, [r])
    if not l_islist and not r_islist:
        return l - r


def part1():
    c, i = 0, 1
    for p in read_input():
        if compare(p[0], p[1]) < 0:
            c += i
        i += 1
    print(c)


def part2():
    l = []
    for p in read_input():
        l.extend(p)
    l.extend([[[2]], [[6]]])
    l = sorted(l, key=cmp_to_key(compare))
    a = l.index([[2]]) + 1
    b = l.index([[6]]) + 1
    print(a * b)


part1()
part2()
