import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


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
            dfs(i, 0)
            count += 1

print(count)