dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [0] * (n**2 + 1)

    for row in range(n):
        for col in range(n):
            room = arr[row][col]
            cnt = 1
            while True:
                for i in range(4):
                    nr, nc = row + dr[i], col + dc[i]
                    if 0 <= nr < n and 0 <= nc < n and arr[row][col] + 1 == arr[nr][nc]:
                        row, col = nr, nc
                        cnt += 1
                        break
                else:
                    result[room] = cnt
                    break

    max_room = max(result)
    print(f'#{t} {result.index(max_room)} {max_room}')