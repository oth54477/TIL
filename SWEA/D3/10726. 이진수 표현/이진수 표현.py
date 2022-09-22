for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    m = format(m, 'b')
    result = 'ON'
    chk = m[-n:]
    if '0' in chk or n > len(chk):
        result = 'OFF'
    print(f'#{t} {result}')