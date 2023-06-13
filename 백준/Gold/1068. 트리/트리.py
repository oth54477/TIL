import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N = int(input().strip())

tree = list(map(int, input().strip().split()))

M = int(input().strip())

graph = defaultdict(list)

for i, v in enumerate(tree):
    graph[v].append(i)

dq = deque([-1])
count = 0
while dq:
    n = dq.popleft()
    nodes = graph[n]
    if nodes:
        for node in nodes:
            if node != M:
                dq.append(node)
            elif len(nodes) == 1:
                count += 1
    else:
        count += 1

if n == -1:
    count = 0

print(count)