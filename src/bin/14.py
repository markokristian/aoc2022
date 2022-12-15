import numpy as np
from collections import defaultdict


def read_input():
    with open("./input/14") as f:
        return [
            [
                tuple([int(val) for val in pos.split(",")])
                for pos in l.rstrip().split(" -> ")
            ]
            for l in f.readlines()
        ]


def print_g(g, minx, maxx, miny, maxy):
    for y in range(miny, maxy + 1):
        s = "".join([str(g[(x, y)]) for x in range(minx, maxx + 1)])
        print(s)


def part1():
    paths = read_input()

    # map
    flat = [item for sublist in paths for item in sublist]
    ymax = max([y for _, y in flat])

    # part 2
    paths.append([(0, ymax + 2), (1000, ymax + 2)])
    ymax += 2

    xmax = max([x for x, _ in flat])
    ymin = 0  # source of sand
    xmin = min([x for x, _ in flat])

    # part 2
    xmin = 0
    xmax = 1000

    # render paths
    render = set()
    for path in paths:
        p = 0
        k = 0
        while k + 1 < len(path):
            between = np.linspace(
                path[k],
                path[k + 1],
                num=max(abs(np.subtract(path[k], path[k + 1]))) + 1,
                dtype=int,
            )
            render.update([tuple(x) for x in between])
            k += 1
        p += 1
    # print("rocks", len(render))
    paths = render

    # construct map
    grid = defaultdict(lambda: ())
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            grid[(x, y)] = "#" if (x, y) in paths else "."

    # place start sand
    grid[(500, 0)] = "+"

    # sand thing
    sx, sy = (500, 0)
    k = 0
    while 1:
        # print("\nstep %s" % (k + 1))
        adj = [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]

        # done?
        # outside = [
        #     a for a in adj if a[0] < xmin or a[0] > xmax or a[1] < ymin or a[1] > ymax
        # ]
        # if len(outside) > 0:
        #     print("done after %s steps" % k)
        #     print_g(grid, xmin, xmax, ymin, ymax)
        #     break

        blocked = 0
        for a in adj:
            if grid[a] in ["#", "o"]:
                blocked += 1
            else:
                grid[(sx, sy)] = "."
                sx, sy = a  # move sand to next adj
                grid[(sx, sy)] = "+"
                break

        if blocked == 3:  # more sand needed
            # at rest
            grid[(sx, sy)] = "o"
            if (sx, sy) == (500, 0):
                print("done part 2")
                break
            sx, sy = (500, 0)
            grid[(sx, sy)] = "+"

        k += 1

    print(len([v for v in grid.values() if v == "o"]))


part1()
