import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1
for i, v in enumerate(arr):
    for _ in range(v):
        print(i)