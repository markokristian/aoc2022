import numpy as np


def part1():
    with open("./input/09") as f:
        motions = [
            (t[0], int(t[1]))
            for t in [tuple(l.rstrip().split()) for l in f.readlines()]
        ]

    class Rope:
        def __init__(self):
            self.head = (0, 0)
            self.tail = (0, 0)
            self.head_hist = [(0, 0)]
            self.tail_hist = [(0, 0)]

        dirs = {
            "R": (1, 0),
            "L": (-1, 0),
            "D": (0, 1),
            "U": (0, -1),
        }

        def move(self, motion):
            def is_adj(h, t):
                aligned = h[0] == t[0] or h[1] == t[1]
                dist = sum(abs(np.subtract(h, t)))
                same = h[0] == t[0] and h[1] == t[1]
                return (aligned and dist == 1) or (not aligned and dist == 2) or same

            dir, mag = self.dirs[motion[0]], motion[1]
            for _ in range(mag):
                self.head = tuple(np.add(dir, self.head).tolist())
                self.head_hist.append(self.head)

                if not is_adj(self.head, self.tail):
                    self.tail = self.head_hist[-2]
                    self.tail_hist.append(self.tail)

    ht = Rope()
    for m in motions:
        ht.move(m)

    print(len(set(ht.tail_hist)))


def part2():
    with open("./input/09") as f:
        motions = [
            (t[0], int(t[1]))
            for t in [tuple(l.rstrip().split()) for l in f.readlines()]
        ]

    class Rope:
        def __init__(self):
            self.tails = [(0, 0) for _ in range(10)]
            self.hists = [[(0, 0)] for _ in range(10)]

        dirs = {
            "R": (1, 0),
            "L": (-1, 0),
            "D": (0, 1),
            "U": (0, -1),
        }

        def move(self, motion):
            def is_adj(h, t):
                aligned = h[0] == t[0] or h[1] == t[1]
                dist = sum(abs(np.subtract(h, t)))
                same = h[0] == t[0] and h[1] == t[1]
                return (aligned and dist == 1) or (not aligned and dist == 2) or same

            dir, mag = self.dirs[motion[0]], motion[1]
            for _ in range(mag):

                self.tails[0] = tuple(np.add(dir, self.tails[0]).tolist())
                self.hists[0].append(self.tails[0])

                for k in range(1, len(self.tails)):
                    if not is_adj(self.tails[k - 1], self.tails[k]):
                        diff = np.subtract(self.tails[k - 1], self.tails[k])
                        self.tails[k] = tuple(
                            np.add(
                                self.tails[k],
                                np.sign(diff),
                            ).tolist()
                        )
                        self.hists[k].append(self.tails[k])

    ht = Rope()
    for m in motions:
        ht.move(m)

    print(len(set(ht.hists[-1])))


part1()
part2()
