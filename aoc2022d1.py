"""
Advent of Code 2022 Day 1
"""

xs = (x.split("\n") for x in open("./aoc2022d1.txt").read().split("\n\n"))

ys = [sum(int(n) for n in x) for x in xs]

t1 = max(ys)
t2 = sum(sorted(ys, reverse=True)[:3])

print(t1, t2)
