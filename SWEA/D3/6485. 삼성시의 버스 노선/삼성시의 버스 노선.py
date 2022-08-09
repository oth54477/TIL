t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    count = [0] * 5000
    for _ in range(n):
        a, b = map(int, input().split())
        for bus in range(a - 1, b):
            count[bus] += 1
    p = int(input())
    result = [count[int(input()) - 1] for _ in range(p)]
    print(f'#{tc}', end=' ')
    print(*result)