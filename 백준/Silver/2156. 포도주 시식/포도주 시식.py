import sys

input = sys.stdin.readline

N = int(input().strip())
cups = [int(input().strip()) for _ in range(N)]

dp = [0] * N

dp[0] = cups[0]

if N > 1:
    dp[1] = cups[0] + cups[1]

if N > 2:
    dp[2] = max(cups[2] + cups[1], cups[2] + cups[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 3] + cups[i - 1] + cups[i], dp[i - 2] + cups[i])

print(dp[N - 1])
