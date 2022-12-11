import math


def parse():
    with open("./input/11") as f:
        lines = [l.rstrip() for l in f.readlines()]
    monkeys = {}
    for line in lines:
        if line.startswith("Monkey "):
            id = int(line.split(" ")[1][:-1])
            m = {"id": id, "inspections": 0}
            monkeys[id] = m
            continue
        if "Starting items" in line:
            m["items"] = [int(n) for n in line.split(":")[1].strip().split(",")]
            continue
        if "Operation" in line:
            operation = line.split(":")[1].strip()
            m["op_operand_l"] = "old"
            m["op_operator"] = operation.split(" ")[3]
            m["op_operand_r"] = operation.split(" ")[4]
            continue
        if "Test: " in line:
            test = line.split(":")[1].strip()
            m["candivby"] = int(test.split(" ")[-1])
            continue
        if "If true" in line:
            iftrue = line.split(":")[1].strip()
            m["true_monkey"] = int(iftrue.split(" ")[-1])
            continue
        if "If false" in line:
            iffalse = line.split(":")[1].strip()
            m["false_monkey"] = int(iffalse.split(" ")[-1])
            continue
    return monkeys


def part1():
    monkeys = parse()
    opmap = {"+": sum, "*": math.prod}

    for _ in range(20):
        for m in monkeys.values():
            while m["items"]:
                worry = m["items"][0]
                m["inspections"] += 1

                # apply op
                op = opmap[m["op_operator"]]
                if m["op_operand_r"] == "old":
                    worry = op([worry, worry])
                else:
                    worry = op([worry, int(m["op_operand_r"])])

                # div by three
                worry = worry // 3

                # test
                destination = None
                if worry % m["candivby"] == 0:
                    destination = m["true_monkey"]
                else:
                    destination = m["false_monkey"]

                # throw to monkey
                monkeys[destination]["items"].append(worry)
                m["items"] = m["items"][1:]

    insp = []
    for m in monkeys.values():
        insp.append(m["inspections"])

    print(math.prod(sorted(insp, reverse=True)[:2]))


def part2():
    monkeys = parse()
    opmap = {"+": sum, "*": math.prod}
    md = math.prod([f["candivby"] for f in monkeys.values()])

    def print_state(monkeys):
        for m in monkeys.values():
            print("monkey {}: {}".format(m["id"], m["inspections"]))

    for k in range(10000):
        for m in monkeys.values():
            while m["items"]:
                worry = m["items"][0]
                m["inspections"] += 1

                # apply op
                op = opmap[m["op_operator"]]
                if m["op_operand_r"] == "old":
                    worry = op([worry, worry])
                else:
                    worry = op([worry, int(m["op_operand_r"])])

                # all tests are divisions, create the common factor for all division tests
                # keep the remainder to maintain modulo
                worry %= md

                # test
                destination = None
                if worry % m["candivby"] == 0:
                    destination = m["true_monkey"]
                else:
                    destination = m["false_monkey"]

                # throw to monkey
                monkeys[destination]["items"].append(worry)
                m["items"] = m["items"][1:]

        if k + 1 in [1, 20, 1000, 2000]:
            print("after %s rounds" % (k + 1))
            print_state(monkeys)

    insp = []
    for m in monkeys.values():
        insp.append(m["inspections"])

    print(math.prod(sorted(insp, reverse=True)[:2]))


part1()
part2()
