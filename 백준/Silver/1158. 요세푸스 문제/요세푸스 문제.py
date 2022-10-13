import sys

input = sys.stdin.readline


n, k = map(int, input().split())

people = list(range(1, n + 1))
visited = [False] * n
arr = []
idx = 0

for t in range(n):
    idx += k - 1
    if idx >= len(people):
        idx = idx % len(people)
    arr.append(people.pop(idx))

print('<', end='')
print(*arr, sep=', ', end='')
print('>')
