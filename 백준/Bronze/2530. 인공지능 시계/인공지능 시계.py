import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())
d = int(input())

total = h * 3600 + m * 60 + s + d
h, total = divmod(total, 3600)
m, s = divmod(total, 60)

if s >= 60:
    m += (s // 60)
    s %= 60

if m >= 60:
    h += (m // 60)
    m %= 60

if h >= 24:
    h %= 24

print(h, m, s)