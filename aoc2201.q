//Advent of Code 2022 Day 1

/v1
d: "1\n2\n3\n\n4\n5\n6\n\n7\n8\n9"; /sample

t:{sum each "J"$ "\n" vs/: "\n\n" vs x};

t1:{max t x};
t2:{sum 3#desc t x};

s1:t1[d];
s2:t2[d];

show s1, s2;

/v2
d:read0`:aoc2201.txt;
t:{
    n: "J"$x;       / numbers
    n
    }

show t[d];