import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

check_set = set()
for r, line in enumerate(arr):
        for c, value in enumerate(line):
            if value == 2:
                start = (r, c)
            elif value == 1:
                 check_set.add((r, c))

visited = set()
d = [(0,1), (0,-1), (1,0), (-1,0)]
visited.add((start[0], start[1]))
dq = deque([(start[0], start[1], 1)])
arr[start[0]][start[1]] = 0

while dq:
    r, c, cnt = dq.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and (nr, nc) not in visited:
            visited.add((nr, nc))
            arr[nr][nc] = cnt
            dq.append((nr, nc, cnt + 1))

remain = check_set - visited

for r, c in remain:
     arr[r][c] = -1

for result in arr:
    print(*result)
