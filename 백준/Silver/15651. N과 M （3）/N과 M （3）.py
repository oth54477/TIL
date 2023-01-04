import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())

for case in product(range(1, n + 1), repeat=m):
    print(*case)