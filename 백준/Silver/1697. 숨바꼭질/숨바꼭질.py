import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(v):
    dq = deque([v])
    while dq:
        v = dq.popleft()
        if v == k:
            return counts[v]
        for i in range(1,4):
            nv = case[i](v)
            if 0 <= nv < MAX and counts[nv] == 0:
                counts[nv] = counts[v] + 1
                dq.append(nv)



case = {1: lambda x:x+1, 2: lambda x: x-1, 3: lambda x: x*2}

MAX = 100001
n, k = map(int, input().strip().split())
counts = defaultdict(int)
result = bfs(n)
print(result)