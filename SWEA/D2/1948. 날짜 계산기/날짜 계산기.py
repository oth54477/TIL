for t in range(1, int(input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())

    table = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    result = 0

    if m1 == m2:
        result = d2 - d1 + 1
    else:
        for i in range(m1 + 1, m2):
            result += table[i]
        result += table[m1] - d1 + 1 + d2
    print(f'#{t} {result}')
