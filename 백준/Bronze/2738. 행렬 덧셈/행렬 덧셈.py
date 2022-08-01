import sys

input = sys.stdin.readline
N, M = map(int, input().split())

matrix1 = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

matrix2 = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for row in range(N):
    for col in range(M):
        matrix1[row][col] += matrix2[row][col]
        print(matrix1[row][col], end=' ')
