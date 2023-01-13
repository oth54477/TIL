import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input().strip())

heap = []
for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, x)