import sys

input = sys.stdin.readline

a, b = map(int, input().split())

measure, multiple = 0, 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        measure = max(measure, i)

for j in range(max(a, b), a * b + 1):
    if j % a == 0 and j % b == 0:
        multiple = j
        break
print(measure)
print(multiple)
