def part1():
    mapping = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    outcomes = {-1: 0, 2: 0, -2: 6, 1: 6}
    with open("./input/02") as f:
        lines = f.readlines()
        rounds = [l.rstrip().split(" ") for l in lines]
        score = 0
        for r in rounds:
            opp, me = mapping[r[0]], mapping[r[1]]
            score += 3 if me == opp else outcomes[me - opp]
            score += me
    print(score)

def part2():
    mapping = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
    # 1 rock 2 paper 3 scissors
    outcomes = {
        1: {6: 2, 0: 3, 3: 1},
        2: {0: 1, 6: 3, 3: 2},
        3: {6: 1, 0: 2, 3: 3},
    }
    with open("./input/02") as f:
        lines = f.readlines()
        rounds = [l.rstrip().split(" ") for l in lines]
        score = 0
        for r in rounds:
            opp, outcome = mapping[r[0]], mapping[r[1]]
            me = outcomes[opp][outcome]
            score += outcome + me
    print(score)

part1()
part2()
