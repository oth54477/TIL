import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = [int(input().strip()) for _ in range(n)]
dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4
start = 4
for number in numbers:
    for i in range(start,number+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        start = i
    print(dp[number])