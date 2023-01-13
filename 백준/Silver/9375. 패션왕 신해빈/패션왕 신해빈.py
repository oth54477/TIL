import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    clothes = defaultdict(int)
    for _ in range(n):
        result, temp = 0, 1
        name, kind = input().strip().split()
        clothes[kind] += 1
    result = 1
    for v in clothes.values():
        result *= (v + 1)
    print(result - 1)

   