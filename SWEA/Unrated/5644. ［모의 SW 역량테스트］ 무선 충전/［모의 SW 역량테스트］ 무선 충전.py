dxy = [(0 ,0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for t in range(1, int(input()) + 1):
    m, a = map(int, input().split())
    a_info = [0] + list(map(int, input().split()))
    b_info = [0] + list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(a)]

    a_row, a_col = 1, 1
    b_row, b_col = 10, 10
    result = 0
    for time in range(m + 1):
        a_row, a_col = a_row + dxy[a_info[time]][0], a_col + dxy[a_info[time]][1]
        b_row, b_col = b_row + dxy[b_info[time]][0], b_col + dxy[b_info[time]][1]

        a_temp, b_temp = set(), set()
        for idx, bc_info in enumerate(bc):
            if abs(a_col - bc_info[0]) + abs(a_row - bc_info[1]) <= bc_info[2]:
                a_temp.add(idx)
            if abs(b_col - bc_info[0]) + abs(b_row - bc_info[1]) <= bc_info[2]:
                b_temp.add(idx)

        if a_temp & b_temp:
            max_sum = 0
            for i in a_temp:
                for j in b_temp:
                    if i == j:
                        power = bc[i][3] // 2
                        a_power, b_power = power, power
                    else:
                        a_power, b_power = bc[i][3], bc[j][3]
                    if max_sum <= a_power + b_power:
                        max_sum = a_power + b_power
                        a = a_power
                        b = b_power
            result += a + b
        else:
            if a_temp:
                result += max(map(lambda x: bc[x][3], a_temp))
            if b_temp:
                result += max(map(lambda x: bc[x][3], b_temp))

    print(f'#{t} {result}')
