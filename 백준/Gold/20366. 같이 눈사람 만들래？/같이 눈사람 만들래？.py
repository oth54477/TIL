import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_diff = 999999999999999
for i, j in combinations(arr, 2):
    if min_diff == 0:
        break
    i_idx = bisect_left(arr, i)
    j_idx = bisect_right(arr, j)-1
    if j_idx - i_idx >= 3:
        left, right = i_idx+1, j_idx-1
        snow1 = i + j
        while left < right:
            l, r = arr[left], arr[right]
            snow2 = l + r
            diff = snow1 - snow2
            min_diff = min(min_diff, abs(diff))
            if diff > 0:
                left += 1
            elif diff < 0:
                right -= 1
            else:
                break
print(min_diff)
