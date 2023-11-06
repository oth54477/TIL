import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int , input().strip().split())
lab = [list(map(int, input().strip().split())) for _ in range(N)]

table = [(-1, 0), (1, 0), (0, -1), (0, 1)]

virus = []
safe_list = []
safe_count = 0
max_safe = 0
min_virus = 999999999
flag = False

# 바이러스 찾기
for r in range(N):
    for c in range(M):
        point = lab[r][c]
        if point == 2:
            virus.append((r, c))
        elif point == 0:
            safe_count += 1
            safe_list.append((r, c))

# 가능한 경우의 수 찾기
for case in combinations(safe_list, 3):
    temp_lab = deepcopy(lab)
    virus_count = 0
    flag = True
    # 벽 세우기
    for r, c in case:
        temp_lab[r][c] = 1
    dq = deque(virus)
    while dq and flag:
        r, c = dq.popleft()
        for dr, dc in table:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and temp_lab[nr][nc] == 0:
                temp_lab[nr][nc] = 2
                virus_count += 1
                if virus_count > min_virus:
                    flag = False
                    break
                dq.append((nr, nc))

    safe_area = safe_count - virus_count - 3
    min_virus = min(min_virus, virus_count)
    max_safe = max(max_safe, safe_area)

print(max_safe)
