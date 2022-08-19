w, h = map(int, input().split())
n = int(input())
arr = []
map_arr = [[False] * (w + 1) for _ in range(h + 1)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n + 1):
    d, l = map(int, input().split())

    if d == 1:
        row, col = 0, l
    elif d == 2:
        row, col = h, l
    elif d == 3:
        row, col = l, 0
    elif d == 4:
        row, col = l, w
    if i != n:
        map_arr[row][col] = 2
    else:
        map_arr[row][col] = True
check_arr = []
cnt = 0
d_idx = 0
while len(check_arr) < n:
    nr, nc = row + dr[d_idx][0], col + dr[d_idx][1]
    if (
        0 <= nr < h + 1
        and 0 <= nc < w + 1
        and (nr == 0 or nr == h or nc == 0 or nc == w)
        and (map_arr[nr][nc] != True)
    ):
        row, col = nr, nc
        cnt += 1
        if map_arr[row][col] == 2:
            check_arr.append(cnt)
        map_arr[nr][nc] = True
    d_idx += 1
    d_idx %= 4

sum_cnt = 0
for num in check_arr:
    if num > (w + h):
        num = 2 * (w + h) - num
    sum_cnt += num

print(sum_cnt)