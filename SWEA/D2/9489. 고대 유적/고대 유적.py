for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    r_max_count = 0
    r_count = 0
    l_max_count = 0
    l_count = 0
    for row in range(n):
        for col in range(m):
            # 가로 탐색
            if arr[row][col] == 1:
                r_count += 1
            else:
                if r_max_count < r_count:
                    r_max_count = r_count
                r_count = 0
        if r_max_count < r_count:
            r_max_count = r_count
        r_count = 0

    for col in range(m):
        for row in range(n):
            # 세로 탐색
            if arr[row][col] == 1:
                l_count += 1
            else:
                if l_max_count < l_count:
                    l_max_count = l_count
                l_count = 0

        if r_max_count < r_count:
            r_max_count = r_count
        if l_max_count < l_count:
            l_max_count = l_count
        l_count = 0

    if r_max_count < l_max_count:
        r_max_count = l_max_count

    print(f'#{t} {r_max_count}')
