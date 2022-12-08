def part1():
    with open("./input/08") as f:
        l = [[int(num) for num in line.strip()] for line in f]

    visible = set()
    max = 0

    for row in range(0, len(l)):
        for col in range(0, len(l)):
            d = l[row][col]
            if d > max or col == 0:
                max = d
                visible.add((row, col))

    for row in range(0, len(l)):
        for col in range(len(l) - 1, -1, -1):
            d = l[row][col]
            if d > max or col == len(l) - 1:
                max = d
                visible.add((row, col))

    for col in range(0, len(l)):
        for row in range(0, len(l)):
            d = l[row][col]
            if d > max or row == 0:
                max = d
                visible.add((row, col))

    for col in range(0, len(l)):
        for row in range(len(l) - 1, -1, -1):
            d = l[row][col]
            if d > max or row == len(l) - 1:
                max = d
                visible.add((row, col))

    print(len(visible))


def part2():
    with open("./input/08") as f:
        l = [[int(num) for num in line.strip()] for line in f]

    def score(r, c):
        if c == 0 or r == 0 or c == len(l) - 1 or r == len(l) - 1:
            return 0

        tree = l[r][c]
        left = 0
        for col in range(c - 1, -1, -1):
            d = l[r][col]
            left += 1
            if d >= tree:
                break

        right = 0
        for col in range(c + 1, len(l)):
            d = l[r][col]
            right += 1
            if d >= tree:
                break

        up = 0
        for row in range(r - 1, -1, -1):
            d = l[row][c]
            up += 1
            if d >= tree:
                break

        down = 0
        for row in range(r + 1, len(l)):
            d = l[row][c]
            down += 1
            if d >= tree:
                break

        return left * right * up * down

    max = 0
    for col in range(0, len(l)):
        for row in range(0, len(l)):
            s = score(row, col)
            if s > max:
                max = s
    print(max)


part1()
part2()
