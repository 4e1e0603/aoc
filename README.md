# Advent of Code

*Advent of Code is an annual set of Christmas-themed computer programming challenges that follow an Advent calendar. It has been running since 2015.*

[Website](https://adventofcode.com/), [Wikipedia](https://en.wikipedia.org/wiki/Advent_of_Code)

## Solutions

<details>

<summary>2022</summary>

- See <https://adventofcode.com/2022>
- [01/25: Calorie Counting](https://adventofcode.com/2022/day/1), code: [py](./aoc2201.py); [data](./aoc2201.txt)
- [02/25: Rock Paper Scissors](https://adventofcode.com/2022/day/2), code: [py](./aoc2202.py); [data](./aoc2202.txt)
- [03/25: Rucksack Reorganization](https://adventofcode.com/2022/day/3), code: [py](./aoc2203.py); [data](./aoc2203.txt)
- [04/25: Camp Cleanup](https://adventofcode.com/2022/day/4), code: [py](./aoc2204.py); [data](./aoc2204.txt)
- Other people solutions (Watch after you finish your solution!):
- 01/25: [Jonathan Paulson (py)](https://youtu.be/XpkFsqqYi6A)
- 02/25: [Jonathan Paulson (py)](https://youtu.be/X1XH774hId0)
- 03/25: [Jonathan Paulson (py)](https://youtu.be/nMJUzjr5tQY)
- 04/25: [Jonathan Paulson (py)](https://youtu.be/15qPSEFoR0U)

</details>

<details>

<summary>2023</summary>

- See <https://adventofcode.com/2023>

</details>

---

My code is quite dense. I usually end up with a solution without explicit loops, I use
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
