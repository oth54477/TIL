def solution(x, n):
    return [0 for _ in range(n)] if x == 0 else [i for i in range(x, x * (n + 1), x)]