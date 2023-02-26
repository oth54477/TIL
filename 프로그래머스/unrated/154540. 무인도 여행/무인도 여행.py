import sys
sys.setrecursionlimit(10000)

def solution(maps):
    global result, visited, len_row, len_col

    maps = make_array(maps)
    len_row = len(maps)
    len_col = len(maps[0])

    visited = set()
    result = []

    for r in range(len_row):
        for c in range(len_col):
            if maps[r][c] and (r, c) not in visited:
                result.append(maps[r][c])
                visited.add((r, c))
                dfs(maps, r, c)

    return sorted(result) if result else [-1]

def make_array(arrs):
    return [list(map(lambda x: 0 if x == 'X' else int(x), arr)) for arr in arrs]

def dfs(maps, r, c):
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len_row and 0 <= nc < len_col and (nr, nc) not in visited:
            next_food = maps[nr][nc]
            visited.add((nr, nc))
            if next_food:
                result[-1] += next_food
                dfs(maps, nr, nc)



d = [(-1, 0), (1, 0), (0, -1), (0, 1)]