# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN

def chk_parent(node):
    if not visited[node]:
        parents = parent[node]
        if parents:
            for p_node in parents:
                chk_parent(p_node)
        result.append(node)
        visited[node] = True



def order(node):
    if not visited[node]:
        chk_parent(node)
        for c_node in graph[node]:
            order(c_node)



for t in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    parent = [[] for _ in range(v+1)]
    visited = [True] + [False] * v
    result = []
    for i in range(0, e*2, 2):
        p, c = edges[i], edges[i+1]
        graph[p].append(c)
        parent[c].append(p)

    order(1)
    while visited.count(False):
        order(visited.index(False))
    print(f'#{t}', *result)
