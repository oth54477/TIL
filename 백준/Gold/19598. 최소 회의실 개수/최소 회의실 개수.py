import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input().strip())

times = [list(map(int ,input().strip().split())) for _ in range(n)]
times.sort()
heap = []
heappush(heap, times[0][1])

for i in range(1,n):
    if times[i][0] < heap[0]:
        heappush(heap, times[i][1])
    else:
        heappop(heap)
        heappush(heap, times[i][1])
print(len(heap))