T = int(input())
for t in range(1, T + 1):

    # 다음에 입력할 곳의 값이 0이면 계속 0 이 아니면 스탑
    N = int(input())
    snail = [[0 for j in range(N)] for i in range(N)]  # 0으로 채워져 있는 2차원 배열 선언
    snail[0][0] = 1  # 0,0에 1 할당
    number = 1  # 할당해줄 숫자
    row = 0
    col = 0
    cnt = 0
    while number != N**2:  # number가 N의 제곱이 될 때까지 반복
        while True and cnt < N - 1:  # 오른쪽으로 이동
            if snail[row][col + 1] != 0:  # 다음칸(오른쪽)의 값이 0이 아니면  정지
                break
            else:
                number += 1
                col += 1
                snail[row][col] = number
                end_condition = 0
                cnt += 1
        cnt = 0
        while True and cnt < N - 1:  # 아래쪽으로 이동
            if snail[row + 1][col] != 0:  # 다음칸(아래쪽)의 값이 0이 아니면  정지
                break
            else:
                number += 1
                row += 1
                snail[row][col] = number
                end_condition = 0
                cnt += 1
        cnt = 0
        while True and cnt <= N - 1:  # 왼쪽
            if snail[row][col - 1] != 0:  # 다음칸(왼쪽)의 값이 0이 아니면  정지
                break
            else:
                number += 1
                col -= 1
                snail[row][col] = number
                end_condition = 0
                cnt += 1
        cnt = 0
        while True and cnt <= N - 1:  # 위쪽
            if snail[row - 1][col] != 0:  # 다음칸(위쪽)의 값이 0이 아니면  정지
                break
            else:
                number += 1
                row -= 1
                snail[row][col] = number
                end_condition = 0
                cnt += 1

    print(f'#{t}')
    for rows in snail:
        for cols in rows:
            print(cols, end=' ')
        print()