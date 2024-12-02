import os
from collections import Counter


def read_input():
    with open(os.path.join(os.getcwd(), "input.txt"), "r") as f:
        lines = f.readlines()
    splits = [i.strip("\n").split("   ") for i in lines]
    left, right = [int(i[0]) for i in splits], [int(i[1]) for i in splits]
    return left, right
    

def part_1():
    left, right = read_input()
    left, right = sorted(left), sorted(right)
    distances = [abs(i - j) for i, j in zip(left, right)]
    print(f"The answer to part one is {sum(distances)}")


def part_2():
    left, right = read_input()
    right_counts = Counter(right)
    score = 0
    for i in left:
        lookup = right_counts.get(i)
        if lookup is not None:
            score += i * lookup
    print(f"The answer to part two is {score}")


if __name__ == "__main__":
    part_1()
    part_2()