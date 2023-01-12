import sys
input = sys.stdin.readline

def fib(n):
    if n in memo:
        return memo[n]    
    memo[n] = list(map(sum,zip(fib(n-1), fib(n-2))))
    return memo[n]

t = int(input().strip())

memo = {0: [1,0], 1: [0,1], 2: [1, 1]}
for _ in range(t):
    n = int(input().strip())

    print(*fib(n))
