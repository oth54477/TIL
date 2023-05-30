import sys

input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
S = input().strip()

p = "IO" * N + "I"

point = N * 2 + 1

count = 0

s = S[:point]
if s == p:
    count += 1
for i in range(point, M):
    s = "".join([s[1:], S[i]])
    if s == p:
        count += 1
print(count)
