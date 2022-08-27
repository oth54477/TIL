n = int(input())

ptn, space = '*', ' '
for m in range(n, 0, -1):
    line = space * (n - m) + ptn * (2 * m - 1)
    print(line)
