import sys
input = sys.stdin.readline
def dfs(arr):
    global n, m
    if len(arr) == m:
        print(*arr)
        return
    for i in numbers:
        if arr:
            if arr[-1] > i:
                continue
        dfs(arr + [i])
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
dfs([])
