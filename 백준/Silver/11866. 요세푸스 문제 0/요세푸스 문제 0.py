import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())

people = list(range(1, n + 1))
visited = [False] * n
arr = []
cnt, idx = 0, 0
while False in visited:
    while True:
        if not visited[idx]:
            cnt += 1
        if cnt == k:
            break
        idx = (idx + 1) % n
    arr.append(people[idx])
    visited[idx] = True
    cnt = 0
print('<', end='')
print(*arr, sep=', ', end='')
print('>')
