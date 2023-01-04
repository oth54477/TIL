import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for case in product(numbers, repeat=m):
    print(*case)