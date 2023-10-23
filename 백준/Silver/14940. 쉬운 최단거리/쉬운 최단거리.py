import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
d = [(0,1), (0,-1), (1,0), (-1,0)]

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치를 찾기 위한 set
check_set = set()
visited = set()

# 출발 위치를 찾고, 갈 수 있는 땅 기록
for r, line in enumerate(arr):
        for c, value in enumerate(line):
            if value == 2:
                visited.add((r, c))
                dq = deque([(r, c, 1)])
                arr[r][c] = 0
            elif value == 1:
                check_set.add((r, c))

# BFS
while dq:
    r, c, cnt = dq.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and (nr, nc) not in visited:
            visited.add((nr, nc))
            arr[nr][nc] = cnt
            dq.append((nr, nc, cnt + 1))

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치
remain = check_set - visited

for r, c in remain:
     arr[r][c] = -1

for result in arr:
    print(*result)
