import sys
input = sys.stdin.readline

n = int(input().strip())
prices = [int(input().strip()) for _ in range(n)]

prices.sort(reverse=True)

result = 0
for idx, price in enumerate(prices):
    if (idx + 1) % 3 != 0:
        result += price
print(result)