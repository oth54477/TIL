import sys

input = sys.stdin.readline

R, C = map(int, (input().strip().split()))

arr = [list(map(str, input().strip())) for _ in range(R)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

land_to_sea = []
land_r = set()
land_c = set()
for r, line in enumerate(arr):
    for c, point in enumerate(line):
        if point == "X":
            sea_cnt = 0
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C and arr[nr][nc] == "X"):
                    sea_cnt += 1
            if sea_cnt >= 3:
                land_to_sea.append((r, c))
            else:
                land_r.add(r)
                land_c.add(c)
max_r, min_r = max(land_r), min(land_r)
max_c, min_c = max(land_c), min(land_c)

for r, c in land_to_sea:
    arr[r][c] = "."

result = list(map(lambda line: line[min_c:max_c+1], arr[min_r:max_r+1]))

for line in result:
    print(*line, sep="")
