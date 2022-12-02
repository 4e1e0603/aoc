"""
Advent of Code 2022 Day 1
"""

# v1
xs = (x.split("\n") for x in open("./aoc2022d1.txt").read().split("\n\n"))

ys = [sum(int(n) for n in x) for x in xs]

s1 = max(ys)
print(s1)

s2 = sum(sorted(ys, reverse=True)[:3])
print(s2)
