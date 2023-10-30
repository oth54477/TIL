import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().strip())

graph = [0] * (N+1)

same = set()

for i in range(1, N+1):
    n = int(input().strip())
    graph[i] = n
    if i == n:
        same.add(n)

def dfs(n):
    global max_cnt, result
    if not visited[n]:
        visited[n] = 1
        a_set.add(n)
        b_set.add(graph[n])
        if a_set == b_set:
            result.update(a_set)
        dfs(graph[n])

result = set()
max_cnt = 0

for i in range(1, N+1):
    visited = [0] * (N+1)
    a_set = set()
    b_set = set()
    if i not in same:
        dfs(i)

result.update(same)
print(len(result))
print(*sorted(result), sep="\n")