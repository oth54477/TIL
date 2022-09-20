for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    m = format(m, 'b')
    cnt, result = 0, 'OFF'
    if n <= len(m):
        for i in m[::-1]:
            if cnt == n:
                break
            if i == '0':
                result = 'OFF'
                break
            else:
                result = 'ON'
            cnt += 1

    print(f'#{t} {result}')