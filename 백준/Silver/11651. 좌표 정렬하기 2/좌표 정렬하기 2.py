import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]

for i in sorted(arr, key=lambda x: (x[1], x[0])):
    print(*i)