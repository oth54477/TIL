import sys

input = sys.stdin.readline

a, b = map(int, input().split())

q = list(range(a, (a - b), -1))
w = list(range(1, b + 1))
result = 1
for i in q:
    result *= i
for j in w:
    result /= j
print(int(result))
