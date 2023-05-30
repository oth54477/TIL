import sys

input = sys.stdin.readline


def zip_img(arr, n):
    point = n // 3

    for i in range(0, n, point):
        for j in range(0, n, point):
            temp = [arr[r][j : j + point] for r in range(i, i + point)]
            count = [0, 0, 0]
            for line in temp:
                for x in line:
                    if x == 1:
                        count[2] += 1
                    elif x == 0:
                        count[1] += 1
                    else:
                        count[0] += 1
            if point**2 in count:
                result[count.index(point**2)] += 1
            else:
                zip_img(temp, point)


N = int(input().strip())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

result = [0, 0, 0]

count = [0, 0, 0]
for line in arr:
    for x in line:
        if x == 1:
            count[2] += 1
        elif x == 0:
            count[1] += 1
        else:
            count[0] += 1
if N**2 in count:
    result[count.index(N**2)] += 1
else:
    zip_img(arr, N)
print(*result, sep="\n")