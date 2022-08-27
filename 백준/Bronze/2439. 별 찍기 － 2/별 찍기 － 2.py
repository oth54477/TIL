n = int(input())

ptn, space = '*', ' '
for m in range(1, n + 1):
    line = space * (n - m) + ptn * m
    print(line)
