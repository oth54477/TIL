import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(row, col):
    global m, n
    visited[row][col] = True

    for dr in d:
        nr, nc = row + dr[0], col + dr[1]
        if (
            (0 <= nr < m)
            and (0 <= nc < n)
            and (not visited[nr][nc])
            and (field[nr][nc] == 1)
        ):
            dfs(nr, nc)


for t in range(int(input())):
    m, n, k = map(int, input().split())

    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    for row in range(m):
        for col in range(n):
            if field[row][col] == 1 and (not visited[row][col]):
                cnt += 1
                dfs(row, col)
    print(cnt)
