import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().strip().split())
poketmons = defaultdict(int)
index = defaultdict(int)
for i in range(1, n+1):
    temp = input().strip()
    poketmons[temp] = i
    index[i] = temp
for _ in range(m):
    temp = input().strip()
    if temp.isnumeric():
        print(index[int(temp)])
    else:
        print(poketmons[temp])