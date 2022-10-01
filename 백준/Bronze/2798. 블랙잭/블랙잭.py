import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
min_d,result = 99999999999, 0
for case in permutations(arr, 3):
    s = sum(case)
    d = m-s
    if d >= 0:
        if min_d >= d:
            min_d = d
            result = s
print(result)