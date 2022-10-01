import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [False, False] + [True] * (m-1)

k = int(m ** 0.5)
for i in range(2, k+1):
    if arr[i]:
        for j in range(i + i, m+1, i):
            arr[j] = False
print(*[i for i in range(n, m+1) if arr[i]], sep='\n')

