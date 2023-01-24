import sys

input = sys.stdin.readline

n = int(input().strip())
points = list(map(int ,input().strip().split()))

table = dict()
for i, v in enumerate(sorted(set(points))):
    table[v] = i
result = []
for point in points:
    result.append(table[point])
print(*result)