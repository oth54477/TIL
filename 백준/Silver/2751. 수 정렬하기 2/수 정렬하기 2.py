import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
print(*sorted(arr), sep='\n')