def dfs(row, col, eat, d):
    global max_eat
    if d == 3 and row == i and col == j:
        max_eat = max(max_eat, len(eat))
        return

    if 0 <= row < n and 0 <= col < n and arr[row][col] not in eat:
        new_eat = eat + [arr[row][col]]
        nr, nc = row + dxy[d][0], col + dxy[d][1]
        dfs(nr, nc, new_eat, d)
        if d < 3:
            nr, nc = row + dxy[d+1][0], col + dxy[d+1][1]
            dfs(nr, nc, new_eat, d+1)



dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_eat = -1
    for i in range(n):
        for j in range(1,n-1):
            dfs(i, j, [], 0)
    print(f'#{tc} {max_eat}')