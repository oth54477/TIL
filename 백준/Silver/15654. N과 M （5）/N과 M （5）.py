import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for case in permutations(numbers, m):
    print(*case)