import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(4)]
for _ in range(N):
    for i, v in enumerate(map(int, input().split())):
        arr[i].append(v)

ab = []
cd = []
result = 0

for i in range(N):
    for j in range(N):
        ab.append(arr[0][i] + arr[1][j])
        cd.append(arr[2][i] + arr[3][j])
ab.sort()
cd.sort()


idx, jdx = 0, N*N-1
result = 0

while idx < N*N and jdx >= 0:
    abcd = ab[idx] + cd[jdx]
    if abcd  < 0:
        idx += 1
    elif abcd > 0:
        jdx -= 1
    else:
        ab_same = bisect_right(ab, ab[idx]) - 1
        cd_same = bisect_left(cd, cd[jdx])
        result += (ab_same - idx + 1) * (jdx - cd_same + 1)
        idx, jdx = ab_same + 1, cd_same - 1

print(result)