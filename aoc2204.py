"""
Advent of Code 2022 Day 4
"""

data = open("aoc2204.txt").read().strip().split()

xs: list[tuple[set, set]] = []

for d in data:
    t = d.split(",")
    x, y = tuple(map(int, t[0].split("-"))), tuple(map(int, t[1].split("-")))
    a, b = set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))
    if b > a:
        a, b = b, a
    xs.append((a, b))

s1 = sum((a.issuperset(b) for a, b in xs))
print(s1)

s2 = sum((bool(a.intersection(b)) for a, b in xs))
print(s2)
