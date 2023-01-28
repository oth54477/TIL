import sys

input = sys.stdin.readline

n = int(input().strip())

result = 0
for i in range(1,n+1):
    result += i
print(result)