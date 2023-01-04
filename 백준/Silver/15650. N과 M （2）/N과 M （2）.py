import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

for case in combinations(range(1, n + 1), m):
    print(*case)