import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n, depth):
    global result
    if depth >= 4:
        result = 1
        return
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth+1)
            visited[i] = 0

result = 0
for i in range(N):
    if result:
        break
    visited = [0] * 2001
    dfs(i, 0)

print(result)
