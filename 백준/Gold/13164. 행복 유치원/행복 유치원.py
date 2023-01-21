import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().strip().split())
height_list = list(map(int, input().strip().split()))

d = []
for i in range(n-1):
    d.append(height_list[i+1] - height_list[i])
d.sort()
print(sum(d[:n-k]))
