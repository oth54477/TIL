import math
from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]
    cost = 0  # MST의 가중치 총합(== 최소 비용)

    while heap:
        # 1. 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist, min_node = heappop(heap)  # 최소힙이므로 튜플의 첫 번째 원소를 기준으로 최소값 pop
        if visited[min_node]:
            continue  # 이미 MST에 포함된 정점이라면 무시

        # 2. 해당 정점을 MST에 포함하고 비용 총합을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 heappush
        for next_node, dist in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost

for t in range(1, int(input()) + 1):
    n = int(input())  # 섬의 개수
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt(((x_arr[i] - x_arr[j]) ** 2 + (y_arr[i] - y_arr[j]) ** 2))
                w = (distance ** 2) * e
                graph[i].append((j, w))

    print(f'#{t} {int(round(prim(1), 0))}')  # 1번 정점에서 시작