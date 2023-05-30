import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = defaultdict(set)
result = (0, 9999999999)
for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].add(b)
    graph[b].add(a)

for i in range(1, N + 1):
    dq = deque()
    visited = set()
    count = 0
    for x in graph[i]:
        dq.append((x, 1))
    while dq and len(visited) < N - 1:
        p, cnt = dq.popleft()
        if p not in visited and p != i:
            count += cnt
            visited.add(p)
        for x in graph[p]:
            dq.append((x, cnt + 1))
    if count < result[1]:
        result = (i, count)
    elif count == result[1]:
        result = (min(i, result[0]), count)
print(result[0])
