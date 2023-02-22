import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    global get_sword, use_sword
    visited = set()
    dq = deque([(*start, 0)])
    while dq:
        r, c, cnt = dq.popleft()
        if cnt > T:
            return 'Fail'
        if get_sword:
            if cnt > use_sword:
                return use_sword
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0 <= nc < M and (nr, nc) not in visited:

                now_position = castle[nr][nc]
                if now_position == 0:
                    if nr == N - 1 and nc == M - 1:
                        return cnt + 1
                    dq.append((nr, nc, cnt + 1))
                    visited.add((nr, nc))
                elif now_position == 2:
                    get_time = cnt + 1
                    use_sword = ((N-1) - nr) + ((M-1) - nc) + get_time
                    if use_sword <= T:
                        get_sword = True
                    visited.add((nr, nc))
    else:
        if get_sword:
            return use_sword
        else:
            return 'Fail'

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, T = map(int, input().strip().split())

castle = [list(map(int, input().strip().split())) for _ in range(N)]

warrior = (0, 0)
Princess = (N, M)

get_sword = False
use_sword = 0
result = bfs(warrior)

print(result)