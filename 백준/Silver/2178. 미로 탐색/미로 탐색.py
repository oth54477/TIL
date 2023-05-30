import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().strip().split())

arr = [list(map(int, input().strip())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

flag = True
dq = deque([(0, 0, 1)])
visited = {(0, 0)}
while dq and flag:
    r, c, cnt = dq.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and (nr, nc) not in visited:
            if nr == N - 1 and nc == M - 1:
                flag = False
                break
            visited.add((nr, nc))
            dq.append((nr, nc, cnt + 1))
print(cnt + 1)
