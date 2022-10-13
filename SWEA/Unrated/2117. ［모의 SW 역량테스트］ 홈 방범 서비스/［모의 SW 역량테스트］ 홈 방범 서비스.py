from collections import deque

def bfs(row, col):
    global max_home
    home, cnt = 0, 1
    visited = [[False] * n for _ in range(n)]
    visited[row][col] = True
    if field[row][col] == 1:
        home += 1
    q = deque([(row, col)])

    while q:
        if home * m >= (cnt * cnt + (cnt-1) * (cnt-1)):
            max_home = max(max_home, home)
        for _ in range(len(q)):
            row, col = q.popleft()
            for dr, dc in drc:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if field[nr][nc] == 1:
                        home += 1
                    q.append((nr, nc))
        cnt += 1

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    max_home = 0

    for i in range(n):
        for j in range(n):
            bfs(i, j)
    print(f'#{t} {max_home}')