def day_or_month(month_idx):
    day_cost = plan[month_idx] * prices[0]
    month_cost = prices[1]
    return min(day_cost, month_cost)


for t in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    total_cost = [0] * 13
    for i in range(1, 13):
        total_cost[i] = total_cost[i - 1] + day_or_month(i - 1)
        if i >= 3:
            month_3 = total_cost[i - 3] + prices[2]
            total_cost[i] = min(total_cost[i], month_3)
    year_or_total = min(prices[3], total_cost[12])
    print(f'#{t} {year_or_total}')
