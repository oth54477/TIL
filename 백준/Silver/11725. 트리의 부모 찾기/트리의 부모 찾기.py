import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().strip())

# 기본값이 set인 defaultdict
graph = defaultdict(set)

# 그래프 연결
for _ in range(N-1):
    n, m = map(int, input().strip().split())
    graph[n].add(m)
    graph[m].add(n)

# 부모 노드를 기록하고, 방문 체크를 하기 위한 리스트
result = [-1, -1] + [0] * (N-1)
dq = deque([1])

while dq:
    node = dq.popleft()
    linked_node = graph[node]
    for n in linked_node:
        if not result[n]:
            result[n] = node
            dq.append(n)

print(*result[2:], sep="\n")
