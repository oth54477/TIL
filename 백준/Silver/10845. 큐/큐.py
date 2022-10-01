import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):

    c, *n = map(lambda x: int(x) if x.isdigit() else x, input().split())
    if c == 'push':
        q.append(n)
    elif c == 'pop':
        if q:
            print(*q.popleft())
        else:
            print(-1)
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if q:
            print(*q[0])
        else:
            print(-1)
    elif c == 'back':
        if q:
            print(*q[-1])
        else:
            print(-1)
