for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = 0
    arr = [[] for _ in range(n)]

    while cnt < n:
        for i in range(cnt + 1):
            if i - 1 < 0 or i + 1 > cnt:
                arr[cnt].append(1)
            else:
                arr[cnt].append(arr[cnt - 1][i] + arr[cnt - 1][i - 1])
        cnt += 1

    print(f'#{t}')
    for idx in range(n):
        print(*arr[idx])
