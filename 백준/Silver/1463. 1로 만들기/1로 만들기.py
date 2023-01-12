import sys
input = sys.stdin.readline
x = int(input().strip())
memo = {1:0, 2:1, 3:1}

for i in range(3, x+1):
    memo[i] = memo[i-1] + 1
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1)
print(memo[x])