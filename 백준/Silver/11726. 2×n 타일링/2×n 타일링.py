import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0,1,2] 
if n <= 2:
    print(dp[n])
else:
    now = 2
    old = 1
    for i in range(3, n+1):
        now, old = now + old, now
    print(now%10007)