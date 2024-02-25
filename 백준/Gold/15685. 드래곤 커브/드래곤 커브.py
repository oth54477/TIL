import sys

input = sys.stdin.readline

N = int(input().strip())

board = [[0] * 101 for _ in range(101)]

# 오, 위, 왼, 아래
D = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for _ in range(N):
    x, y, d, g = map(int, input().strip().split())

    board[y][x] = 1

    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)-1, -1, -1):
            temp.append((move[i]+1) % 4)
        move.extend(temp)

    for i in move:
        dy, dx = D[i]
        ny, nx = y + dy, x + dx
        board[ny][nx] = 1
        x, y = nx, ny

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
            answer += 1

print(answer)