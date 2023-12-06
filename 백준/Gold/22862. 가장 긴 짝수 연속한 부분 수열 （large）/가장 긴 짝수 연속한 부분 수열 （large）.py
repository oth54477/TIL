import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

left, right = 0, 0

def chk_odd(number):
    return True if number % 2 != 0 else False

dq = deque([])
odd_cnt = 0
result = {0}
flag = False

while left < N:
    if right >= N:
        flag = True
        right = N-1
    if flag:
        result.add(len(dq) - odd_cnt)
        left += 1
    else:
        r = arr[right]
        if chk_odd(r):
            odd_cnt += 1
            dq.append(r)

        else:
            dq.append(r)
            if odd_cnt > K:
                while True:
                    left += 1
                    n = dq.popleft()
                    if chk_odd(n):
                        odd_cnt -= 1
                    if not chk_odd(arr[left]):
                        break
            else:
                result.add(len(dq) - odd_cnt)
        right += 1

print(max(result))