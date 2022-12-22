import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

commands = {
    'push': lambda x: dq.append(int(x[0])), 
    'pop': lambda x: print(dq.popleft()) if dq else print(-1), 
    'size': lambda x: print(len(dq)),
    'empty': lambda x: print(0) if dq else print(1),
    'front': lambda x: print(dq[0]) if dq else print(-1),
    'back': lambda x: print(dq[-1]) if dq else print(-1),
    }

for _ in range(int(input())):
    command, *x = input().split()

    commands[command](x)


