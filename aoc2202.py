"""
Advent of Code 2022 Day 2
"""

# v1
xs = open("./aoc2202.txt").read().split("\n")
R, P, S, L, D, W = 1, 2, 3, 0, 3, 6

G1 = {"A X": R + D, "A Y": P + W, "A Z": S + L,
      "B X": R + L, "B Y": P + D, "B Z": S + W,
      "C X": R + W, "C Y": P + L, "C Z": S + D, }
s1 = sum((G1[x] for x in xs))
print(s1)

G2 = {"A X": S + L, "A Y": R + D, "A Z": P + W,
      "B X": R + L, "B Y": P + D, "B Z": S + W,
      "C X": P + L, "C Y": S + D, "C Z": R + W, }

s2 = sum((G2[x] for x in xs))
print(s2)
