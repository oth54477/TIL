import sys
from collections import deque

input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data

        self.prev = None

N, K = map(int, input().strip().split())

if N == K:
    print(0)
    print(K)
else:
    moves = [(lambda x: x+1), (lambda x: x-1), (lambda x: x*2)]

    dq = deque([Node((N, 0))])
    flag = True
    visited = set()

    while flag and dq:
        head = dq.popleft()
        x, cnt = head.data
        for move in moves:
            nx = move(x)

            if nx == K:
                flag = False
                cnt += 1
                break

            if nx not in visited and 0 <= nx <= 100000:
                next_head = Node((nx, cnt + 1))
                next_head.prev = head
                visited.add(nx)
                dq.append(next_head)

    print(cnt)
    result = [K]
    while head.prev != None:
        result.append(head.data[0])
        head = head.prev
    print(N, *result[::-1])