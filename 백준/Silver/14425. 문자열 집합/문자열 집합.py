import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
S = set(input().strip() for _ in range(N))
CHECK_STRING = [input().strip() for _ in range(M)]

count = 0
for s in CHECK_STRING:
    if s in S:
        count += 1
print(count)