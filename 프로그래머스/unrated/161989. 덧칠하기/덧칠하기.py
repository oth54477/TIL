from collections import deque

def solution(n, m, section):
    dq = deque(section)
    count = 0
    while dq:
        count += 1
        start = dq.popleft()
        while dq and dq[0] - start < m:
            dq.popleft()
    return count