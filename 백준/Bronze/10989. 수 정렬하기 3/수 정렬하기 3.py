import sys
input = sys.stdin.readline
arr = [0] * 10001
for _ in range(int(input())):
    arr[int(input())] += 1
for i, v in enumerate(arr):
    if v:
        for _ in range(v):
            print(i)
