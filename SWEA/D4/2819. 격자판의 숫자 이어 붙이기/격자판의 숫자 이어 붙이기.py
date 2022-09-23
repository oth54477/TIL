def dfs(row, col, s):
    if len(s) == 7:
        nums_set.add(s)
        return
        
    for d in range(4):
        nr, nc = row + dx[d], col + dy[d]
        if 0<= nr < 4 and 0<= nc < 4:
            dfs(nr,nc,s+str(arr[nr][nc]))
            

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # visited = [[False] * n for _ in range(n)]
    nums_set = set()
    for row in range(4):
        for col in range(4):
            dfs(row, col,'')
    
    print(f'#{t} {len(nums_set)}')
