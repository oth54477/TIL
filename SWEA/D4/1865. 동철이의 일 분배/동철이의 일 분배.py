def success_rate(person, r, visit):
    global result
    if person == n:
        result = max(result, r)
        return
    if r <= result:
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            success_rate(person + 1, r * rate[person][i], visit)
            visit[i] = False



for t in range(1, int(input()) + 1):
    n = int(input())
    rate = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [False] * n
    result = 0
    success_rate(0, 1, visited)
    max_rate = round(result * 100, 6)  
    print(f'#{t} {max_rate:.6f}')