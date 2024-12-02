import os
import itertools


def read_input():
    with open(os.path.join(os.getcwd(), "input.txt"), "r") as f:
        lines = f.readlines()
    lines = [[int(j) for j in i.strip("\n").split(" ")] for i in lines]
    return lines


def _is_safe(l):
    changes = [abs(i - j) for i, j in zip(l[:-1], l[1:])]
    in_range = [i >= 1 and i <= 3 for i in changes]
    increasing = [i < j for i, j in zip(l[:-1], l[1:])]
    decreasing = [i > j for i, j in zip(l[:-1], l[1:])]
    return all(in_range) and (all(increasing) or all(decreasing))


def _is_safe_brute(l):
    if _is_safe(l):
        return True
    else:
        subsets = itertools.combinations(l, len(l) - 1)
        for s in subsets:
            if _is_safe(s):
                return True
        return False


def part_one():
    puzzle_input = read_input()
    safe_reports = [_is_safe(i) for i in puzzle_input]
    print(f"The answer to part one is {sum(safe_reports)}")


def part_two():
    puzzle_input = read_input()
    safe_reports = [_is_safe_brute(i) for i in puzzle_input]
    print(f"The answer to part two is {sum(safe_reports)}")


if __name__ == "__main__":
    part_one()
    part_two()