import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    dq = deque([start])
    visited[start] = True
    while dq:
        node = dq.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)


n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n + 1)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

print(count)