import sys
from collections import deque
input = sys.stdin.readline

x = list(map(lambda x: int(x) if x.isdigit() else x, input().strip().replace('+', ',+,').replace('-', ',-,').split(',')))

dq = deque()
temp = 0
for i in x:
    if i == '-':
        dq.append(temp)
        temp = 0
        dq.append('-')
    elif i == '+':
        pass
    else:
        temp += i
else:
    dq.append(temp)

result = 0
while dq:
    x = dq.popleft()
    if x == '-':
        result -= dq.popleft()
    else:
        result += x
print(result)
