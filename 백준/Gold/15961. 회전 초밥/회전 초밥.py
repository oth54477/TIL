import sys
from collections import defaultdict

input = sys.stdin.readline


N, D, K, C = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]

left, right = 0, K-1
counter = defaultdict(int)

def move(left, right):
    left += 1
    right += 1
    if right >= N:
        right = 0
    return left, right

for i in range(0, K):
    counter[arr[i]] += 1
counter[C] += 1
max_cnt = len(counter)

while left < N-1 and max_cnt <= K:
    counter[arr[left]] -= 1
    if counter[arr[left]] == 0:
        del counter[arr[left]]
    left, right = move(left, right)
    counter[arr[right]] += 1
    max_cnt = max(max_cnt, len(counter))

print(max_cnt)