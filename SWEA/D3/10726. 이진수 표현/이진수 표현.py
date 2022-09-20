for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    m = format(m, 'b')
    result = 'ON'
    chk = m[-n:]
    if n > len(chk):
        result = 'OFF'
    elif '0' in chk:
        result = 'OFF'
    print(f'#{t} {result}')