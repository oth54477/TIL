import sys

input = sys.stdin.readline

a1, b1, c1, a2, b2, c2 = map(int, input().strip().split())

y = (c1 * a2 - c2 * a1) // (b1 * a2 - b2 * a1)
x = (c1 * b2 - c2 * b1) // (a1 * b2 - a2 * b1)
print(x, y)