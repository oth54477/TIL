def othello(row, col, dol):
    for d in range(8):
        nr, nc = row + dx[d], col + dy[d]
        if 0 <= nr < n and 0 <= nc < n and field[nr][nc] == dols[dol]:
            find_dol(nr, nc, dol, d)


def find_dol(row, col, dol, d):
    global find_status
    find_status = False
    if 0 <= row < n and 0 <= col < n and field[row][col]:
        if field[row][col] == dol:
            find_status = True
            return
        elif field[row][col] == dols[dol]:
            find_dol(row + dx[d], col + dy[d], dol, d)
        if find_status:
            field[row][col] = dols[field[row][col]]
    else:
        return
    
dols = {1:2, 2:1}
table = {4:[(1,1),(1,2),(2,2),(2,1)], 6:[(2,2),(2,3),(3,3),(3,2)], 8:[(3,3),(3,4),(4,4),(4,3)]}
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    field = [[0] * n for _ in range(n)]
    cnt = 0
    find_status = False
    for r, c in table[n]:
        if cnt % 2 == 0:
            field[r][c] = 2
        else:
            field[r][c] = 1
        cnt += 1
    for _ in range(m):
        row, col, dol = map(int, input().split())
        row -= 1
        col -= 1
        field[row][col] = dol
        othello(row,col,dol)
    white, black = 0,0
    for line in field:
        black += line.count(1)
        white += line.count(2)
    print(f'#{t} {black} {white}')