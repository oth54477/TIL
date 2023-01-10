import sys

input = sys.stdin.readline

n = int(input())

times = list(map(int, input().strip().split()))

result, temp = 0, 0
for time in sorted(times):
    temp += time
    result += temp
print(result)