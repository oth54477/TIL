import sys
from collections import deque

input = sys.stdin.readline

def bfs(r, c, cnt):
    global tr, tc, i
    visited = set()
    dq = deque([(r, c, cnt)])
    visited.add((r,c))
    while dq:
        r, c , cnt = dq.popleft()
        if tr == r and tc == c:
            return cnt
        if tr == r:
            if tc < c:
                d = [2, 3]
            else:
                d = [1, 4]
        elif tc == c:
            if tr < r:
                d = [1, 2]
            else:
                d = [3, 4]
        elif tr < r and tc > c:
            d = [1, 2, 4]
        elif tr < r and tc < c:
            d = [2, 1, 3]
        elif tr > r and tc < c:
            d = [3, 2, 4]
        else:
            d = [4, 1, 3]
        for dn in d:
            for dr, dc in d_dict[dn]:
                nr, nc = r + dr, c + dc
                if nr == tr and nc == tc:
                    return cnt + 1
                if 0 <= nr < i and 0 <= nc < i and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dq.append((nr, nc, cnt + 1))




d_dict = {1: [(-2, 1), (-1, 2)], 2: [(-1, -2), (-2, -1)], 3: [(1, -2), (2, -1)], 4: [(2, 1) , (1, 2)]}
tc = int(input().strip())
result = []
for _ in range(tc):
    i = int(input().strip())
    r,c = map(int,input().strip().split())
    tr,tc = map(int,input().strip().split())
    result.append(bfs(r, c, 0))
print(*result, sep='\n')