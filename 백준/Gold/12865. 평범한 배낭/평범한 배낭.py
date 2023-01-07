n, k = map(int, input().split())
knapsack = [[0] * (k + 1) for _ in range(n + 1)]
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            # weight보다 작으면 위의 값을 그대로 가져온다
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(
                value + knapsack[i - 1][j - weight], knapsack[i - 1][j]
            )

print(knapsack[n][k])