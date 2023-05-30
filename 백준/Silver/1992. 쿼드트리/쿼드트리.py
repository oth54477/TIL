import sys

input = sys.stdin.readline


def zip_img(arr, n):
    half = n // 2
    result = []
    for i in range(0, n, half):
        for j in range(0, n, half):
            temp = [arr[r][j : j + half] for r in range(i, i + half)]
            count = [0, 0]
            for line in temp:
                for x in line:
                    if x == 1:
                        count[1] += 1
                    else:
                        count[0] += 1
            if 0 not in count:
                result.append(zip_img(temp, half))
            else:
                if count[0] == 0:
                    result.append(1)
                else:
                    result.append(0)
    return tuple(result)


N = int(input().strip())

arr = [list(map(int, input().strip())) for _ in range(N)]

count = [0, 0]
for line in arr:
    for x in line:
        if x == 1:
            count[1] += 1
        else:
            count[0] += 1
if 0 not in count:
    result = zip_img(arr, N)
    print(str(result).replace(", ", ""))
else:
    if count[0] == 0:
        print(1)
    else:
        print(0)