from collections import deque

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(maps):
    global row_len, col_len
    result = -1
    maps = make_array(maps)

    row_len = len(maps)
    col_len = len(maps[0])
    
    start, lever, end = find_idx(maps)

    lever_count = count_time(start, lever, maps)
    if lever_count:
        end_count = count_time(lever, end, maps)
        if end_count: 
            return lever_count + end_count
    return -1




def make_array(arrs):
    return [list(map(str, arr)) for arr in arrs]


def find_idx(maps):
    start, lever, end = None, None, None
    for row_idx, map in enumerate(maps):
        for col_idx, value  in enumerate(map):
            if value == 'O' or value == 'X':
                continue
            elif value == 'S':
                start = (row_idx, col_idx)
            elif value == 'L':
                lever = (row_idx, col_idx)
            else:
                end = (row_idx, col_idx)
            if end and lever and start:
                return start, lever, end


def count_time(start_point, find_point, maps):
    dq = deque([(*start_point, 0)])
    visited = set()
    while dq:
        r, c, cnt = dq.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0<= nr < row_len and 0 <= nc < col_len and (nr, nc) not in visited and maps[nr][nc] != 'X':
                if (nr ,nc) == find_point:
                    return cnt + 1
                dq.append((nr, nc, cnt + 1))
                visited.add((nr, nc))

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))