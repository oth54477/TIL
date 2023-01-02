import sys

input = sys.stdin.readline
circles = []
error = False
n = int(input())

for i in range(n):
    x, r = map(int, input().split())
    circles.append((x - r, i, 0))
    circles.append((x + r, i, 1))

circles.sort()
stack = []
points = set()
for point, i, flag in circles:
    if point in points:
        error = True
        break
    if flag == 0:
        stack.append((point, i))
    elif stack[-1][1] != i:
        error = True
        break
    else:
        points.add(point)
        stack.pop()
if error:
    print('NO')
else:
    print('YES')
