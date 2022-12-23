import sys
from collections import deque

input = sys.stdin.readline

input()

dq = deque(enumerate(map(int, input().split())))
result = []
now = 0
while dq:
    idx, value = dq.popleft()
    result.append(idx + 1)

    if value > 0:
        value = -(value - 1)
    else:
        value = -value
    dq.rotate(value)

print(*result)
