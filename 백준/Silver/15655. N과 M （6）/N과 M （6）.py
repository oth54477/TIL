import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for case in combinations(numbers, m):
    print(*case)