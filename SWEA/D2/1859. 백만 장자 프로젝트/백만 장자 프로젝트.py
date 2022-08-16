for t in range(1, int(input()) + 1):
    n = int(input())
    costs = list(map(int, input().split()))

    start_idx, revenue = 0, 0
    while True:
        max_cost = max(costs)
        max_idx = costs.index(max_cost)

        revenue += (max_idx) * max_cost - sum(costs[:max_idx])
        del costs[: max_idx + 1]
        if not costs:
            break

    print(f'#{t} {revenue}')
