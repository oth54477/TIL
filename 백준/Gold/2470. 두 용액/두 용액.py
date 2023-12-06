import sys
from itertools import combinations
input = sys.stdin.readline


N = int(input().strip())

arr = sorted(map(int, input().strip().split()))

left, right = 0, (N-1)
result = [10000000000, -1, -1]

def chk_diff(left, right):
    diff = arr[right] + arr[left]
    abs_diff = abs(diff)
    if abs_diff < result[0]:
        result[0], result[1], result[2] = abs_diff, arr[left], arr[right]
    return diff

while left != right and arr[left] <= arr[right]:
    diff = chk_diff(left, right)
    if diff == 0:
        break
    elif diff > 0:
        if arr[right-1] < 0:
            left += 1
        else:
            right -= 1
    else:
        if arr[left+1] > 0:
            right -= 1
        else:
            left += 1

for p1, p2 in combinations(arr[max(0, left - 2): min(N, left + 3)], 2):
    diff = abs(p1 + p2)
    if diff < result[0]:
        result = [diff, p1, p2]

print(*sorted(result[1:]))