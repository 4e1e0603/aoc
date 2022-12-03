"""
Advent of Code 2022 Day 3
"""

import string

# v1
xs = [(x[:len(x) // 2], x[len(x) // 2:])  for x in open("./aoc2203.txt").read().split()]

t = { k:v for k,v in (zip(string.ascii_letters, range(1, 53)))}

s1 = sum(t[list(set(x[0]) & set(x[1]))[0]] for x in xs)
print(s1)

ys = [xs[i:i + 3] for i in range(0, len(xs),  3)] # Split to groups by three bags.

s2 = sum( (t[ list( set(y[0][0] + y[0][1]) & set(y[1][0] + y[1][1]) & set(y[2][0] + y[2][1]) )[0] ] for y in ys) )
print(s2)