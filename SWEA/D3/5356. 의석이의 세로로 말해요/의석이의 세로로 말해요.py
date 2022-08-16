for t in range(1, int(input()) + 1):
    n = 5
    breaker = False
    arr = [input() for _ in range(n)]
    arr_col = [''] * 15
    for row in range(15):
        for col in range(5):
            if len(arr[col]) <= row:
                continue
            arr_col[row] += arr[col][row]

    result = ''.join(arr_col)
    print(f'#{t} {result}')
