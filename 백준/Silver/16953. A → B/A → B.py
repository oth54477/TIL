import sys
from collections import deque

input = sys.stdin.readline

def case1(x):
    return x*2

def case2(x):
    return x*10 + 1

a, b = map(int ,input().strip().split())
dq = deque([(a,1)])
result = -1
cnt = 1
while  dq:
    x, cnt = dq.popleft()
    x1 = case1(x)
    if x1 < b:
        dq.append((case1(x), cnt+1))
    elif x1 == b:
        result = cnt
        break
    x2 = case2(x)
    if x2 < b:
        dq.append((case2(x), cnt + 1))
    elif x2 == b:
        result = cnt
        break
else:
    result = -2
print(result + 1)