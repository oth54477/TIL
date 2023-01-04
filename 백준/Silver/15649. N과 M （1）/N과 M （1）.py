import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

for case in permutations(range(1, n + 1), m):
    print(*case)