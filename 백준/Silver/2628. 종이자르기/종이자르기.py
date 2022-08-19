c, r = map(int, input().split())

n = int(input())

row_arr = [i for i in range(r)]
col_arr = [i for i in range(c)]
# rows, cols, r_cnt, c_cnt = [], [], 0, 0
rows, cols, r_cnt, c_cnt = [0], [0], 0, 0
for _ in range(n):
    cut, idx = map(int, input().split())
    if cut == 0:
        rows.append(idx)
    else:
        cols.append(idx)

rows.sort()
cols.sort()

rows.append(r)
cols.append(c)
max_r, max_c = 0, 0
for rr in range(1, len(rows)):
    rrr = rows[rr] - rows[rr - 1]
    if max_r < rrr:
        max_r = rrr
for cc in range(1, len(cols)):
    ccc = cols[cc] - cols[cc - 1]
    if max_c < ccc:
        max_c = ccc
print(max_c * max_r)