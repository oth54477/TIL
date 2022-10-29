from collections import deque
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def draw(row, col, i, c):
    cnt = 0
    q = deque([(row, col, cnt)])
    while q:
        row, col, cnt = q.popleft()
        map_arr[row][col].add(i)
        for dr, dc in d:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 10 and 0 <= nc < 10 and i not in map_arr[nr][nc] and cnt < c:
                q.append((nr, nc, cnt + 1))

def select(a, b):
    max_sum = 0
    for i in a:
        for j in b:
            if i == j:
                power = powers[i] // 2
                a_power, b_power = power, power
            else:
                a_power, b_power = powers[i], powers[j]
            if max_sum <= a_power + b_power:
                max_sum = a_power + b_power
                a_max_power = a_power
                b_max_power = b_power
    return a_max_power, b_max_power


dxy = [(0 ,0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for t in range(1, int(input()) + 1):
    m, a = map(int, input().split())
    map_arr = [[set() for _ in range(10)] for _ in range(10)]

    a_info = [0] + list(map(int, input().split()))
    b_info = [0] + list(map(int, input().split()))
    powers = []
    for i in range(a):
        col, row, c, p = map(int, input().split())
        powers.append(p)
        draw(row-1, col-1, i, c)

    a_row, a_col = 0, 0
    b_row, b_col = 9, 9
    a_result, b_result = 0, 0
    for time in range(m+1):
        a_row, a_col = a_row + dxy[a_info[time]][0], a_col + dxy[a_info[time]][1]
        b_row, b_col = b_row + dxy[b_info[time]][0], b_col + dxy[b_info[time]][1]

        a_now = map_arr[a_row][a_col]
        b_now = map_arr[b_row][b_col]

        if a_now & b_now:
            a_power, b_power = select(a_now, b_now)
            a_result += a_power
            b_result += b_power
        else:
            if a_now:
                a_result += max(map(lambda x: powers[x], a_now))
            if b_now:
                b_result += max(map(lambda x: powers[x], b_now))

    print(f'#{t} {a_result + b_result}')
