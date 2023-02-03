import sys

input = sys.stdin.readline

total = int(input().strip())
n = int(input().strip())
for _ in range(n):
  cost, x = map(int, input().strip().split())
  total -= (cost * x)
if total == 0:
  print('Yes')
else:
  print('No')
