for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    m = format(m, 'b')
    result = 'ON'
    if n > len(m):
        result = 'OFF'
    else:
        if '0' in m[-n:]:
            result = 'OFF'
    print(f'#{t} {result}')