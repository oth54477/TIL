import sys
input = sys.stdin.readline

n = int(input().strip())
ropes = [int(input().strip()) for _ in range(n)]
ropes.sort()
weights = []
for idx, rope in enumerate(ropes):
    weights.append(rope * (n - idx))
print(max(weights))