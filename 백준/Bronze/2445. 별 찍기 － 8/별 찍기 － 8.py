n = int(input())

ptn, space = '*', ' '
for m in range(1, n + 1):
    line = ptn * m + space * (n - m) * 2 + ptn * m
    print(line)
for m in range(n - 1, 0, -1):
    line = ptn * m + space * (n - m) * 2 + ptn * m
    print(line)
