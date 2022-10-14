def dfs(arr, now):
    global min_space
    if now >= len_cctv:
        space = sum(list(map(lambda x : x.count(0), arr)))
        min_space = min(min_space, space)
        return
    row, col, cctv_type = cctvs[now]
    for d in cctv_dict[cctv_type]:
        copy_room = [a[:] for a in arr]
        for dr, dc in d:
            nr, nc = row + dr, col + dc
            while 0 <= nr < n and 0 <= nc < m:
                if copy_room[nr][nc] != 6:
                    if not copy_room[nr][nc]:
                        copy_room[nr][nc] = -1
                else:
                    break
                nr, nc = nr + dr, nc + dc
        dfs(copy_room, now + 1)
                
                
                
            


cctv_dict = {1:[[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]], 2:[[(-1, 0), (1, 0)], [(0, -1), (0, 1)]], 3:[[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]], 4:[[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]], 5:[[(-1, 0), (1, 0), (0, -1), (0, 1)]]} 

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cctvs =  []
min_space = n * m
for i in range(n):
    for j in range(m):
        value = room[i][j]
        if 0 < value < 6:
           cctvs.append((i, j, value))
len_cctv = len(cctvs)
dfs(room, 0)
print(min_space)



