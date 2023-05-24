def solution(n):
    memo = {0: 0, 1:1, 2:1}

    x = 3
    while x <= n:
        memo[x] = memo[x-1] + memo[x-2]
        x+= 1

    return memo[n] % 1234567