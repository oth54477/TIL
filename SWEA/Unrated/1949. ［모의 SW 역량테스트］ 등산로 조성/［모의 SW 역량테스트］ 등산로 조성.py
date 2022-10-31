def dfs(row, col, cnt, drill, now_h):
    global max_cnt
    visited[row][col] = True
    for dr, dc in d:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            next_h = map_arr[nr][nc]
            if now_h > next_h:
                dfs(nr, nc, cnt + 1, drill, next_h)
                visited[nr][nc] = False
            elif drill and next_h - now_h < k:
                dfs(nr, nc, cnt + 1, 0, now_h-1)
                visited[nr][nc] = False

    max_cnt = max(max_cnt, cnt)




d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for t in range(1, int(input())+ 1):
    n, k = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(n)]
    max_h = max(list(map(max, map_arr)))
    visited = [[False] * n for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            if map_arr[i][j] == max_h:
                dfs(i, j, 1, 1, max_h)
                visited[i][j] = False
    print(f'#{t} {max_cnt}')
