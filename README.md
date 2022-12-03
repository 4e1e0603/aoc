# Advent of Code

- https://adventofcode.com/
- https://en.wikipedia.org/wiki/Advent_of_Code

- [2022](https://adventofcode.com/2022)
  - [D 01/25: Calorie Counting](https://adventofcode.com/2022/day/1), code: [py](./aoc2201.py); [data](./aoc2201.txt),
  - [D 02/25: Rock Paper Scissors](https://adventofcode.com/2022/day/2), code: [py](./aoc2202.py); [data](./aoc2202.txt)
  - [D 03/25: Rucksack Reorganization](https://adventofcode.com/2022/day/3), code: [py](./aoc2203.py); [data](./aoc2203.txt)
  - Other people solutions (Watch after you finish your solution!):
    - Day 1: [Jonathan Paulson (py)](https://youtu.be/XpkFsqqYi6A)
    - Day 2: [Jonathan Paulson (py)](https://youtu.be/X1XH774hId0)
    - Day 3: [Jonathan Paulson (py)](https://youtu.be/nMJUzjr5tQY)

Comment on my solutions later!

The code is quite dense. I usually end up with a solution without explicit loops, I use
comprehension where possible without intermediate variables. This is hard to debug, so
I usually start with some loop and then refactor it on the way. The variable names are usually abbreviated
as follows: `t`: table, `s`: solution (sometimes intermediate), `s1`, `s2`: solutions (parts 1 and 2), `xs`, `ys`: input data.

### Python

    py aoc{yy}{dd}.py

e.g.

    py aoc2201.py

### kdb+/q

    C:\q\w64\q.exe
    q)system "cd C:/path/to/advent-of-code"

    q)\l aoc{yy}{dd}.q

e.g.

    q)\l aoc2201.q

## Template

Use PowerShell?
- download data from `https://adventofcode.com/{yyyy}/day/{d}/input`
- create a file with proper name, defaults, and comment `aoc{yy}{dd}.{ex}`