import sys
from heapq import heappush, heappop

input = sys.stdin.readline

heap = []
n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    if x != 0:
        heappush(heap, -x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))