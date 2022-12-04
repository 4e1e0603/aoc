"""
Advent of Code 2022 Day 4
"""

data = open("aoc2204.txt").read().strip().split()

xs: list[tuple[set, set]] = []

for d in data:
    x, y = [tuple(map(int, t.split("-"))) for t in d.split(",")]
    a, b = set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))
    xs.append((a, b))

s1 = sum((a.issubset(b) or a.issuperset(b) for a, b in xs))
print(s1)

s2 = sum((bool(a.intersection(b)) for a, b in xs))
print(s2)
