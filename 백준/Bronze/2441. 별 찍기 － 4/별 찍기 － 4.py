n = int(input())

ptn, space = '*', ' '
for m in range(n, 0, -1):
    line = space * (n - m) + ptn * m
    print(line)
