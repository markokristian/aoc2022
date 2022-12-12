import heapq


def print_g(g):
    maxx, maxy = max(g)
    for y in range(0, maxy + 1):
        s = "".join([str(g[(x, y)]).rjust(4) for x in range(0, maxx + 1)])
        print(s)


def input(file_name):
    with open(file_name) as f:
        y = 0
        x = 0
        g = {}
        for line in f:
            for cost in line.rstrip():
                if cost == "S":
                    g[(x, y)] = ord("a")
                    S = (x, y)
                elif cost == "E":
                    g[(x, y)] = ord("z")
                    E = (x, y)
                else:
                    g[(x, y)] = ord(cost)
                x += 1
            y += 1
            x = 0
        return (g, S, E)


def adj(pos, g, max):
    x, y = pos
    a = [
        None if x == 0 else (x - 1, y),
        None if y == max[1] else (x, y + 1),
        None if y == 0 else (x, y - 1),
        None if x == max[0] else (x + 1, y),
    ]
    return [(pos, g[pos]) for pos in a if pos is not None]


# with regards to elevation rule
def possible(current_elevation, locations):
    for pos, elevation in locations:
        if elevation - current_elevation <= 1:
            yield (pos, elevation)


def dijkstra(g, start, goal, max):
    q = []
    d = {k: 100000000 for k in g.keys()}
    p = {}
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        last_cost, current = heapq.heappop(q)
        for pos, elevation in possible(g[current], adj(current, g, max)):
            dist = last_cost + 1
            if dist < d[pos]:
                d[pos] = dist
                p[pos] = current
                heapq.heappush(q, (dist, pos))
    return d[goal]


def part1():
    g, S, E = input("./input/12")
    print(dijkstra(g, start=S, goal=E, max=max(g)))


def part2():
    starts = []
    dists = []
    g, _, E = input("./input/12")
    for pos, elevation in g.items():
        if elevation == ord("a"):
            starts.append(pos)
    for a in starts:
        dists.append(dijkstra(g, start=a, goal=E, max=max(g)))
    print(min(dists))


# part1()
part2()
