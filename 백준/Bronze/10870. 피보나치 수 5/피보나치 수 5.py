def fibo(n):
    if len(memo) <= n:
        memo.append(fibo(n-2) + fibo(n-1))
    return memo[n]
memo = [0,1]
print(fibo(int(input())))