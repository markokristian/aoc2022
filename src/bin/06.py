def part1():
    with open("./input/06") as f:
        msg = [l.rstrip() for l in f.readlines()][0]
    for k in range(0, len(msg) - 3, 1):
        win = msg[k : k + 4]
        if len(set(win)) == 4:
            print(k + 4)
            break


def part2():
    with open("./input/06") as f:
        msg = [l.rstrip() for l in f.readlines()][0]
    for k in range(0, len(msg) - 13, 1):
        win = msg[k : k + 14]
        if len(set(win)) == 14:
            print(k + 14)
            break


part1()
part2()
