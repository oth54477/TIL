
import sys

input = sys.stdin.readline

N = int(input().strip())

dp = [0,1,3] 
if N <= 2:
    print(dp[N])
else:
    now = 3
    old = 1
    for i in range(3, N+1):
        now, old = now + old*2, now
    print(now%10007)