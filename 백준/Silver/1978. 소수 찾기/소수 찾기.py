import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
cnt = n
for n in numbers:
    if n <= 1:
        cnt -= 1
        continue
    for i in range(2, n):
        if n % i == 0:
            cnt -= 1
            break
print(cnt)