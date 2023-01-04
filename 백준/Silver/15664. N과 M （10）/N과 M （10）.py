import sys
input = sys.stdin.readline
def dfs(arr,numbers):
    global n, m
    if len(arr) == m:
        if arr not in result:
            print(*arr)
        result.add(arr)
        return
    for idx, i in enumerate(numbers):
        if arr:
            if arr[-1] > i:
                continue
        dfs(arr + (i,), numbers[:idx] + numbers[idx+1:])
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = set()
dfs((),numbers)
