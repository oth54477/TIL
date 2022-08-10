n = int(input())

arr = [[0] * 100 for _ in range(100)]
count = 0
for _ in range(n):
    col, row = map(int, input().split())
    for i in range(row - 10, row):
        for j in range(col, col + 10):
            if arr[i][j] != 1:
                arr[i][j] = 1
                count += 1
print(count)
