import os
import re


MUL_PATTERN = re.compile(r"(mul)\(([0-9]*,[0-9]*)\)")
DO_PATTERN = re.compile(r"(mul)\(([0-9]*,[0-9]*)\)|don't\(\)|do\(\)")


def read_input():
    with open(os.path.join(os.getcwd(), "input.txt"), "r") as f:
        s = f.read()
    return s


def part_one():
    s = read_input()
    matches = re.findall(MUL_PATTERN, s)
    res = 0
    for _, nums in matches:
        x, y = nums.split(",")
        res += (int(x) * int(y))
    print(f"The answer to part one is {res}")


def part_two():
    s = read_input()
    matches = re.finditer(DO_PATTERN, s)
    res, turned_on = 0, True
    for m in matches:
        match m.group(0):
            case 'do()': 
                turned_on = True
            case "don't()": 
                turned_on = False
            case _:
                if turned_on:
                    x, y = m.group(0)[4:-1].split(",")
                    res += int(x) * int(y)
    print(f"The answer to part two is {res}")


if __name__ == "__main__":
    part_one()
    part_two()