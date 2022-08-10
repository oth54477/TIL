for tc in range(1, 11):
    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    diagonal_1 = 0
    diagonal_2 = 0
    result_arr = []
    for i in range(100):
        cols_sum = 0
        result_arr.append(sum(arr[i]))
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][99 - i]
        for j in range(100):
            cols_sum += arr[j][i]
        result_arr.append(cols_sum)
    result_arr.append(diagonal_1)
    result_arr.append(diagonal_2)

    print(f'#{t} {max(result_arr)}')
