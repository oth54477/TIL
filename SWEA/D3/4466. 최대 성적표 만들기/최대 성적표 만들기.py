for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print(f'#{t} {sum(scores[:k])}')