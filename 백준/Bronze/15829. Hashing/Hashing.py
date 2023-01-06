import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(lambda x: ord(x) - 96 ,input().strip()))
result = 0

for i, v in enumerate(arr):
    result += v * 31**(i)

print(result % 1234567891)
