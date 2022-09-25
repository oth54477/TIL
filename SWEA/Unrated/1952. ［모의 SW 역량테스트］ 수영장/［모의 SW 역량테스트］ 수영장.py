for t in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    total_cost = [0] * 13
    for i in range(1, 13):
        day_cost = plan[i - 1] * prices[0]
        month_cost = prices[1]
        total_cost[i] = total_cost[i - 1] + min(day_cost, month_cost)
        if i >= 3:
            month_3 = (
                total_cost[i - 3] + prices[2]
            )  # 1일권 / 1달권 비교한 누적값 , 3개월전 누적값  + 3개월권
            total_cost[i] = min(total_cost[i], month_3)
    year_or_total = min(prices[3], total_cost[12])
    print(f'#{t} {year_or_total}')