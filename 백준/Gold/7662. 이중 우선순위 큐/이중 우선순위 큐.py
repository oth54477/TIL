import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    min_heap = []
    max_heap = []
    counter = defaultdict(int)
    for _ in range(k):
        comm, value = input().strip().split()
        v = int(value)
        if comm == "I":
            heappush(min_heap, v)
            heappush(max_heap, (-v, v))
            counter[v] += 1
        elif comm == "D":
            if v == -1:
                while min_heap:
                    temp = heappop(min_heap)
                    if counter[temp] > 0:
                        counter[temp] -= 1
                        break

            elif v == 1 and max_heap:
                while max_heap:
                    temp = heappop(max_heap)[1]
                    if counter[temp] > 0:
                        counter[temp] -= 1
                        break

    if sum(counter.values()) == 0:
        print("EMPTY")
    else:
        temp = list(map(lambda y: y[0], filter(lambda x: x[1] != 0, counter.items())))
        print(max(temp), min(temp))