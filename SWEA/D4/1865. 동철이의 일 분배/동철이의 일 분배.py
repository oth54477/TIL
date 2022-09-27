def success_rate(person, rate, visit):
    global result
    if person == n:
        result = max(result, rate)
        return
    if rate <= result:
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            success_rate(person + 1, rate * rate_arr[person][i], visit)
            visit[i] = False

for t in range(1, int(input()) + 1):
    n = int(input())
    rate_arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [False] * n
    result = 0
    success_rate(0, 1, visited)
    print(f'#{t} {round(result * 100, 6)  :.6f}')