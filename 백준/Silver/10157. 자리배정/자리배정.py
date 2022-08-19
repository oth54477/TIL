# BOJ_10157. 자리배정

c, r = map(int, input().split())
k = int(input())
if c * r < k:
    print(0)
else:
    hall = [[0] * c for _ in range(r)]
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    number = 1
    nr, nc = r - 1, 0
    dr = 0
    while number < k + 1:
        if 0 <= nr < r and 0 <= nc < c and not hall[nr][nc]:
            hall[nr][nc] = number
            number += 1
            row, col = nr, nc
        else:
            dr += 1
        dr %= 4
        nr, nc = row + d[dr][0], col + d[dr][1]

    print(col + 1, r - row)
