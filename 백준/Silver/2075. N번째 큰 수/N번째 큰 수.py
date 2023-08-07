import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

heap = []
for idx, line in enumerate(arr):
    for n in line:
        if idx == 0:
            heappush(heap, n)
        else:
            if heap[0] < n:
                heappop(heap)
                heappush(heap,n)

print(heap[0])