T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # A사
    cost_A = P * W

    # B사
    if W <= R:
        cost_B = Q
    else:
        cost_B = Q + (S * (W - R))
    
    # 결과 출력
    if cost_A > cost_B:
        print(f'#{test_case} {cost_B}')
    else:
        print(f'#{test_case} {cost_A}')
