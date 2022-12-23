import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    dq = deque(enumerate(map(int, input().split())))
    count = 0
    while dq:
        if dq[0][1] == max(dq, key=lambda x: x[1])[1]:
            idx, value = dq.popleft()
            count += 1
            if idx == m:
                break
        else:
            dq.rotate(-1)
    print(count)