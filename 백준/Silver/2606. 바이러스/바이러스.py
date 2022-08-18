def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)

dfs(1)
print(sum(visited) - 1)
