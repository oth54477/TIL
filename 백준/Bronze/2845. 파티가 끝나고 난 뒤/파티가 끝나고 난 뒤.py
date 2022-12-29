import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n = a * b
arr = list(map(int , input().split()))
result = []

for i in arr:
    result.append(i - n)
print(*result)


