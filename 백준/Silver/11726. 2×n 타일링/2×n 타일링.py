import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0,1,2] 

if n <= 2:
    print(dp[n])
else:
    dp += [0] * (n-2)
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)

