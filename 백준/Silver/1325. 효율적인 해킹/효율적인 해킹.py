import sys
from collections import defaultdict, deque

input = sys.stdin.readline

graph = defaultdict(set)

N, M = map(int, input().strip().split())

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[b].add(a)


result = defaultdict(list)
max_result = 0
for i in range(1, N+1):
    dq = deque([i])
    cnt = 0
    visited = [0] * (N+1)
    visited[i] = 1
    while dq:
        n = dq.popleft()
        cnt += 1
        for next_n in graph[n]:
            if not visited[next_n]:
                visited[next_n] = 1
                dq.append(next_n)
    result[cnt].append(i)
    max_result = max(max_result, cnt)

print(*result[max_result])
